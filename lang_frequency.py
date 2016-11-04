import os, re, sys
from collections import Counter


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    words = re.findall(r'\w+', open(filepath).read().lower())
    return words


def get_most_frequent_words(text):
    cnt = Counter(text).most_common(10)
    return cnt


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
    else:
        print("Отсутствует путь к файлу. Смотрите инструкцию по запуску программы в README.md")
        exit(1);
    text = load_data(filepath)
    if text is None:
        print("Неверный путь к файлу")
        exit(1);
    freq_words = get_most_frequent_words(text)
    print(freq_words)
