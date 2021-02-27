import wikipedia
from wordcloud import WordCloud, STOPWORDS


def get_wiki(query):
    title = wikipedia.search(query)[0]

    # get wikipedia page for selected title
    page = wikipedia.page(title)
    return page.content


print(get_wiki('python programming language'))
