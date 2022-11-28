from nltk.corpus import wordnet as wn
import requests
import json

def get_meaning(word):
    """
    get the meaning of the given word from wordnet
    :param word: string, the word for which meaning is to be found
    :return: string, the meaning of the word if the word is found in corpus; None otherwise
    """
    synset = wn.synsets(word)
    if synset:
        return synset[0].definition()
    else:
        return None


def get_synonyms(word):
    """
    get the synonyms for the given word from wordnet
    :param word: string, the word for which synonyms are to be found
    :return: the synonyms for the word
    """
    synonyms = []
    for synset in wn.synsets(word):
        for lemma in synset.lemmas():
            if lemma:
                synonyms.append(lemma.name())
    if synonyms:

        return synonyms[1]
    else:
        return None

def get_sentence(word):
    if str(word) =='none':
         return
    else:
        words = []
        language = 'en'
        word_id = word
        strictMatch = 'false'

        url = 'https://od-api.oxforddictionaries.com:443/api/v2/sentences/' + language + '/' + word_id.lower() + '?strictMatch=' + strictMatch

        r = requests.get(url, headers={"app_id": "b6ab83e9", "app_key": "ce2ea8bb3658ab04b3b7a1bab212f00c"})

        for i in range(5):
            words.append(str(r.json()['results'][0]['lexicalEntries'][0]['sentences'][i]['text']))

        return (words)
