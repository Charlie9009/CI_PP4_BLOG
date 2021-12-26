/**
 * This first javascript function was used from Code Institutes Django Blog
 * Getting the id of msg and closing the alert in 4 seconds
 */
setTimeout(function() {
    let messages = document.getElementById('msg');
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);

/**
 * This function was added as a fun secret for those who finds it
 * Adding an eventlistener to the header and sending an alert
 */
document.getElementById('hello').addEventListener("click", helloModal);

function helloModal() {
  alert ("Hello there how'd you find me?!?");
}