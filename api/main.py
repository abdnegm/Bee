from fastapi import FastAPI

import os
import pickle
import random

##########
# Startup
##########

def unpickle(file_name):
    with open(file_name, 'rb') as f:
        unpickled = pickle.load(f)
    return unpickled

# level_one_words
level_one_words = list(filter(lambda s: s.endswith(".pickle"), os.listdir("easy")))

# level_two_words
level_two_words = list(filter(lambda s: s.endswith(".pickle"), os.listdir("medium")))

# level_three_words
level_three_words = list(filter(lambda s: s.endswith(".pickle"), os.listdir("hard")))

##########
# FastAPI
##########

app = FastAPI(
    root_path="/bee/api" # comment out when testing on localhost
)

@app.get("/dict/easy")
def easy_words():
    return unpickle("easy/" + random.choice(level_one_words))

@app.get("/dict/medium")
def medium_words():
    return unpickle("medium/" + random.choice(level_two_words))

@app.get("/dict/hard")
def hard_words():
    return unpickle("hard/" + random.choice(level_three_words))
