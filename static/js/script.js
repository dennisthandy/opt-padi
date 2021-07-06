const iconMenu = document.querySelector(".nav__icon--menu");
const mobileNavigation = document.querySelector(".nav--mobile");
const iconClose = document.querySelector('.nav__icon--close');

iconMenu.addEventListener('click', () => {
    mobileNavigation.classList.remove('hidden')
});

iconClose.addEventListener('click', () => {
    mobileNavigation.classList.add('hidden')
});