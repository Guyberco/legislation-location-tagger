
# Add tag to the Location
# def wrapText(string, textToWrapLen, textStartIndex, prefix, suffix):
#     string = addToString(string, prefix, textStartIndex)
#     string = addToString(string, suffix, textStartIndex + textToWrapLen + len(prefix))
#     return string

def addToString(str, strToAdd, index):
    return str[ : index] + strToAdd + str[index : ]

def wrapString(strToWrap, prefix, suffix):
    return prefix + strToWrap + suffix

def replaceWordAtIndex(str, strToReplaceWith, index, prevWordSize):
    if -1 < index < len(str):
        return str[ : index] + strToReplaceWith + str[index + prevWordSize:]
    else:
        return str
