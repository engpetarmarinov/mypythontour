#!/usr/bin/env python3
""" Retrieves and print words from a URL

Usage:

    python3 words.py <URL>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """ Fetches words from URL

    param url: the URL that we want to fetch
    return: List of words
    """
    story = urlopen(url)
    story_words = []

    for line in story:
        line_words = line.decode("utf-8").split()
        for word in line_words:
            story_words.append(word)

    story.close()

    return story_words


def print_items(story_words):
    for word in story_words:
        print(word)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.argv.append("http://sixty-north.com/c/t.txt")
    main(sys.argv[1])  # sys.argv[0]) is the program name
