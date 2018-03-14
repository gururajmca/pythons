var express = require('express')
var path = require('path')
var app = express()

app.set('port', (process.env.PORT || 5000))
app.use('/data', express.static(path.join(__dirname, 'data')))
app.use(express.static(__dirname + '/public'))

app.get('/', function(request, response) {
  //response.send('Hello World!');
  response.sendFile(__dirname + '/index.html');
})

app.listen(app.get('port'), function() {
  console.log("Node app is running at localhost:" + app.get('port'))
})
