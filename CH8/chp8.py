
def prefixes():
    prefixes = "JKLMNOPQ"
    suffix = "ack"

    
    for letter in prefixes:
        if letter == "O":
            print(prefixes[5] +"uack")
        elif letter =="Q":
            print(prefixes[7] + "uack")
        else:
            print(letter + suffix)
            
print (prefixes())

# "None" is printed out in the console below, I am not sure where in the code that is coming from


def count_letters(string, letter):
    count = 0
    for char in string:
        if char == letter:
            count += 1
    return count

#print (count_letters("eggplant", "g"))


def find2(strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

#print (find2("banana", "a", 2)) #== 3)

def count_letters_2(string, letter):
    count = 0
    index = find2(string, letter, 0)
    while index != -1:
        count += 1
        index = find2(string, letter, index + 1)        
    return count

print (find2("tarantula", "a", 1))
print (find2("tarantula", "a", 2))
print (find2("tarantula", "a", 5))

import string

def remove_punctuation(s):
    s_without_punct = ""
    for letter in s:
        if letter not in string.punctuation:
            s_without_punct += letter
    return s_without_punct

    
def analyze_string(str):

    no_punctuation = remove_punctuation(str)
    words = no_punctuation.split()
    word_count = len(words)
    e_word_count = 0
    for word in words:
        if word.find("e") >= 0:
            e_word_count += 1
    percentage = (e_word_count/ word_count) * 100
                    
    print('Your text contains {0} words, of which {1} ({2:.1f}%) contain an "e".'.format(word_count, e_word_count, percentage))

anthem = """Oh, say can you see by the dawn's early light. What so proudly we hailed at the twilight's last gleaming?
    Whose broad stripes and bright stars through the perilous fight,
    O'er the ramparts we watched were so gallantly streaming?
    And the rocket's red glare, the bombs bursting in air,
    Gave proof through the night that our flag was still there.
    Oh, say does that star-spangled banner yet wave
    O'er the land of the free and the home of the brave?"""
    
analyze_string(anthem)



def print_multiples(n, high):
    for i in range(1, high+1):
        print('%4d' % (n * i), end="")            
    print()

def print_mult_table(high):
    print("       ", end="")
    print_multiples(1, high)
    print("  :----------------------------------------------------")
    for i in range(1, high+1):
        print('%2d:    ' % (i), end="")
        print_multiples(i, high)

print_mult_table(12)


#def reverse(string):
#    return string[::-1]

def reverse(string):
    quotes = ""
    for ch in range(len(string) - 1, -1, -1):
        quotes = quotes + string[ch]        
    return quotes

def reverse_2(string):
    quotes = ""
    for ch in string:
        quotes = ch + quotes
    return quotes


def mirror(string):
    return string + reverse(string)

def remove_letter(letter,strng):
    string_minus_ltr = ""
    for ch in strng:
        if ch not in letter:
            string_minus_ltr += ch
    return string_minus_ltr 


def is_palindrome(strng):
    if strng == reverse(strng):
        return True
    else:
        return False

def is_palindrome_2(str):
        
    length = len(str)
    index = 0
   
    if len(str) == 1:
        return True
    
    if len (str) == 0:
        return True
    
    while index < length / 2 + 1:
        if str[index] != str[length - index - 1]:
            return False
            break
        index += 1
    else:
        return True
    
    

def count(sub, strng):
    count = 0
    index = strng.find(sub)
    while index != -1:
        count += 1
        index = strng.find(sub, index + 1)
    return count
        
#    count = 0
#    index = -1
#    while True:
#        index = strng.find(sub, index + 1)
#        if index == -1:
#            break
#        count += 1
#    return count

def remove(sub,strng):
    str_without_first_sub = strng.replace(sub,"", 1)
    return str_without_first_sub


def remove_2(sub,strng):
    if sub not in strng:
        return strng
    
    ret_val = ""
    index = strng.find(sub)
    length = len(sub)
    part_1 = strng[:index]
    part_2 = strng[(index+length):]
    ret_val = part_1 + part_2
    return ret_val


def remove_all(sub,strng):
    str_no_subs = strng.replace(sub,"")
    return str_no_subs


def remove_all_2 (sub, str):
    if sub not in str:  # this edge case is not necessary to make code work
        return str
    
    length = len(sub)
    ret_val = ""
    index = str.find(sub)
    while index != -1:
        ret_val = ret_val + str[:index] 
        str = str[index+length:] 
        index = str.find(sub)
        
    ret_val = ret_val + str
    return ret_val
        

import sys

def test(did_pass):
    """  Print the result of a test.  """
    linenum = sys._getframe(1).f_lineno   
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)
    

def test_suite():
    """ Run the suite of tests for code in this module (this file).
    """
    test(reverse("happy") == "yppah")
    test(reverse("Python") == "nohtyP")
    test(reverse("") == "")
    test(reverse("a") == "a")
    
    test(reverse_2("happy") == "yppah")
    test(reverse_2("Python") == "nohtyP")
    test(reverse_2("") == "")
    test(reverse_2("a") == "a")
    
    test(mirror("good") == "gooddoog")
    test(mirror("Python") == "PythonnohtyP")
    test(mirror("") == "")
    test(mirror("a") == "aa")
    
    test(remove_letter("a", "apple") == "pple")
    test(remove_letter("a", "banana") == "bnn")
    test(remove_letter("z", "banana") == "banana")
    test(remove_letter("i", "Mississippi") == "Msssspp")
    test(remove_letter("b", "") == "")
    test(remove_letter("b", "c") == "c")
    
    test(is_palindrome("abba"))
    test(not is_palindrome("abab"))
    test(is_palindrome("tenet"))
    test(not is_palindrome("banana"))
    test(is_palindrome("straw warts"))
    test(is_palindrome("a"))
    test(is_palindrome(""))    # Is an empty string a palindrome?
    
    test(is_palindrome_2("abba"))
    test(not is_palindrome_2("abab"))
    test(is_palindrome_2("tenet"))
    test(not is_palindrome_2("banana"))
    test(is_palindrome_2("straw warts"))
    test(is_palindrome_2("a"))
    test(is_palindrome_2(""))    # Is an empty string a palindrome?
        
    test(count("is", "Mississippi") == 2)
    test(count("an", "banana") == 2)
    test(count("ana", "banana") == 2)
    test(count("nana", "banana") == 1)
    test(count("nanan", "banana") == 0)
    test(count("aaa", "aaaaaa") == 4)
    
    test(remove("an", "banana") == "bana")
    test(remove("cyc", "bicycle") == "bile")
    test(remove("iss", "Mississippi") == "Missippi")
    test(remove("eggs", "bicycle") == "bicycle")

    test(remove_2("an", "banana") == "bana")
    test(remove_2("cyc", "bicycle") == "bile")
    test(remove_2("iss", "Mississippi") == "Missippi")
    test(remove_2("eggs", "bicycle") == "bicycle")
    
    test(remove_all("an", "banana") == "ba")
    test(remove_all("cyc", "bicycle") == "bile")
    test(remove_all("iss", "Mississippi") == "Mippi")
    test(remove_all("eggs", "bicycle") == "bicycle")

    test(remove_all_2("an", "banana") == "ba")
    test(remove_all_2("cyc", "bicycle") == "bile")
    test(remove_all_2("iss", "Mississippi") == "Mippi")
    test(remove_all_2("eggs", "bicycle") == "bicycle")

    
 
    
test_suite()

    

