// Select the div with id 'red_header' and add click event listener
document.querySelector('#red_header').addEventListener('click', function () {
  // When clicked, add the 'red' class to the header element
  document.querySelector('header').classList.add('red');
});
