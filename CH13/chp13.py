#import urllib.request

#url = "http://textfiles.com/stories/psf.txt"
#destination_filename = "psf.txt"

#urllib.request.urlretrieve(url, destination_filename)

def reverse_file():

    f = open("psf.txt", "r")
    xs = f.readlines()
    f.close()

    xs_2 = [ ]
    for line in xs:
        xs_2.insert(0, line)

    g = open("reversedfile.txt", "w")
    for line in xs_2:
        g.write(line)
    g.close()

#reverse_file()

def print_snake():

    mynewhandle = open("psf.txt", "r")
    while True:                            # Keep reading forever
        theline = mynewhandle.readline()   # Try to read next line
        if len(theline) == 0:              # If there are no more lines
            break                          #     leave the loop
        
        if theline.lower().find("snake") != -1:
            # Now process the line we've just read
            print(theline, end="")
    
    mynewhandle.close()

#print_snake()


def line_num_file():

    f = open("psf.txt", "r")
    xs = f.readlines()
    f.close()
    
    xs_2 = [ ]
    n = 1
    for line in xs:
        columns = ("{0:05d}".format(n))
        result = columns + line
        xs_2.insert(len(xs), result)       
        n += 1
    
    g = open("linenumberfile.txt", "w")
    for line in xs_2:
        g.write(line)
    g.close()
    
line_num_file()
        


def omit_linenum_file():
    f = open("linenumberfile.txt", "r")
    xs = f.readlines()
    f.close()
    # read file with numbered lines
    
    
    xs_2 = [ ]
    n = 1
    columns = ("{0:05d}".format(n))
    for line in xs:
        result = columns + line
        n +=1

        line_without_columns = result.replace(columns,"") 
        xs_2.insert(len(xs), line_without_columns)       
    
    # take out numbered lines
    
    
    
    g = open("omitlinenum.txt", "w")
    for line in xs_2:
        g.write(line)
    g.close()
    # write out new file without line numbers

omit_linenum_file()    
#call function

    



