
import sys
import collections

str = sys.argv[1]
dictionary = {}
    
for char in str:
    new_char = char.lower()
    if new_char.isalpha():
        if new_char in dictionary:
            dictionary[new_char] += 1
        else:
            dictionary[new_char] = 1
        
od = collections.OrderedDict(sorted(dictionary.items()))        
for key, value in od.items():
    print (key, value)
    
