import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.utils import secure_filename
from backend.auth import auth_bp, login_required
from backend.db import init_db, save_prediction, get_predictions, get_prediction_stats
from backend.model_service import load_ai_model, predict as predict_image

# ── App Setup ──
app = Flask(__name__)
app.secret_key = 'skinai_secret_key_2026'

UPLOAD_FOLDER = os.path.join('static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Register auth blueprint
app.register_blueprint(auth_bp)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# ── Routes ──
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('auth.login'))


@app.route('/dashboard')
@login_required
def dashboard():
    uid = session['user_id']
    stats = get_prediction_stats(uid)
    recent = get_predictions(uid)[:5]  # Last 5
    return render_template('dashboard.html', stats=stats, recent=recent)


@app.route('/predict', methods=['GET', 'POST'])
@login_required
def predict():
    if request.method == 'POST':
        patient_name = request.form.get('patient_name', '').strip()
        patient_age = request.form.get('patient_age', '')

        if not patient_name or not patient_age:
            flash('Please fill in patient name and age.', 'warning')
            return redirect(url_for('predict'))

        if 'image' not in request.files or request.files['image'].filename == '':
            flash('Please upload an image.', 'warning')
            return redirect(url_for('predict'))

        file = request.files['image']
        if not allowed_file(file.filename):
            flash('Invalid file type. Use JPG or PNG.', 'danger')
            return redirect(url_for('predict'))

        try:
            filename = secure_filename(file.filename)
            os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)

            # Run AI prediction
            result = predict_image(filepath)

            # Save to database
            image_url = '/' + filepath.replace('\\', '/')
            save_prediction(
                session['user_id'],
                patient_name,
                int(patient_age),
                image_url,
                result['label'],
                result['confidence']
            )

            # Get the latest prediction to show on result page
            preds = get_predictions(session['user_id'])
            latest = preds[0] if preds else None

            return render_template('result.html', prediction=latest)

        except Exception as e:
            flash(f'Analysis error: {str(e)}', 'danger')
            return redirect(url_for('predict'))

    return render_template('predict.html')


@app.route('/patients')
@login_required
def patients():
    preds = get_predictions(session['user_id'])
    return render_template('patients.html', predictions=preds)


# ── Main ──
if __name__ == '__main__':
    os.makedirs('model', exist_ok=True)
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    init_db()
    load_ai_model()
    print('Starting SkinAI Platform...')
    app.run(debug=True, port=5000)
