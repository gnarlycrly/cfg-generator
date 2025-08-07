# CFG Generator

A simple context-free grammar (CFG) based sentence generator written in Python.

This script generates random sentences based on a predefined grammar by recursively replacing non-terminal symbols.

## Features

- Define your own context-free grammar using a Python dictionary
- Generates varied, grammatically structured sentences
- Minimal and easy to modify

## Example Output
Once upon a time, a dragon fought a monster.
Once upon a time, a robot built a spaceship.
Once upon a time, a pirate saved the kingdom.

## How It Works

1. The grammar is defined as a dictionary, where:
   - Keys are non-terminal symbols (e.g., `CHARACTER`, `ACTION`)
   - Values are lists of possible expansions for those symbols

2. The script starts with the start symbol (`S`).

3. It randomly selects and replaces any non-terminal symbols in angle brackets (`<...>`) with one of their corresponding expansions.

4. This process continues until no non-terminals remain in the sentence.


## Customizing the Grammar
You can edit the grammar dictionary inside cfg_generator.py to use different sentence structures and vocabulary.

Example:
 ```bash
grammar = {
    "S": ["<GREETING>, <CHARACTER>!"],
    "GREETING": ["Hello", "Greetings", "Hey"],
    "CHARACTER": ["traveler", "wizard", "friend"]
}
