import os
import json
import difflib
from tkinter import *
import pyttsx3
from playsound import playsound
from difflib import get_close_matches

engine =pyttsx3.init()
engine.setProperty('rate',125)

data =json.load(open("C:/Users/HP800g1/PycharmProjects/TalkingDictionary/data.json"))
c1='y'

def extract(word):
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys())) > 0:
        choice =input("Did You Mean : "+word+"\n\n Enter Choice 'y' if Yes and 'n' if No")
        return data[get_close_matches(word, data.keys())[0]]
    else:
        print("This word doesn't exist")
        engine.say("Opps, The word doesn't exist")
        engine.runAndWait()
        engine.stop()


while True:
    engine.say("Enter The Word You Want To Search Sir :")
    engine.runAndWait()

    to_search =input("Enter The Word You Want To Search Sir").lower()
    result=""
    result=extract(to_search)
    if result==None:
        c=input("Do You Want To Continue The Search (y/n)")
        if c=="y":
            pass
        else:
            exit()

    else:
        engine.say(result)
        engine.runAndWait()
        engine.stop()
        ch1 = input("Do You Want To Continue The Search (y/n)")
        if ch1 == "y":
            pass
        else:
            exit()