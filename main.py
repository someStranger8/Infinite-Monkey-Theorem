
# imports
import json
import random
import time


# calc probability of getting string correct
def calc_prob(strlen, charlen):
    return strlen * charlen


# guess the string
def guess(strlen, chars):
    out = ""

    for i in range(strlen):
        out += random.choice(chars)

    return out

# main func
def main():
    # read config file
    with open("config.json", "r") as f:
        data = json.loads(f.read())

    prob = calc_prob(len(data["string"]), len(data["chars"]))
    
    print(f"String to guess: {data["string"]}")
    print(f"Probability of guess: 1/{prob} or {(1/prob)*100}%")

    time.sleep(5)

    guesses = 0
    string = ""

    while string != data["string"]:
        string = guess(len(data["string"]), data["chars"])
        print(string)
        guesses += 1

    print("Got it!")
    print(f"Only took {guesses} guesses")


# exec main if running main.py
if __name__ == "__main__":
    main()
