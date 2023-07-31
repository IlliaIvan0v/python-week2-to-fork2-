from random import choice
attepts = 6

words = [
    "computer",
    "python",
    "programming",
    "keyboard",
    "mouse",
    "monitor",
    "internet",
    "website",
    "software",
    "hardware",
    "algorithm",
    "function",
    "variable",
    "statement",
    "database",
    "framework",
    "directory",
    "document",
    "directory",
    "package",
    "console",
    "terminal",
    "compiler",
    "debugging",
    "graphics",
    "encryption",
    "password",
    "security",
    "firewall",
    "protocol",
    "router",
    "server",
    "client",
    "virtual",
    "memory",
    "download",
    "upload",
    "storage",
    "algorithm",
    "interface",
    "operating",
    "system",
    "arithmetic",
    "operation",
    "accessible",
    "keyboard",
    "character",
    "programmer",
    "database",
    "operator",
    "function",
    "variable",
    "statement",
    "debugger",
    "framework",
    "directory",
    "algorithm",
    "graphics",
    "password",
    "security",
    "firewall",
    "protocol",
    "compiler",
    "execution",
    "loop",
    "condition",
    "machine",
    "language",
    "syntax",
    "semantic",
    "debugging",
    "graphics",
    "encryption",
    "software",
    "hardware",
    "program",
    "interface",
    "internet",
    "website",
    "package",
    "console",
    "terminal",
    "debugger",
    "framework",
    "algorithm",
    "keyboard",
    "variable",
    "document",
    "directory",
    "package",
    "console",
    "terminal",
    "compiler",
    "graphics",
    "encryption",
    "firewall",
    "protocol",
    "server",
    "database",
    "maxrosoft",
]
Random_Word = choice(words)
Word = "_" * len(Random_Word)
Used_Words = []

while attepts != 0 and Word != Random_Word:
    print("\nYou used this letter:\n", Used_Words)
    print("\nHidden word:", Word)
    print(f"you have {attepts} tries")

    assumption = input("Enter the letter: ").lower()

    while assumption in Used_Words:
        print(f"\nYou are already guess word,  {assumption}")
        assumption = input("Choose another letter: ").lower()

    Used_Words.append(assumption)

    if assumption in Random_Word:
        print(f"\nYes, letter '{assumption}' is in the word")

        new = ""
        for i in range(len(Random_Word)):
            if assumption == Random_Word[i]:
                new += assumption
            else:
                new += Word[i]
        Word = new
    else:
        print(f"\nNo, letter '{assumption}' isn`t in word")
        attepts -= 1
if attepts == 0:
    print("\nYou have not more attepts")
    print("Game is over!\nyou lost")
    print("Word was:", Random_Word)
else:
    print("\nYou guessed the word", Random_Word)
    print("You won game")
