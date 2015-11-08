var express = require("express"),
    app = express(),
    port = 3000,
    publicDir = process.argv[2] || __dirname + '/public_html';

app.get("/", function (req, res) {
  res.sendfile("public_html/index.html");
});
app.get("/login", function (req, res) {
  res.sendfile("public_html/index.html");
});
app.get("/home", function (req, res) {
  res.sendfile("public_html/index.html");
});
app.get("/404", function (req, res) {
  res.sendfile("public_html/index.html");
});
app.get("/recommendations", function (req, res) {
  res.sendfile("public_html/index.html");
});

app.use(express.static(publicDir));

console.log("static server showing %s listening at %s", publicDir, port);
app.listen(port);