import os

envPath = os.path.dirname(os.path.realpath(__file__))
windows=True
runTaggerMac = "java -Xmx1200m -XX:MaxPermSize=256m -cp trove-2.0.2.jar:morphAnalyzer.jar:opennlp.jar:gnu.jar:chunker.jar:splitsvm.jar:duck1.jar:tagger.jar vohmm.application.BasicTagger ./ ./ outputfile -NER -lemma -conll"
runTaggerWindows = "java -Xmx1200m -XX:MaxPermSize=256m -cp trove-2.0.2.jar;morphAnalyzer.jar;opennlp.jar;gnu.jar;chunker.jar;splitsvm.jar;duck1.jar;tagger.jar vohmm.application.BasicTagger .\  ../../../TextFiles/tagger_input ../../../TextFiles/tagger_output -NER -lemma -conll"

