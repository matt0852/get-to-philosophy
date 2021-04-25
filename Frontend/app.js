const express = require('express')
const app = express()
app.set('view engine', 'ejs')
app.listen(3000)

app.get('/', (req, res) => {
    res.render('index.ejs')
})

app.use((req, res) => {
    res.status(404).render('error.ejs')
})