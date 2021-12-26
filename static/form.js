setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);

document.getElementById('hello').addEventListener("click", helloModal);

function helloModal() {
  alert ("Hello there how'd you find me?!?");
}