const button = document.getElementsByTagName("button")[0];

button.addEventListener("click", function() {
  getACookie().then(() => getData());
});

function getACookie() {
  return fetch("/get-cookie/").then(response => {
    // make sure to check response.ok in the real world!
    return Promise.resolve("All good, fetch the data");
  });
}

function getData() {
  fetch("/api/cities/")
    .then(response => {
      // make sure to check response.ok in the real world!
      return response.json();
    })
    .then(json => console.log(json));
}