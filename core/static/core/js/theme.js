// переключение иконок
let theme = true
let sun = document.querySelector('.sun-img')
let moon = document.querySelector('.moon-img')
let btn_theme = document.querySelector('.btn-theme')

btn_theme.addEventListener('click', toggleTheme)

setTheme(localStorage.getItem('theme') === 'true')

function setTheme(value){
    theme = value
    localStorage.setItem('theme', value)
    document.body.setAttribute('data-bs-theme', value ? 'dark' : 'light');
    sun.style.opacity = value ? '0' : '1';
    moon.style.opacity = value ? '1' : '0';
    sun.style.marginLeft = value ? '33px' : '0';
    moon.style.marginLeft = value ? '33px' : '0';

}
function toggleTheme() {
    setTheme(!theme)
}