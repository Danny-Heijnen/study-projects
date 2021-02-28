import wikipedia
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image


# TODO: waarom werkt het selecteren van het eerste zoekresultaat (title) niet? met .page(query) werkt het wel.
# Get the content of a wikipedia article.
def get_wiki(query):

    # Store the first suggested page as the title.
    title = wikipedia.search(query, results=1)[0]
    print(title)

    # Get the wikipedia page for selected title.
    page = wikipedia.page(query)

    return page.content


# Create a word cloud for a given text in the shape of a tophat.
def create_wordcloud(text):

    # Create an array for the mask.
    mask = np.array(Image.open('tophat.png'))

    # Create a set of stopwords that will be left out of the word cloud.
    stopwords = set(STOPWORDS)

    # Create word cloud object
    wc = WordCloud(background_color='black', max_words=200, mask=mask, stopwords=stopwords)

    # Generate the word cloud.
    wc.generate(text)

    # Save the word cloud as a .png file.
    wc.to_file('output.png')


# Request a topic from the user to make a word cloud with. Note: the user will get an error when there are more than 1 possible pages.
topic = input('Please enter the topic for the word cloud: ')

# Create the word cloud with the given input.
create_wordcloud(get_wiki(topic))
