import difflib
import random
import time
import webbrowser
from tkinter import *
from datetime import datetime
from googlesearch import search

websites = {
    "gpt": "chat.openai.com",
    "spotify": "www.spotify.com",
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "facebook": "https://www.facebook.com",
    "amazon": "https://www.amazon.in",
    "flipkart": "https://www.flipkart.com",
    "yahoo": "https://www.yahoo.com",
    "wikipedia": "https://www.wikipedia.org",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "twitter": "https://www.twitter.com",
    "snapdeal": "https://www.snapdeal.com",
    "paytm": "https://www.paytm.com",
    "indiatimes": "https://www.indiatimes.com",
    "hdfcbank": "https://www.hdfcbank.com",
    "icicibank": "https://www.icicibank.com",
    "statebankofindia": "https://www.sbi.co.in",
    "ndtv": "https://www.ndtv.com",
    "cricbuzz": "https://www.cricbuzz.com",
    "rediff": "https://www.rediff.com",
    "irctc": "https://www.irctc.co.in",
    "quora": "https://www.quora.com",
    "moneycontrol": "https://www.moneycontrol.com",
    "ebay": "https://www.ebay.in",
    "airtel": "https://www.airtel.in",
    "jio": "https://www.jio.com",
    "zomato": "https://www.zomato.com",
    "bookmyshow": "https://www.bookmyshow.com",
    "olx": "https://www.olx.in",
    "makemytrip": "https://www.makemytrip.com",
    "bigbasket": "https://www.bigbasket.com",
    "swiggy": "https://www.swiggy.com",
    "cricinfo": "https://www.espncricinfo.com",
    "hotstar": "https://www.hotstar.com",
    "indiamart": "https://www.indiamart.com",
    "oyo": "https://www.oyorooms.com",
    "justdial": "https://www.justdial.com",
    "snapchat": "https://www.snapchat.com",
    "dailymotion": "https://www.dailymotion.com",
    "myntra": "https://www.myntra.com",
    "naukri": "https://www.naukri.com",
    "timesofindia": "https://www.timesofindia.indiatimes.com",
    "inshorts": "https://www.inshorts.com",
    "bankbazaar": "https://www.bankbazaar.com",
    "jabong": "https://www.jabong.com",
    "croma": "https://www.croma.com",
    "medlife": "https://www.medlife.com",
    "gaana": "https://www.gaana.com",
    "policybazaar": "https://www.policybazaar.com",
    "freshersworld": "https://www.freshersworld.com",
    "urbanclap": "https://www.urbanclap.com",
    "reddit": "https://www.reddit.com",
    "pintrest":"https://www.pintrest.com"
}
    
class Responses:
    def __init__(self):
        pass
    
    responses = {
    "hi": ["Hi there!", "Hello!", "Hey!", "Greetings!", "Hi, how can I assist you?"],
    "hello": ["Hi there!", "Hello!", "Hey!", "Greetings!", "Hi, how can I assist you?"],
    "hey": ["Hi there!", "Hello!", "Hey!", "Greetings!", "Hi, how can I assist you?"],
    "greetings": ["Hi there!", "Hello!", "Hey!", "Greetings!", "Hi, how can I assist you?"],
    "how are you": ["I'm an AI, so I don't have feelings, but thank you for asking!",
                    "I'm here to help, how can I assist you?"],
    "who are you": ["I am Assistant AI developed by Aditya Jain.",
                    "I'm an AI designed to assist with information and tasks.",
                    "I'm your friendly neighborhood Assistant AI! How can I assist you?"],
    "tell me a joke": [
        "Why don't scientists trust atoms?\nBecause they make up everything!",
        "Knock-Knock! Who's There\nCowsays! Cowsays who?\nNo, Cowsays MOOOO!",
        "What's the best time to go to the dentist?\nTooth-hurty!",
        "Why did the tomato turn red?\nBecause it saw the salad dressing!"
    ],
    "thank you": ["You're welcome!", "No problem!", "Glad to help!", "Anytime!",
                  "You're welcome.\nHave a great day!"],
    "goodbye": ["Goodbye!", "Farewell!", "Take care!", "Until next time!",
                "Goodbye.\nHave a wonderful day!"],
    "what's your favorite color": [
        "I don't have a favorite color since I'm an AI, but I can appreciate all colors!",
        "I don't experience color the same way humans do,\nso I don't have a favorite."
    ],
    "tell me a fun fact": [
        "Did you know that honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible!",
        "A group of flamingos is called a flamboyance.",
        "The shortest war in history lasted only 38 to 45 minutes!\nIt was the Anglo-Zanzibar War fought between the United Kingdom and the Sultanate of Zanzibar on August 27, 1896.",
        "There are more possible iterations of a game of chess than there are atoms in the known universe.",
        "The average person walks the equivalent of three times around the world in a lifetime.",
        "The human brain is the most energy-consuming organ in the body, using up to 20 percent of the body's total energy."
    ],
    "tell me a riddle": [
        "I have cities, but no houses. I have mountains, but no trees.\nI have water, but no fish. What am I? (answer: a map)",
        "I speak without a mouth and hear without ears.\nI have no body, but I come alive with wind. What am I? (answer: an echo)",
        "The more you take, the more you leave behind.\nWhat am I? (answer: footsteps)",
        "I have keys, but no locks. I have space, but no room.\nYou can enter, but you can't go outside. What am I? (answer: a keyboard)",
        "I have cities but no houses. I have forests but no trees.\nI have rivers but no water. What am I? (answer: a map)",
        "I have no life, but I can die.\nI can't breathe, but I need air to survive. What am I? (answer: fire)",
        "What can you break,\neven if you never pick it up or touch it? (answer: a promise)",
        "I can be cracked, made, told,\nand played. What am I? (answer: a joke)",
        "I am taken from a mine and shut in a wooden case,\nfrom which I am never released,\nand yet I am used by almost every person. What am I? (answer: pencil lead)",
        "I am always hungry, I must always be fed,\nThe finger I touch will soon turn red.\nWhat am I? (answer: a fire)"
    ],
    "who is your father": "I don't have one.",
    "who is your mother": "I don't have one.",
    "who are your parents": "I don't have parents.",
    "do you eat food": "I can't physically eat or drink.",
    "can you eat food": "I can't physically eat or drink.",
    "can you drink water": "I can't physically eat or drink.",
    "do you have a favorite drink": "I can't physically eat or drink.",
    "do you know about funny numbers": "69420",
    "what can you do": "I am here to help.",
    "you are not funny": "I'm sorry, but as an AI, I can't understand humor.",
    "can you code": "I can't code.",
    "what's the meaning of life": "The meaning of life is a philosophical question and varies\ndepending on individual beliefs and perspectives.",
    "what's the weather like": "I'm sorry, I don't have access to real-time weather information.",
    "tell me a quote": [
        "The only way to do great work is to love what you do\n- Steve Jobs",
        "In the end, it's not the years in your life that count, it's the life in your years\n- Abraham Lincoln",
        "Success is not final, failure is not fatal. It is the courage to continue that counts\n- Winston Churchill",
        "The future belongs to those who believe in the beauty of their dreams\n- Eleanor Roosevelt",
        "The best way to predict the future is to create it\n- Peter Drucker",

    ]
}



    def get_best_match(self,user_input, choices):
        # Find the best match using difflib's get_close_matches
        matches = difflib.get_close_matches(user_input, choices)
        if matches:
            return matches[0]  # Return the best match
        else:
            return None
    def get_response(self,user_input):
        # Check if the user input is in the given dictionary
        if user_input in self.responses:
            return random.choice(self.responses[user_input])
        else:
            best_match=self.get_best_match(self=self,user_input=user_input, choices=self.responses.keys())
            if best_match:
                return random.choice(self.responses[best_match])
            else:
                raise ValueError
            

