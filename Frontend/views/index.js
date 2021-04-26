const socket = io()

var search_form = document.getElementById('search_form')
var search_input = document.getElementById('search_input')

search_form.addEventListener('submit', (err) => {
    err.preventDefault()
    if (search_input.value) {
        socket.emit('search', search_input.value)
        search_input.value = ''
    }
})