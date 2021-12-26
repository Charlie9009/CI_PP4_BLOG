let closeModal = document.getElementById('msg');
let bootstrap = document.getElementsByClassName('alert-success');
closeModal.addEventListener('click', () => {
    bootstrap.close();
});