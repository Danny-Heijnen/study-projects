import wikipedia
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image
import multidict as multidict
import re


def getFrequencyDictForText(sentence):
    fullTermsDict = multidict.MultiDict()
    tmpDict = {}

    # making dict for counting frequencies
    for text in sentence.split(" "):
        if re.match("a|the|an|the|to|in|for|of|or|by|with|is|on|that|be", text):
            continue
        val = tmpDict.get(text, 0)
        tmpDict[text.lower()] = val + 1
    for key in tmpDict:
        fullTermsDict.add(key, tmpDict[key])
    return fullTermsDict


# TODO: waarom werkt het selecteren van het eerste zoekresultaat (title) niet? met .page(query) werkt het wel.
# Get the content of a wikipedia article.
def get_wiki(query):

    # Store the first suggested page as the title.
    # title = wikipedia.search(query, results=3)[0]
    title = wikipedia.search(query, results=3)
    print(title)

    # Get the wikipedia page for selected title.
    page = wikipedia.page(query)

    print(page.content)

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
    wc.generate_from_frequencies(text)

    # Save the word cloud as a .png file.
    wc.to_file('output.png')


# Request a topic from the user to make a word cloud with. Note: the user will get an error when there are more than 1 possible pages.
# Suggestion for good output: groningen
topic = input('Please enter the topic for the word cloud: ')

# Create the word cloud with the given input.
create_wordcloud(getFrequencyDictForText(get_wiki(topic)))
