document.addEventListener('DOMContentLoaded', () => {
    const dropZone = document.getElementById('drop-zone');
    const fileInput = document.getElementById('file-input');
    const previewBox = document.getElementById('preview-box');
    const imagePreview = document.getElementById('image-preview');
    const dropContent = document.getElementById('drop-content');
    const removeBtn = document.getElementById('remove-image');
    const analyzeBtn = document.getElementById('analyze-btn');
    const form = document.getElementById('predict-form');

    // Drag and drop
    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(evt => {
        dropZone.addEventListener(evt, e => { e.preventDefault(); e.stopPropagation(); }, false);
    });
    ['dragenter', 'dragover'].forEach(evt => {
        dropZone.addEventListener(evt, () => dropZone.classList.add('dragover'), false);
    });
    ['dragleave', 'drop'].forEach(evt => {
        dropZone.addEventListener(evt, () => dropZone.classList.remove('dragover'), false);
    });

    dropZone.addEventListener('drop', e => {
        const files = e.dataTransfer.files;
        if (files.length) {
            fileInput.files = files;
            showPreview(files[0]);
        }
    });

    fileInput.addEventListener('change', function () {
        if (this.files.length) showPreview(this.files[0]);
    });

    function showPreview(file) {
        if (!file.type.startsWith('image/')) {
            alert('Please select an image file.');
            return;
        }
        const reader = new FileReader();
        reader.onloadend = () => {
            imagePreview.src = reader.result;
            dropContent.classList.add('hidden');
            previewBox.classList.remove('hidden');
            checkReady();
        };
        reader.readAsDataURL(file);
    }

    removeBtn.addEventListener('click', e => {
        e.stopPropagation();
        fileInput.value = '';
        previewBox.classList.add('hidden');
        dropContent.classList.remove('hidden');
        analyzeBtn.disabled = true;
    });

    // Enable button only when all fields are filled
    function checkReady() {
        const name = document.getElementById('patient_name').value.trim();
        const age = document.getElementById('patient_age').value.trim();
        const hasFile = fileInput.files && fileInput.files.length > 0;
        analyzeBtn.disabled = !(name && age && hasFile);
    }

    document.getElementById('patient_name').addEventListener('input', checkReady);
    document.getElementById('patient_age').addEventListener('input', checkReady);

    // Loading state on submit
    form.addEventListener('submit', () => {
        analyzeBtn.disabled = true;
        analyzeBtn.innerHTML = '<div class="spinner-sm"></div> Analyzing...';
    });
});
