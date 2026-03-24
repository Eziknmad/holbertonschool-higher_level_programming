#!/usr/bin/node
const header = document.querySelector('header');
const btn = document.querySelector('#update_header');

btn.addEventListener('click', () => {
  header.textContent = 'New Header!!!';
});
