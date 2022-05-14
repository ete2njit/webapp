import { GoogleLogin } from 'react-google-login';
import * as React from 'react';
import { Socket } from './Socket';
import '../static/googlebuttonstyle.css';

const successGoogle = (response) => {
  Socket.emit('user login', {
    type: 'Google',
    data: response,
  });
};

const failureGoogle = (response) => {
};

export function GoogleButton() {
  return (
    <GoogleLogin
      className="GLogin"
      clientId="399301149493-tr1ue5oufparksj601sc0pctkukkqr6g.apps.googleusercontent.com"
      buttonText="Login"
      onSuccess={successGoogle}
      onFailure={failureGoogle}
      cookiePolicy="single_host_origin"
    />
  );
}
