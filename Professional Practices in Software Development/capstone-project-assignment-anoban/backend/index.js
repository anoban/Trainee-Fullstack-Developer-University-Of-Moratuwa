const server  = require ("./server.js");

if(process.env.NODE_ENV === "test"){
  server.listen(3000, () => {
    console.log(
      "Capstone Project Backend is running on http://localhost:3000"
    );
  });
}else{
  server.listen(8080, () => {
    console.log(
      "Capstone Project Backend is running on http://localhost:8080"
    );
  });
}