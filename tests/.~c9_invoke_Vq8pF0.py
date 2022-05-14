import unittest
from dotenv import load_dotenv
import os
import datetime
from os.path import join, dirname
import sys

sys.path.append(join(dirname(__file__), "../chat-app/"))

from chatbot import Chatbot

KEY_INPUT = "input"
KEY_EXPECTED = "expected"


class ChatAppTestCase(unittest.TestCase):
    def setUp(self):
        self.is_command_test_params = [
            {
                KEY_INPUT: "!! about",
                KEY_EXPECTED: True,
            },
            {
                KEY_INPUT: "help",
                KEY_EXPECTED: False,
            },
            {
                KEY_INPUT: "!!about",
                KEY_EXPECTED: True,
            }
        ]

        self.bot_response_test_params = [
            {
                KEY_INPUT: "!! about",
                KEY_EXPECTED: "Go no further, you must. Found Master Yoda, you have.",
            },
            {
                KEY_INPUT: "!! help",
                KEY_EXPECTED: "Type '!! about' for info about me! Type '!! funtranslate <message>' and I will translate your message. " +
                                "Type '!! randcase <message>' and I'll return your message with random capitalization. " +
                                "Type '!! funtranslate <message>' and Master Yoda will have a look at your message and rephrase it for you. " +
                                "Type '!! joke' and I will tell you a programming joke! We all love those! Right?",
            },
            {
                KEY_INPUT: "!! milk from Ahch-To",
                KEY_EXPECTED: "A recognized command, 'milk' is not. Type !! help for info about recognized commands",
            }
        ]

    
    def test_chatbot(self):
        bot = Chatbot()
        
        for test_case in self.is_command_test_params:
            bot_response = bot.is_command(test_case[KEY_INPUT])
    
            expected = test_case[KEY_EXPECTED]
            
            self.assertEqual(bot_response, expected)
            
        for test_case in self.bot_response_test_params:
            bot_response = bot.process(test_case[KEY_INPUT])
                
            expected = test_case[KEY_EXPECTED]
            
            self.assertEqual(bot_response, expected)
            
            
if __name__ == '__main__':
    unittest.main()
