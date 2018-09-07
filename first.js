var express = require('express');

var app = express();

app.get("/",function(req,res){

	console.log(req);

	res.status(200).send("done");

});



app.listen(8081)
