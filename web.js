// Initiate requirements
var express = require("express");

// Create app using express
// Set ejs as template framework
var app = express();
app.use(express.static(__dirname + '/public'));
app.set('views', __dirname + "/views");
app.set('view engine', 'ejs');

// Set the port and listen
var port = process.env.PORT || 5000;
app.listen(port, function() {
  console.log("Listening on " + port);
});

app.get('/sudoku', function(request, response) {
  response.render('sudoku');
});

app.get('/phonelist', function(request, response) {
  response.render('phonelist');
});