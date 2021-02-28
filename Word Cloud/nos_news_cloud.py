from wordcloud import WordCloud
import numpy as np
from PIL import Image
import feedparser


def create_stopwords():
    file = open('./Resources/stopwoorden.txt')

    stopwords_list = []

    for line in file:
        stopwords_list.append(line[:-1])

    return stopwords_list


def get_feed():

    d = feedparser.parse('http://feeds.nos.nl/nosnieuwsalgemeen')

    title_string = ''

    for post in d.entries:
        print(post.title)
        title_string += (post.title + ' ')

    return title_string


def remove_special_char(text):

    new_text = ''

    for char in text:
        if char not in ".,?!@#^&*()_=+[]:;'/":
            new_text = new_text + char

    return new_text


def create_wordcloud(text):

    # Create an array for the mask.
    mask = np.array(Image.open('./Masks/banana.png'))

    # Create a set of stopwords that will be left out of the word cloud.
    stopwords = set(create_stopwords())

    # Create word cloud object
    wc = WordCloud(background_color='black', max_words=200, mask=mask, stopwords=stopwords)

    # Generate the word cloud.
    wc.generate(text)

    # Save the word cloud as a .png file.
    wc.to_file('./Output/nos_news_cloud_output.png')


create_wordcloud(remove_special_char(get_feed()))
