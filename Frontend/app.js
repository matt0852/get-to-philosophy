const express = require('express')
const http = require('http')
const socketio = require('socket.io')
const axios = require('axios')

const app = express()
const server = http.createServer(app)
const io = socketio(server)

app.set('view engine', 'ejs')
app.use(express.urlencoded({ extended: true }))
app.use(express.json())
app.use(express.static(__dirname + '/views'))

app.get('/', (req, res) => {
    res.render('index.ejs')
})

app.use((req, res) => {
    res.status(404).render('error.ejs')
})

var obtain_next_link = async (io, link) => {
    var title = link
    while (title != 'Outline_of_philosophy') {
        res = await axios.get('http://127.0.0.1:5000/?title=' + title)
        var data = res.data.links[0]
        io.emit('result', data)
        title = data
    }
}

io.on('connection', socket => {
    console.log('a user connected');
    socket.on('search', search_term => {
        console.log(search_term)
        io.emit('clear')
        obtain_next_link(io, search_term)
    })
});

const port = 3000
server.listen(port, () => {
    console.log('Server running on port ' + port)
})