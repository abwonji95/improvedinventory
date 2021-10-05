let btn = document.querySelector('button');
let div = document.querySelector('div');

btn.addEventListener('click', () => {
    if (div.style.display == 'none') {
        div.style.display = 'block';
    } else {
        div.style.display = 'none';
    }
})

var myModal = document.getElementById('myModal')

myModal.addEventListener('show.bs.modal', function(event) {
    if (!data) {
        return event.preventDefault() // stops modal from being shown
    }
})