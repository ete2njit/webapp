import unittest
import unittest.mock as mock
from dotenv import load_dotenv
import os
import datetime
from os.path import join, dirname
import sys
import json
from requests.models import Response

import flask_socketio

sys.path.append(join(dirname(__file__), "../chat-app/"))

from chatbot import Chatbot
from models import Message
import app

KEY_INPUT = "input"
KEY_EXPECTED = "expected"


class ChatAppTestCase(unittest.TestCase):
    def setUp(self):
        self.chatbot_funtranslate_test = [
            {
                KEY_INPUT: "Sentence to translate",
                KEY_EXPECTED: "Sentence to translate",
            },
        ]
        
        self.chatbot_joke_test = [
            {
                KEY_INPUT: "",
                KEY_EXPECTED: "this is a joke",
            }
        ]
        self.chatbot_randcase_test = [
            {
                KEY_INPUT: "Sentence to randcase",
                KEY_EXPECTED: "sentence to randcase",
            }
        ]
        self.chatbot_translate_from_process_test = [
            {
                KEY_INPUT: "!! funtranslate sentence to translate",
                KEY_EXPECTED: "sentence to translate",
            }
        ]
        self.create_message_test = [
            {
                KEY_INPUT: 
                    {
                        "username": "user", 
                        "userimage": "image",
                        "userkey": "key",
                        "message": "message",
                    }
            }
        ]

       
    
    def mocked_funtranslate_get(self, sentence):
        response = mock.Mock(spec=Response)
        response.json.return_value = { "contents": {"translated": sentence[57:]}}
        return response
    
    def mocked_joke_get(self, url):
        response = mock.Mock(spec=Response)
        response.json.return_value = [{ "setup": "this is",  "punchline": "a joke"}]
        return response
    
    def mocked_random_choice(self, values):
        return values[1]
        
    def mocked_socketio_emit(self, channel, data, requestid):
        print(channel)
        return
    
    
    def test_chatbot(self):
        bot = Chatbot()
        
        for test_case in self.chatbot_funtranslate_test:
            with mock.patch('requests.get', self.mocked_funtranslate_get):
                bot_response = bot.translate(test_case[KEY_INPUT])
                
                self.assertEqual(test_case[KEY_EXPECTED], bot_response)
                
        for test_case in self.chatbot_joke_test:
            with mock.patch('requests.get', self.mocked_joke_get):
                bot_response = bot.joke()
                
                self.assertEqual(test_case[KEY_EXPECTED], bot_response)
        
        for test_case in self.chatbot_randcase_test:
            with mock.patch('chatbot.choice', self.mocked_random_choice):
                bot_response = bot.randcase(test_case[KEY_INPUT])
                
                self.assertEqual(test_case[KEY_EXPECTED], bot_response)
            
        for test_case in self.chatbot_translate_from_process_test:
            with mock.patch('requests.get', self.mocked_funtranslate_get):
                bot_response = bot.process(test_case[KEY_INPUT])
                
                self.assertEqual(test_case[KEY_EXPECTED], bot_response)
            
        for test_case in self.create_message_test:
            model = Message(test_case[KEY_INPUT]['username'], test_case[KEY_INPUT]['userimage'], test_case[KEY_INPUT]['userkey'], test_case[KEY_INPUT]['message'])
        

            
if __name__ == '__main__':
    unittest.main()
