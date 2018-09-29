

import nltk
from nltk.stem.lancaster import LancasterStemmer
from collections import defaultdict


def filtering(words):
    # This function is used for case normalization , stemming and stopwords removal #

    st = LancasterStemmer()                         #Using stemmer from  http://www.nltk.org/api/nltk.stem.html
    docID = 0
    stopWords = ['the', 'is', 'at', 'of', 'on', 'and', 'a']     #Stop words list
    mylist = []

    for word in words:
        if word =='DOC':                            # Getting document ID
            docID +=1
            continue

        if word.isalpha():
            word = word.lower()                     # Convert to lower case and append
            rootword = st.stem(word)                # Getting root word of the word
            if rootword in stopWords:               # Creating list of root words with document number
                continue
            else :
                mylist.append((rootword,docID))

        elif word.isdigit():                        # Adding numbers in list with document number
            mylist.append((word,docID))

    return mylist



def createDict(mylist):
    # This function creates dictionary of the list (containing words and respective documents) #

    dict=defaultdict(list)
    for key,value in mylist:
        dict[key].append(value)

    return dict


def tokenizeDoc(file_content):
    # This function is used to tokenize of the given content#

    words = nltk.word_tokenize(file_content)         # Tokenize the words
    return words



def mainModule(file_content):
    # This function takes complete data set as an input and provide dictionary of the keys (as words) and values ( as document lists)#

    # file_content = open("/Users/tejasvibelsare/Library/Mobile Documents/com~apple~CloudDocs/Fall 2018/Search Engines/HW1 documents.txt").read()

    words=tokenizeDoc(file_content)                   # Tokenize the words

    mylist= filtering(words)                          # Check for all filters
    diction = createDict(mylist)                      # Creation of dictionary from list

    return diction

