import * as React from 'react';
import PropTypes from 'prop-types';
import '../static/messagecontentstyle.css';

export function MessageContent({ type, content }) {
  if (type === 'link') {
    return (
      <a href={content}>{ content }</a>
    );
  }

  if (type === 'image') {
    return (
      <img src={content} alt="" />
    );
  }

  return (
    <span>{ content }</span>
  );
}

MessageContent.propTypes = {
  type: PropTypes.string.isRequired,
  content: PropTypes.string.isRequired,
};
