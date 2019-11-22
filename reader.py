import re

clean_re = re.compile('\\W+')


def clean_text(text):
    return clean_re.sub(' ', text)


def get_word_list(file_name):
    file = open(file_name, 'r')
    text = file.read()
    file.close()

    text_in_lower = text.lower()
    cleaned_text = clean_text(text_in_lower)
    return cleaned_text.split()
