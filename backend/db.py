import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'database.db')


def get_db():
    """Get a database connection with Row factory."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Create tables if they don't exist."""
    conn = get_db()
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            patient_name TEXT NOT NULL,
            patient_age INTEGER,
            image_path TEXT NOT NULL,
            diagnosis TEXT NOT NULL,
            confidence REAL NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')
    conn.commit()
    conn.close()


def create_user(username, password_hash):
    """Insert a new user. Returns True on success, False if username exists."""
    conn = get_db()
    try:
        conn.execute('INSERT INTO users (username, password_hash) VALUES (?, ?)',
                     (username, password_hash))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def get_user(username):
    """Fetch a user row by username."""
    conn = get_db()
    user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
    conn.close()
    return user


def save_prediction(user_id, patient_name, patient_age, image_path, diagnosis, confidence):
    """Save a prediction result to the database."""
    conn = get_db()
    conn.execute(
        'INSERT INTO predictions (user_id, patient_name, patient_age, image_path, diagnosis, confidence) VALUES (?, ?, ?, ?, ?, ?)',
        (user_id, patient_name, patient_age, image_path, diagnosis, confidence)
    )
    conn.commit()
    conn.close()


def get_predictions(user_id):
    """Get all predictions for a user, newest first."""
    conn = get_db()
    rows = conn.execute(
        'SELECT * FROM predictions WHERE user_id = ? ORDER BY created_at DESC', (user_id,)
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def get_prediction_stats(user_id):
    """Get summary stats for the dashboard."""
    conn = get_db()
    total = conn.execute('SELECT COUNT(*) FROM predictions WHERE user_id = ?', (user_id,)).fetchone()[0]
    benign = conn.execute('SELECT COUNT(*) FROM predictions WHERE user_id = ? AND diagnosis = ?', (user_id, 'Benign')).fetchone()[0]
    malignant = conn.execute('SELECT COUNT(*) FROM predictions WHERE user_id = ? AND diagnosis = ?', (user_id, 'Malignant')).fetchone()[0]
    conn.close()
    return {'total': total, 'benign': benign, 'malignant': malignant}
