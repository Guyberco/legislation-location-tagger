# legislation-location-tagger

This tool may help you to identify and tag locations in Israel legislation.

This tool was made in a Digital Humanities for CS Students course in Ben Gurion University of the Negev, taught by Yael Netzer.

The program was writtten mainly in python and uses some other tools.


The program takes all law files in xml format, in originalLaws directory, and wraps the locations in a location tag with "refersTo", which contains the name of the
location, and with href, which contains an extrnal opened linked data link, which is currently DBpedia.


This is a very powerfull and usefull tool that may help you manupluating laws with respect to the locations that in them.
It may helps you to get a really informative data about location in the Israel legislation, which can be taken for differenet uses.


In addition, we have attached an example of how to run over all <location>, extract them, and making with them
a usefull structures - GeoJson format file, which displays all locations that have been found in Israel law in a map,
with a list of laws and various inforational graphs.


For a location $MY_LOCATION that found in your xml file, the following will replace the $MY_LOCATION text:

  <location refersTo="$MY_LOCATION" href="https://dbpedia.org/page/$MY_LOCATION">$MY_LOCATION </location>


To run the tool, you should:
* first have LDA tagger of BGU university installed in src/tagger.
* change StanfordNERTagger variable to your JAVA path.
* Run main() function.


You can dowload from here https://www.cs.bgu.ac.il/~elhadad/nlpproj/LDAforHebrew.html.

Second, run the main() function which is in src/main.py, and you are ready to go!

Now all your laws contains location wrapped by our schema.

You can find the new xml files in final_output directory.

The following tools are being used:

  LDA for Hebrew - Dr. Adler BGU, Prophesor elhadad BGU

  Google Translate

  Stanford NER Tagger

  DBpedia

  GeoJson



Tool written by Israel Zemser and Guy Bercovich

