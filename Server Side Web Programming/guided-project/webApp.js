const http = require("http");

const ip = "localhost";     // localhost
const port = 8080;        // port number

const server = http.createServer(function(request, response){
    response.statusCode = 200;
    response.setHeader("Content-Type", "text/plain");
    response.end("TESTING!!!!!");
});

server.listen(port, ip, function(){
    console.log("Node.js server is listening at http://" + ip +":"+ port);
});
