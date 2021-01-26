import os

from env import windows, runTaggerWindows, runTaggerMac


def runTagger():
    os.chdir("tagger/tagger")
    if windows:
        os.system(runTaggerWindows)
    else:
        os.system(runTaggerMac)