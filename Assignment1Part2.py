
def getIntersect(postingList1,postingList2):
    # This function compares the posting lists and gives intersected list as an output#

    intersectedList=[]
    i=0
    j=0
    while i < len(postingList1) and j < len(postingList2):
        if postingList1[i] == postingList2[j]:                      # If document IDs match
            intersectedList.append(postingList1[i])                 # Appending matched document IDs to intersected list
            i+=1
            j+=1
        else :
            if postingList1[i] < postingList2[j] :                  #If document IDs do not match
                i+=1
            else :
                j+=1
    return intersectedList



