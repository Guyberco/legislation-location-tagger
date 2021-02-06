# legislation-location-tagger

This tool may help you to identify and tag locations in Israel laws.

It takes all laws in xml format, in originalLaws directory, and wrap the locations with "refersTo", which contains the name of th
location, and with href, which contains an extrnal open lined data link, which is currently DBpedia.


For a location MY_LOCATION that found in your xml file, the following will replace the MY_LOCATION text:

<location refersTo="MY_LOCATION" href="https://dbpedia.org/page/LOCATION">MY_LOCATION </location>


To run the tool, you should first have LDA tagger of BGU university installed in src/tagger.
You can dowload from here https://www.cs.bgu.ac.il/~elhadad/nlpproj/LDAforHebrew.html.
