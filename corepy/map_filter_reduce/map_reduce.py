from functools import reduce


def count_words(doc: dict) -> dict:
    normalised_doc = "".join(c.lower() if c.isalpha() else " " for c in doc)
    frequencies = {}
    for word in normalised_doc.split():
        frequencies[word] = frequencies.get(word, 0) + 1
    return frequencies


def combine_counts(d1: dict, d2: dict) -> dict:
    d = d1.copy()
    for word, count in d2.items():
        d[word] = d.get(word, 0) + count
    return d


def main():
    print(count_words('It was the best of times, it was the worst of times.'))
    # {'it': 2, 'was': 2, 'the': 2, 'best': 1, 'of': 2, 'times': 2, 'worst': 1}

    documents = [
        'It was the best of times, it was the worst of times.',
        'I went to the woods because I wished to live deliberately, to find only the essential facts of life...',
        'Friends, Romans, countrymen, lend me your ears; I come to bury Caesar, not to praise him.',
        'I do not like green eggs and ham. I do not like them, Sam-I-Am.',
    ]

    counts = map(count_words, documents)
    total_counts = reduce(combine_counts, counts)
    print(total_counts)
    # {'it': 2, 'was': 2, 'the': 4, 'best': 1, 'of': 3, 'times': 2, 'worst': 1, 'i': 6, 'went': 1, 'to': 5, 'woods': 1, 'because': 1, 'wished': 1, 'live': 1, 'deliberately': 1, 'find': 1, 'only': 1, 'essential': 1, 'facts': 1, 'life': 1, 'friends': 1, 'romans': 1, 'countrymen': 1, 'lend': 1, 'me': 1, 'your': 1, 'ears': 1, 'come': 1, 'bury': 1, 'caesar': 1, 'not': 3, 'praise': 1, 'him': 1, 'do': 2, 'like': 2, 'green': 1, 'eggs': 1, 'and': 1, 'ham': 1, 'them': 1, 'sam': 1, 'am': 1}


if __name__ == '__main__':
    main()
