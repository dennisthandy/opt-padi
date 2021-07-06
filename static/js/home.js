// home
const form = document.querySelector('.form');
const inputFile = document.querySelector('.form__input--file');
const labelFile = inputFile.nextElementSibling;
const labelFileContent = labelFile.innerHTML;
const formSubmit = document.querySelector('.form__submit');
const loading = document.querySelector('.loading');
const result = document.querySelector('.result');

// home
inputFile.addEventListener('change', (e) => {
    let fileName = '';
    if (e.target.value) {
        fileName = e.target.value.split( '\\' ).pop();
    };

    fileName ? labelFile.querySelector('span').innerHTML = fileName : labelFile.innerHTML = labelFileContent;
});

form.addEventListener('submit', (e) => {
    loading.classList.remove('hidden');
    result.classList.add('hidden');
})