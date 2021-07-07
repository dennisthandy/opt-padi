// home
const form = document.querySelector('.form');
const inputFile = document.querySelector('.form__input--file');
const labelFile = inputFile.nextElementSibling;
const labelFileContent = labelFile.innerHTML;
const formSubmit = document.querySelector('.form__submit');
const loading = document.querySelector('.loading');
const result = document.querySelector('.result');
const download = document.querySelectorAll('.download')

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

function downloadData(label){
    var link = document.createElement('a');

    link.setAttribute('download', null);
    link.style.display = 'none';

    document.body.appendChild(link);

    for (var i = 0; i < 4; i++) {
        link.setAttribute('href', `/static/img/data/${label}/${label}_${i + 1}.jpg`);
        link.click();
    }

    document.body.removeChild(link);
}

download.forEach((element, index) => {
    element.addEventListener('click', () => {
        downloadData(element.id)
    })
})