envPath = "C:/Users/zemse/Desktop/school/digital sc/final project/legislation-location-tagger/"
windows=True
runTaggerMac = "java -Xmx1200m -XX:MaxPermSize=256m -cp trove-2.0.2.jar:morphAnalyzer.jar:opennlp.jar:gnu.jar:chunker.jar:splitsvm.jar:duck1.jar:tagger.jar vohmm.application.BasicTagger ./ ./ outputfile -NER -lemma -conll"
runTaggerWindows = "java -Xmx1200m -XX:MaxPermSize=256m -cp trove-2.0.2.jar;morphAnalyzer.jar;opennlp.jar;gnu.jar;chunker.jar;splitsvm.jar;duck1.jar;tagger.jar vohmm.application.BasicTagger .\  ../../../TextFiles/input ../../../TextFiles/tagger_output -NER -lemma -conll"

