import Assignment1Part1
import Assignment1Part2
from nltk.stem.lancaster import LancasterStemmer
import sys


def preprocessing(word):
    #This function is used for preprocessing of words before comparison with given query#

    st = LancasterStemmer()
    stopWords = ['the', 'is', 'at', 'of', 'on', 'and', 'a']

    if word.isalpha():
        word = word.lower()                                                        # Convert to lower case and append
        stemWord = st.stem(word)                                                   # Getting rootword of the word
        if stemWord in stopWords:                                                  # Checking if it is among rootwords
            print '\nThese words have been excluded from search , kindly try another query!'
            sys.exit()
        else:
            pass

    return stemWord



def invertedIndexCreation():
    #This function is used for creation of inverted index on the basis of given dataset path#

    givenPath = raw_input("\nKindly provide path of the document set (including name) :")  # Getting file name and path from user

    try:
        file_content = open(givenPath).read()                                       # Read document from given path
        pass
    except IOError:                                                                 # Validation for given file name and path
        print "Unable to open file. Kindly check path and filename again.  "
        sys.exit()

    invertedIndex = Assignment1Part1.mainModule(file_content)                       # Calling function from Assignment1Part1.py to get Inverted Index
    return invertedIndex



def printInvertedIndex(invertedIndex):
    #This function is used for printing created inverted index#

    print ("\nPlease find below inverted index for given document :")
    for key in invertedIndex:                                                       # Printing Inverted Index
        count = len(invertedIndex[key])                                             # Getting count of documents matching
        #print str(key) + '\t\t' + str(count) + '\t--->\t' + str(invertedIndex[key])
        print('{0:10} {1:10}'.format(key, count) + '\t ===> \t' + str(invertedIndex[key]))



def executeQuery(invertedIndex):
    #This function is used for executing given query and giving common documents as an output#

    postingList1=[]
    postingList2=[]
    query = raw_input("Kindly provide the query :")
    word = query.split()
    found = 0

    word1 = word[0]
    word2 = word[2]

    givenWord1 = preprocessing(word1)
    givenWord2 = preprocessing(word2)


    if givenWord1 in invertedIndex.keys():                      #Checking if first word exist in keys
        postingList1 = invertedIndex[givenWord1]                # Getting posting list of first word

    else:
        print ("No results found for "+givenWord1)
        found = 1

    if givenWord2 in invertedIndex.keys():                      #Checking if second word exist in keys
        postingList2 = invertedIndex[givenWord2]                # Getting posting list of seciond word

    else:
        print ("No results found for "+givenWord2)
        found = 1

    intersectedList = Assignment1Part2.getIntersect(postingList1, postingList2)     #Calling function from Assignment1Part2
                                                                                    # for getting intersected list

    if found == 0:
        print "\nCommon documents in which both the words are present :"
        intersectedList = list(set(intersectedList))                        #Removing duplicate entries of documents
        for doc in range(len(intersectedList)):                             #Printing common documents

            print ("DOC " + str(intersectedList[doc]))


def main():
    # This is main function which accepts user's choice and provide output accordingly#

    choice = raw_input("\n 1: Inverted Index Creation \n 2: Execute the query \n \n Kindly select options from above : ")
    options = {
        1: "Inverted Index creation",
        2: "Execite the query"
    }

    try:                                                                    # Validation of user iunput
        choice=int(choice)                                                  #If input is an integer

        if choice == 1:
            # Part a

            invertedIndex = invertedIndexCreation()
            printInvertedIndex(invertedIndex)

        elif choice == 2:
            # Part b

            invertedIndex = invertedIndexCreation()
            executeQuery(invertedIndex)

        else:
            print "Insert correct choice!"                                  #If wrong choice

    except ValueError:                                                     # If wrong input
        print 'Provide correct choice!'



main()                                                                          # Calling main function






