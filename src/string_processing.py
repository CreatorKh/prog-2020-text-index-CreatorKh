from nltk.stem.snowball import RussianStemmer
import nltk
import re

LINES_IN_ONE_PAGE = 45


def pagination(lines):
    pages = ['\n'.join(lines[line:line + LINES_IN_ONE_PAGE])
             for line in range(0, len(lines), LINES_IN_ONE_PAGE)]
    return pages


def clear_non_letters(text):
    return re.sub(r'[^а-яa-z \n]', ' ', text.lower())


def stem_string(text):
    stemmer = RussianStemmer()
    words = [stemmer.stem(word) for word in nltk.word_tokenize(text)]
    return words


def create_dict(text):
    keys = list(set(text.split()))
    return keys
