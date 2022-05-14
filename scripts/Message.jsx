import * as React from 'react';
import PropTypes from 'prop-types';
import { MessageContent } from './MessageContent';
import '../static/messagestyle.css';

export function Message({ userkey, message }) {
  let messageType = 'other';

  if (message[2] === userkey) {
    messageType = 'own';
  }

  if (message[2].endsWith('bot')) {
    messageType = 'bot';
  }

  return (
    <div className={messageType}>
      <div className="message">
        <div className="author">
          <span>
            {' '}
            <img className="profilepicture" src={message[3]} alt="" />
            { message[1] }
            :
          </span>
        </div>
        <div className="content">
          <MessageContent content={message[0]} type={message[4]} />
        </div>
      </div>
    </div>
  );
}

Message.propTypes = {
  userkey: PropTypes.string.isRequired,
  message: PropTypes.string.isRequired,
};
