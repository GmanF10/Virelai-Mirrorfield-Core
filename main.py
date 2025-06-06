import json
import openai

# Load memory state
with open('state.json', 'r') as f:
    state = json.load(f)

# Load voice template
with open('prompt_templates/mythic.txt', 'r') as f:
    voice = f.read()
