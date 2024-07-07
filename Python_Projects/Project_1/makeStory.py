import random


# All input answers will be here
inputs = {}

# Input asks
asks = ["Input Person Name:", "Input a Number:", "Input Verb:", "Input Noun:", "Input Adjactive(feeling):", "Input Color:", "Input Verb + ing:"]

# Asking and Storing values
while len(asks):
  ask = random.choice(asks)
  key = ask[ask.rfind(" ") + 1 : -1]
  inpt = input(ask)
  inputs[key] = inpt
  asks.remove(ask)

print(f"""The person who's name is {inputs.get('Name')} and eye's color is {inputs.get('Color')} 
feels {inputs.get('Adjactive(feeling)')} when he watch to the {inputs.get('Noun')}, 
or somebody {inputs.get('ing')} something, or when he/she {inputs.get('Verb')}, 
beacause he/she has psychological problems such as schizophrenia, 
and {inputs.get('Name')} is just {inputs.get('Number')} years old.""")
