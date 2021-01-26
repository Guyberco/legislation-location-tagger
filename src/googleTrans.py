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


def checkIsLocationInTranslate(text):
    """
    :param text: string of text that represent a word or an sentence
    :return: true if the translated tagged text contains a LOCATION TAG
    """
    englishTranslate = translator.translate(text)  #translate to english
    classified_text = st.tag(word_tokenize(englishTranslate.text))  # tag the words of the text
    return checkLocInList(classified_text)

def checkLocInList(tagged_text):
    """
    :param tagged_text: english text that was tagged with the Stanford ner library
    :return: true if one of the tagged word is tagged with LOCATION
    """
    for tagged in tagged_text:
        if(tagged[1] == "LOCATION"):
            return True
    return False

