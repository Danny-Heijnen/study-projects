import wikipedia
from wordcloud import WordCloud, STOPWORDS
import numpy as np
from PIL import Image


def get_wiki(query):
    title = wikipedia.search(query)[0]
    print(title)

    # get wikipedia page for selected title
    page = wikipedia.page(title)
    return page.content


def create_wordcloud(text):

    mask = np.array(Image.open('tophat.png'))

    stopwords = set(STOPWORDS)

    # create wordcloud object
    wc = WordCloud(background_color='black', max_words=200, mask=mask, stopwords=stopwords)

    wc.generate(text)

    # save wordcloud
    wc.to_file('output.png')


# print(get_wiki('python programming language'))

topic = input('Please enter the topic for the word cloud: ')
create_wordcloud(get_wiki(topic))
