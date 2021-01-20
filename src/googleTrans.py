import os
from googletrans import Translator
from textblob import TextBlob
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tokenize import word_tokenize
translator = Translator()
java_path = "C:/Program Files/Java/jdk-15.0.1/bin/java.exe"
os.environ["JAVAHOME"] = java_path
st = StanfordNERTagger("./stanford-ner-4.2.0/stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz",
                       path_to_jar="./stanford-ner-4.2.0/stanford-ner-2020-11-17/stanford-ner.jar")
tranText = translator.translate("אני הולך לבית שלי בבאר-שבע")
classified_text = st.tag(word_tokenize(tranText.text))
print(classified_text)

