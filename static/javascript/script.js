/**
 * Function to automatically close bootstrap alerts
 * the code is greatly inspired from the walkthough
 * 'I think therefore I blog' with CodeInstitute
 */
setTimeout(function () {
    let messages = document.getElementById("bs-message");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 3000);


/**
 * Changes the innter html if the user submits the form.
 */
let newsletter = document.getElementById('newsletter');
newsletter.addEventListener('submit', function (e) {
    e.preventDefault();
    newsletter.innerHTML = '<p>Thank you for subscribing!</p>';
});

