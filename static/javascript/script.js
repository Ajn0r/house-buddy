setTimeout(function () {
    let messages = document.getElementById("bs-message");
    let alert = new bootstrap.Alert(messages);
    alert.close();
}, 4000);

let newsletter = document.getElementById('newsletter')
newsletter.addEventListener('submit', function (e) {
    e.preventDefault();
    newsletter.innerHTML = '<p>Thank you for subscribing!</p>'
})

window.onload = function () {
    let form = document.getElementById('contact-form')
    let modal = document.getElementById("contactModal");
    let span = document.getElementsByClassName("close")[0];
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        emailjs.sendForm("service_2qjf15k", "housebuddy", this)
        form.reset()
        modal.style.display = "block";
        span.onclick = function () {
        modal.style.display = "none";
        }
    })
}

// Get the modal
