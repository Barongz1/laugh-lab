"""One-Liner Laugh Lab — entry for make.fun.

Writes one line to /output/entry.txt.
The line is a short funny line answering a prompt, at most 200 characters.
"""
import os

LINE = "I didn't eat your sock. I was just giving it a tour of the inside of my dustbin, and it decided to stay."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")

if __name__ == "__main__":
    main()
