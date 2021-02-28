from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import feedparser
import re


def get_feed():

    d = feedparser.parse('http://feeds.nos.nl/nosnieuwsalgemeen')

    title_string = ''

    for post in d.entries:
        title_string += (post.title.lower() + ' ')

    return title_string


def remove_special_char(text):

    new_text = ''

    for char in text:
        if char not in ".,?!@#^&*()-_=+[]:;'/":
            new_text = new_text.join(char)
            print(new_text)

    return new_text


print(remove_special_char("test!@#"))
