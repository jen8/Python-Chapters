prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    print letter + suffix

def remove_vowels(s):
    s = "Peter, Paul, and Mary"
    vowels = "aeiouAEIOU"
    s_without_vowels = ""
    for letter in s:
        if letter not in vowels:
            s_without_vowels += letter
    return s_without_vowels
#print remove_vowels(5)


def find2(strng, ch, start):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
print find2('banana', 'a', 2)
 
    
def find(strng, ch, start=0):
    index = start
    while index < len(strng):
        if strng[index] == ch:
            return index
        index += 1
    return -1
print find('banana', 'a', 2)