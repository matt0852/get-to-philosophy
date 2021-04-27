const socket = io()

var search_form = document.getElementById('search_form')
var search_input = document.getElementById('search_input')
var search_results = document.getElementById('search_results')

search_form.addEventListener('submit', (err) => {
    err.preventDefault()
    if (search_input.value) {
        socket.emit('search', search_input.value)
        search_input.value = ''
    }
})

socket.on('result', link => {
    var result = document.createElement('li')
    result.textContent = link
    search_results.appendChild(result)
})

socket.on('clear', () => {
    while(search_results.firstChild) {
        search_results.removeChild(search_results.firstChild)
    }
})