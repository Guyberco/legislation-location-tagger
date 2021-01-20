import os

def runTagger():
    os.chdir("tagger/lemlda/tagger")
    os.system("java -Xmx1200m -XX:MaxPermSize=256m -cp trove-2.0.2.jar:morphAnalyzer.jar:opennlp.jar:gnu.jar:chunker.jar:splitsvm.jar:duck1.jar:tagger.jar vohmm.application.BasicTagger ./ ../../../../TextFiles/input ../../../../TextFiles/output -NER -conll")
