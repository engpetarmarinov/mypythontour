from urllib.request import urlopen


def words_per_line(flo):
    return [len(line.split()) for line in flo.readlines()]


with open("wasteland.txt", mode='rt', encoding='utf-8') as real_file:
    wpl = words_per_line(real_file)
    print(type(real_file))  # <class '_io.TextIOWrapper'>
    print(wpl)  # [3, 6, 4, 5, 8]


with urlopen("http://sixty-north.com/c/t.txt") as web_file:
    wpl = words_per_line(web_file)
    print(type(web_file))  # <class 'http.client.HTTPResponse'>
    print(wpl)  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 7, 8, 14, 12, 8]
