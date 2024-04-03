const themeToggle = document.getElementById('theme-toggle');
const themeIcon = document.getElementById('theme-icon');
const htmlTag = document.querySelector('html');


const storedTheme = localStorage.getItem('theme');
if (storedTheme) {
    htmlTag.setAttribute('data-bs-theme', storedTheme);
    if (storedTheme === 'dark') {
        themeIcon.classList.replace('bi-moon', 'bi-sun');
    }
}

themeToggle.addEventListener('click', function () {
    if (htmlTag.getAttribute('data-bs-theme') === 'dark') {
        htmlTag.removeAttribute('data-bs-theme');
        themeIcon.classList.replace('bi-sun', 'bi-moon');
        localStorage.setItem('theme', 'light');
    } else {
        htmlTag.setAttribute('data-bs-theme', 'dark');
        themeIcon.classList.replace('bi-moon', 'bi-sun');
        localStorage.setItem('theme', 'dark');
    }
});
