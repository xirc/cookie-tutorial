const button = document.getElementsByTagName("button")[0];

button.addEventListener("click", function() {
  getACookie().then(() => getData());
});

function getACookie() {
  return fetch("http://localhost:5000/get-cookie/", {
    credentials: "include"
  }).then(response => {
    // make sure to check response.ok in the real world!
    return Promise.resolve("All good, fetch the data");
  });
}

function getData() {
  fetch("http://localhost:5000/api/cities/", {
    credentials: "include"
  })
    .then(response => {
      // make sure to check response.ok in the real world!
      return response.json();
    })
    .then(json => console.log(json));
}