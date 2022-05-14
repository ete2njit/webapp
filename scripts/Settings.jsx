import * as React from 'react';
import PropTypes from 'prop-types';
import '../static/settingstyle.css';

export function Settings({ displayCount, handleChange }) {
  return (
    <div className="settings-window">
      <div className="settings-content">
        <span className="display-count">Chat length:  </span>
        <input
          className="display-input"
          type="text"
          value={displayCount}
          onChange={handleChange}
        />
      </div>
    </div>
  );
}

Settings.propTypes = {
  displayCount: PropTypes.number.isRequired,
  handleChange: PropTypes.func.isRequired,
};
