#!/usr/bin/node
const btn = document.querySelector('#add_item');
const list = document.querySelector('.my_list');

btn.addEventListener('click', () => {
  const li = document.createElement('li');
  li.textContent = 'Item';
  list.appendChild(li);
});
