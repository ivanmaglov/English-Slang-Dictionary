import json

def create_json_file():
    person_dict = {
        "the 5-0": ["police"],
        "no biggie": ["no problem"],
        "c-note": ["100$"],
        "dork": ["geek", 'nerd'],
        "goat": ["greatest of all time"],
        "herb": ["weed"],
        "in the zone ": ["to be really focus on something"],
        "mumbo jumbo": ["nonsense", "hard to understand"],
        "mary jane": ["weed", "marihuana "],
        "your john hancock": ["your signature"],
        "intel": ["information", "news"],
        "hit on someone": ["to flirt with  someone"],
        "gizmo": ["gadget"],
        "freebie": ["something you get for free"],
        "your digits": ["phone number"],
        "clapback": ["to return an insult"],
        "booze": ["alcohol"],
        "awesome sauce": ["super", "awesome", "the best"],
        "baby bump": ["Baby bump is the rounded\nbelly that shows when someone\n is pregnant."],
        "grub": ["food"],
    }

    with open('slang.json', 'w') as json_file:
        json.dump(person_dict, json_file)

#17

