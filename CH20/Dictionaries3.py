import io

def wordcount():
    mynewhandle = open("/Users/Home/Downloads/a2.txt", "r")
    longestWord = ""
    dictionary = {}                        # word is key, count is value (word->count)
    while True:                            # Keep reading forever
        aLine = mynewhandle.readline()     # Try to read next line
        if len(aLine) == 0:                # If there are no more lines
            break                          #     leave the loop
    
        # Now process the line we've just read
        #print(theline, end="")
        for word in aLine.split():
            lowerWord = word.lower()
            if len(lowerWord) > len(longestWord):
                longestWord = lowerWord
            dictionary[lowerWord] = dictionary.get(lowerWord,0) + 1

    print("Biggest word: " + longestWord + " " + str(len(longestWord)))
    
    mynewhandle.close()



wordcount()
