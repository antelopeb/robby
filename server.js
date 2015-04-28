/*
*	the server to handle requests to Vger
*/

var express = require('express'),
	app = express(),
	vger = require('./lib/vger.js'),
    bodyParser = require('body-parser')

// parse application/json
app.use(bodyParser.json())

// initialize Vger
vger.init()
	
app.get('/', function (req, res) {
  res.send('I am Vger. POST me a command.')
})

app.post('/', function(req, res){
    console.log("being asked "+req.body.q)
	vger.ask(req.body.q, function(ans){
		// send an answer here
        console.log("sending answer "+ans)
		res.send(ans)
	})
})

var server = app.listen(1618)

