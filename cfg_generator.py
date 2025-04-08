import random
import re

# Define your CFG as a dictionary
grammar = {
    "S": ["Once upon a time, <CHARACTER> <ACTION>."],
    "CHARACTER": ["a dragon", "a princess", "a robot", "a pirate"],
    "ACTION": ["found a treasure", "fought a monster", "built a spaceship", "saved the kingdom"]
}

def generate(symbol="S"):
    sentence = random.choice(grammar[symbol])
    while re.search(r"<[^<>]+>", sentence):
        sentence = re.sub(r"<([^<>]+)>", lambda m: random.choice(grammar[m.group(1)]), sentence, count=1)
    return sentence

# Example run
print(generate())
