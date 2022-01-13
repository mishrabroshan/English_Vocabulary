# imports
import json  # for json operations
import pickle  # for store and retrieve data on disk
import random  # from generating random number

from plyer import notification  # for displaying notification
from pathlib import Path  # for p operations

# getting current path of program
p = __file__
p = str(p)
p = p.replace("/main.py", "")
print(p)

# restoring random state
rF = open(p + "/random", "rb")
rState = pickle.load(rF) 
random.setstate(rState)

# opening file in read mode to get words
f = open(p + "/words.json", "r")

# loading json from file
vocabulary_words = json.load(f)["data"]
lenght = len(vocabulary_words)

# getting random word from json to display
index = random.randint(0, lenght)
word = vocabulary_words[index]

# displaying system pop-up
notification.notify(
    app_name="English Vocabulary",
    title="Word : " + word["name"],
    message="Meaning : " + word["detail"])

# saving random state
rF = open(p + "/random", "wb")
rState = random.getstate()
pickle.dump(rState, rF)
