document.addEventListener('DOMContentLoaded', () => {
    // ── Theme Toggle ──
    const toggle = document.getElementById('theme-toggle');
    if (toggle) {
        const html = document.documentElement;
        const icon = toggle.querySelector('i');
        const saved = localStorage.getItem('theme') || 'light';
        applyTheme(saved);

        toggle.addEventListener('click', () => {
            const next = html.getAttribute('data-theme') === 'light' ? 'dark' : 'light';
            applyTheme(next);
        });

        function applyTheme(theme) {
            html.setAttribute('data-theme', theme);
            localStorage.setItem('theme', theme);
            icon.className = theme === 'dark' ? 'ph ph-sun' : 'ph ph-moon';
        }
    }

    // ── Auto-dismiss flash messages ──
    document.querySelectorAll('.alert').forEach(el => {
        setTimeout(() => {
            el.style.opacity = '0';
            setTimeout(() => el.remove(), 400);
        }, 4000);
    });
});
