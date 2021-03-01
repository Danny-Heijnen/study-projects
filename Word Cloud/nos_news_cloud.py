# nos_news_cloud.py
# This program downloads the 20 most recent news articles from the Dutch NOS news website RSS feed.
# These headlines are then used to create a word cloud and save it as a .png file.

# Import the necessary modules.
from wordcloud import WordCloud
import numpy as np
from PIL import Image
import feedparser


# This function creates a list with common words like prepositions, pronouns and auxilary verbs.
# These words will be left out of the word cloud to increase the information density.
def create_stopwords():
    file = open('./Resources/stopwoorden.txt')

    stopwords_list = []

    for line in file:
        stopwords_list.append(line[:-1])

    return stopwords_list


# This function reads the RSS feed from the Dutch news website NOS.nl and creates a string out of it.
def get_feed():

    d = feedparser.parse('http://feeds.nos.nl/nosnieuwsalgemeen')

    title_string = ''

    print('The most recent headlines of the Dutch NOS news are:\n')

    for post in d.entries:
        print(post.title)
        title_string += (post.title + ' ')

    return title_string


# This function goes through a string character by character and removes different punctuation marks and other special characters.
# The function then returns the changed list.
def remove_special_char(text):

    new_text = ''

    for char in text:
        if char not in ".,?!@#^&*()_=+[]:;'/":
            new_text = new_text + char

    return new_text


# This function creates a word cloud from a given text.
def create_wordcloud(text):

    # Create an array for the mask.
    mask = np.array(Image.open('./Masks/banana.png'))

    # Create a set of stopwords that will be left out of the word cloud.
    stopwords = set(create_stopwords())

    # Create word cloud object.
    wc = WordCloud(background_color='black', max_words=200, mask=mask, stopwords=stopwords)

    # Generate the word cloud.
    wc.generate(text)

    # Save the word cloud as a .png file.
    wc.to_file('./Output/nos_news_cloud_output.png')


# Create the word cloud by getting the headlines from the RSS feed, removing the special characters and saving the word cloud in a .png file.
create_wordcloud(remove_special_char(get_feed()))

# Print a message to the user to indicate that the word cloud is finished and where the output can be found.
print('\nThe word cloud is succesfully created. You can find the word cloud in the output folder.')
