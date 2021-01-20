import os
from googletrans import Translator
from textblob import TextBlob
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize


translator = Translator()
java_path = "C:/Program Files/Java/jdk-15.0.1/bin/java.exe"  #env var
os.environ["JAVAHOME"] = java_path
st = StanfordNERTagger("C:/Users/zemse/Desktop/school/digital sc/final project/legislation-location-tagger/src/stanford-ner-4.2.0/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz",
                       path_to_jar="C:/Users/zemse/Desktop/school/digital sc/final project/legislation-location-tagger/src/stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar")

"""
input: string of text(sentence or word)
the function translates the word to english and tags the words of the text, returns true if there is a Location tag
"""
def checkIsLocationInTranslate(text):
    englishTranslate = translator.translate(text)  #translate to english
    classified_text = st.tag(word_tokenize(englishTranslate.text))  # tag the words of the text
    return checkLocInList(classified_text)

def checkLocInList(tagged_text):
    for tagged in tagged_text:
        if(tagged[1] == "LOCATION"):
            return True
    return False

