'use strict';

function gameOver() {
  const popup = document.createElement('div');
  popup.setAttribute('id', 'gameover');
  popup.innerHTML = 'Game Over';

  document.body.appendChild(popup);
}
