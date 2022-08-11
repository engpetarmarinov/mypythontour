def add_spam(menu=None):
    if menu is None:
        menu = []
    menu.append("spam")
    return menu


def add_spam_by_ref(menu=[]):
    menu.append("spam")
    return menu


def main():
    menu = ["eggs", "beans"]
    print(add_spam(menu))  # ['eggs', 'beans', 'spam']
    menu = ["apple", "banana"]
    print(add_spam(menu))  # ['apple', 'banana', 'spam']
    print(add_spam())  # ['spam']
    print(add_spam())  # ['spam']
    print(add_spam())  # ['spam']

    print(add_spam_by_ref())  # ['spam']
    print(add_spam_by_ref())  # ['spam', 'spam']
    print(add_spam_by_ref())  # ['spam', 'spam', 'spam']


if __name__ == '__main__':
    main()
