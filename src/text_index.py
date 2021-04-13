from collections import Counter
from string_processing import *
from system import *
from argparsing import *

PAGE_SEPARATOR = '_' * 50 + '\n'


def process_text(filename):
    input_text = read_file(filename, dir='texts')
    text = clear_non_letters(input_text)
    lines = re.split(r'\n+', text)
    stemmed_lines = [' '.join(stem_string(line)) for line in lines]
    stemmed_pages = pagination(stemmed_lines)
    save_file(filename, f'\n{PAGE_SEPARATOR}'.join(stemmed_pages), dir='data')


def most_common_words(words_dict):
    return sorted(Counter(words_dict).items(), key=lambda a: a[1], reverse=True)


def load_info(data_filename):
    text = read_file(data_filename)
    text_raw = clear_non_letters(read_file(data_filename, dir='texts')).split('\n')
    text_raw_pages = pagination(text_raw)
    return text, text.split(f'{PAGE_SEPARATOR}'), text_raw_pages


def get_top_words(filename, count):
    input_text = read_file(filename, dir='data')
    top_words = most_common_words(input_text.split())
    print(f"Топ {count} популярных слов:")
    for word in top_words[:count]:
        print(f'"{word[0]}" - {word[1]} вхождений!')


def analys_word_in_text(filename, word):
    stemm = stem_string(word)[0]
    text, pages, pages_raw = load_info(filename)
    index_pages = []
    #forms = []
    for index in range(len(pages)):
        if stemm in pages[index]:
            index_pages.append(index + 1)
            index_word = pages[index].find(stemm)
            #forms.append(pages_raw[index][index_word:index_word+10])
    print(f'''Слово "{args['word']}" встречается на страницах:''')
    print(*index_pages, sep=', ')
    print(f'Всего вхождений: {text.count(stemm)}')
    #print(forms)
    #print(*stem_string(' '.join(forms)))

if __name__ == '__main__':
    nltk.download('punkt')
    args = get_parse_arguments()

    filename = args['filename']

    if args['process']:
        process_text(filename)

    if args['top']:
        get_top_words(filename, args['value'])

    if args['word'] != '':
        analys_word_in_text(filename, args['word'])

    if args['group']:
        print("ToDo")
