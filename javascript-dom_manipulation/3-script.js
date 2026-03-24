// Select the div with id 'toggle_header' and add click event listener
document.querySelector('#toggle_header').addEventListener('click', function () {
  // Select the header element
  const header = document.querySelector('header');
  // Toggle between 'red' and 'green' classes
  header.classList.toggle('red');
  header.classList.toggle('green');
});
