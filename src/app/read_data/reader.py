import re

from constants.path_constants import DATA_PATH

clean_re = re.compile('\\W+')


def _clean_text(text):
    return clean_re.sub(' ', text)


def get_words_list(file_name):
    file = open(DATA_PATH + file_name, 'r', encoding='utf-8')
    text = file.read()
    file.close()

    text_in_lower = text.lower()
    cleaned_text = _clean_text(text_in_lower)
    return cleaned_text.split()
