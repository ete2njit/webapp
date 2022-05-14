import * as React from 'react';
import { Socket } from './Socket';
import '../static/inputstyle.css';

function handleSubmit(event) {
  const newMessage = document.getElementById('message');
  Socket.emit('new message input', {
    message: newMessage.value,
  });

  newMessage.value = '';

  event.preventDefault();
}

export function Input() {
  return (
    <form onSubmit={handleSubmit}>
      <input id="message" placeholder="..." />
      <button type="button">Send</button>
    </form>
  );
}
