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
let newsletter = document.getElementById('newsletter')
newsletter.addEventListener('submit', function (e) {
    e.preventDefault();
    newsletter.innerHTML = '<p>Thank you for subscribing!</p>'
})


/**
 * Code to send email to house buddy mail
 * Code for setting up Emailjs comes from 
 * the documentation or their webpage
 * https://www.emailjs.com/docs/sdk/send/
 * The code for the modal is from: 
 * https://www.w3schools.com/howto/howto_css_modals.asp
 */
window.onload = function () {
    let form = document.getElementById('contact-form')
    let modal = document.getElementById("contactModal");
    let span = document.getElementsByClassName("close")[0];
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        emailjs.sendForm("service_2qjf15k", "housebuddy", this)
            .then(function () {
                form.reset()
                modal.style.display = "block";
                span.onclick = function () {
                    modal.style.display = "none";
                }
                window.onclick = function (event) {
                    if (event.target == modal) {
                        modal.style.display = "none";
                    }
                }
            }, function (error) {
                alert('Message not sent, try again.', error);
            });
    });

}