import * as React from 'react';
import PropTypes from 'prop-types';
import { Input } from './Input';
import { Message } from './Message';
import { Socket } from './Socket';
import '../static/chatstyle.css';

export function Chat({ username, userkey, displayCount }) {
  const [chatlog, setChatlog] = React.useState([]);
  let chat = [];

  function getAllMessages() {
    React.useEffect(() => {
      Socket.on('send all messages', (data) => {
        setChatlog((chatlog) => data.allMessages);
      });
    }, []);
  }

  function getOneMessage() {
    React.useEffect(() => {
      Socket.on('send one message', (data) => {
        setChatlog((chatlog) => [...chatlog, data.message]);
      });
    }, []);
  }

  if (displayCount === 0) chat = chatlog;
  else {
    for (let i = 0; i < chatlog.length && (displayCount === 0 || i < displayCount); i += 1) {
      chat[displayCount - i] = chatlog[chatlog.length - 1 - i];
    }
  }

  getOneMessage();
  getAllMessages();

  return (
    <div className="chat-window">
      <div className="chat-box">
        {chat.map((message) => (
          <Message className="message" key={message.id} message={message} username={username} userkey={userkey} />))}
      </div>
      <div className="input-box">
        <Input />
      </div>
    </div>
  );
}

Chat.propTypes = {
  username: PropTypes.string.isRequired,
  userkey: PropTypes.string.isRequired,
  displayCount: PropTypes.number.isRequired,
};
