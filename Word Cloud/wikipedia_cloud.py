# wikipedia_cloud.py
# This program requests a search query from the user.
# This query is then used to download the summery text of the corresponding wikipedia article.
# This summary is then used to create a word cloud, which is saved as a .png file.

# Import the necessary modules.
import wikipedia
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image


# Get the content of a wikipedia article.
def get_wiki(query):

    # Get the wikipedia page for selected title.
    page = wikipedia.page(query)

    return page.summary


# Create a word cloud for a given text in the shape of a tophat.
def create_wordcloud(text):

    # Create an array for the mask.
    mask = np.array(Image.open('./Masks/tophat.png'))

    # Create a set of stopwords that will be left out of the word cloud.
    stopwords = set(STOPWORDS)

    # Create word cloud object.
    wc = WordCloud(background_color='black', max_words=200, mask=mask, stopwords=stopwords)

    # Generate the word cloud.
    wc.generate(text)

    # Save the word cloud as a .png file.
    wc.to_file('./Output/wikipedia_cloud_output.png')


# Introduce the program to the user.
print('This program takes a search query and will make a word cloud from the summary of the wikipedia article.\n')

# Request a topic from the user to make a word cloud with. Note: the user will get an error when there are more than 1 possible pages.
topic = input('Please enter the topic for the word cloud: ')

# Create the word cloud with the given input.
create_wordcloud(get_wiki(topic))

# Print a message to the user to indicate that the word cloud is finished and where the output can be found.
print('\nThe word cloud is succesfully created. You can find the word cloud in the output folder.')
