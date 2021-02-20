
import re
import codecs
import os, unicodedata
"""
 Robust Hebrew Tokenizer 

 works as a filter:
   hebtokenizer.py < in > out
   
 run as:
   hebtokenizer.py -h  
 for options

 KNOWN ISSUES:
     - NOT VERY FAST!!!

     - transition from hebrew words to numbers: ב-23:00  will be cut as ב-23 :00
     - deliberately not segmenting משהוכלב from start of words before numbers/quotes/dashes
     - emoticons are not supported (treated as punctuation)
     - ' is always kept at end of hebrew chunks (a document level pre/post processing could help here)
     - !!!!!!!111111 are split to !!!!!!!! 1111111
"""
#########

def heb(s,t): return ('HEB',t)
def eng(s,t): return ('ENG',t)
def num(s,t): return ('NUM',t)
def url(s,t): return ('URL',t)
def punct(s,t): return ('PUNCT',t)
def junk(s,t): return ('JUNK',t)

#### patterns
_NIKUD = u"\u05b0-\u05c4"
_TEAMIM= u"\u0591-\u05af"

undigraph = lambda x:x.replace("\u05f0","וו").replace("\u05f1","וי").replace("\u05f2","יי").replace("\ufb4f","אל").replace("\u200d","")

_heb_letter = r"([א-ת%s]|[דגזצתט]')" % _NIKUD

# a heb word including single quotes, dots and dashes  / this leaves last-dash out of the word
_heb_word_plus = r"[א-ת%s]([.'`\"\-/\\]?['`]?[א-ת%s0-9'`])*" % (_NIKUD,_NIKUD)

# english/latin words  (do not care about abbreviations vs. eos for english)
_eng_word = r"[a-zA-Z][a-zA-Z0-9'.]*"

# numerical expression (numbers and various separators)
#_numeric = r"[+-]?[0-9.,/\-:]*[0-9%]"
_numeric = r"[+-]?([0-9][0-9.,/\-:]*)?[0-9]%?"

# url
_url = r"[a-z]+://\S+"

# punctuations
_opening_punc = r"[\[('`\"{]"
_closing_punc = r"[\])'`\"}]"
_eos_punct = r"[!?.]+"
_internal_punct = r"[,;:\-&]"

# junk
#_junk = ur"[^א-ת%sa-zA-Z0-9%%&!?.,;:\-()\[\]{}\"'\/\\+]+" #% _NIKUD
_junk = r"[^א-ת%sa-zA-Z0-9!?.,:;\-()\[\]{}]+" % _NIKUD #%%&!?.,;:\-()\[\]{}\"'\/\\+]+" #% _NIKUD

is_all_heb = re.compile(r"^%s+$" % (_heb_letter),re.UNICODE).match
is_a_number = re.compile(r"^%s$" % _numeric ,re.UNICODE).match
is_all_lat= re.compile(r"^[a-zA-Z]+$",re.UNICODE).match
is_sep = re.compile(r"^\|+$").match
is_punct = re.compile(r"^[.?!]+").match




#### scanner

scanner = re.Scanner([
    (r"\s+", None),
    (_url, url),
    (_heb_word_plus, heb),
    (_eng_word, eng),
    (_numeric,  num),
    (_opening_punc, punct),
    (_closing_punc, punct),
    (_eos_punct, punct),
    (_internal_punct, punct),
    (_junk, junk),
])

def tokenize(sent):
    #print(sent)
    tok = sent

    parts,reminder = scanner.scan(tok)
    assert(not reminder)
    return parts

def hasar_niqqud(source="niqqud.txt"):
    """This function removes niqqud vowel diacretics from Hebrew.
    @param source: The source filename with .txt extension."""

    path  = os.path.expanduser('~/Documents/'+str(source))
    f= open(path,'r', encoding='utf-8')
    content = f.read()
    normalized=unicodedata.normalize('NFKD', content)
    no_niqqud=''.join([c for c in normalized if not unicodedata.combining(c)])
    f.close()
    path  = os.path.expanduser('~/Documents/'+str(source)[:-4]+"-removed.txt")
    f = open(path,'w',encoding='utf-8')
    f.write(no_niqqud)
    f.close()

def tokenize_all(inpath, outpath):

    with os.scandir(inpath) as it:
        for entry in it:
            if entry.name.endswith(".txt") and entry.is_file():
                outfile = codecs.open(outpath+ entry.name,'w',encoding='utf8')
                infile = codecs.open(entry,'r',encoding='utf8')
                for sent in infile:
                    outfile.write(" ".join([tok for (which,tok) in tokenize(sent)]))
                    outfile.write("\n")
                outfile.close()
                infile.close()


tokenize_all("C:/Users/zemse/Downloads/LawRepoWiki/tokenize/before", "C:/Users/zemse/Downloads/LawRepoWiki/tokenize/after")