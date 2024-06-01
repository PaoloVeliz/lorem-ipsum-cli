#!/usr/bin/env python3

import argparse
import random
import pyperclip

lorem_words = (
    "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor "
    "incididunt ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud "
    "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat duis aute irure "
    "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur "
    "excepteur sint occaecat cupidatat non proident sunt in culpa qui officia deserunt mollit "
    "anim id est laborum"
).split()

def generate_lorem_ipsum(paragraphs, words):
    text = []
    for _ in range(paragraphs):
        paragraph = ' '.join(random.choice(lorem_words) for _ in range(words))
        text.append(paragraph)
    return '\n\n'.join(text)

def main():
    parser = argparse.ArgumentParser(description="Generate Lorem Ipsum text.")
    parser.add_argument('-p', '--paragraphs', type=int, default=1, help="Number of paragraphs")
    parser.add_argument('-l', '--words', type=int, default=100, help="Number of words per paragraph")
    
    args = parser.parse_args()
    result = generate_lorem_ipsum(args.paragraphs, args.words)
    print(result)
    
    pyperclip.copy(result)
    print("\nThe text has been copied to your clipboard.")

if __name__ == "__main__":
    main()
