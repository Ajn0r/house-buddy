let newsletter = document.getElementById('newsletter')
newsletter.addEventListener('submit', function (e) {
    e.preventDefault()
    newsletter.innerHTML = '<p>Thank you for subscribing!</p>'
})