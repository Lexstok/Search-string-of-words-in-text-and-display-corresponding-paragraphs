# Search for string in paragraph
# Adaptation from C code
# Alex Boschmans

def usage():
    print """
    Program to read text from a file or from raw input, buffering text and searching for a string.
    When 2 CRs are found (a paragraph) if a match was found in it the buffer is
    printed.  The buffer is cleared and reading continued.
    The effect is to print the entire paragraph if it contains a match.

    Usage: python stringintext.py <searchstring> -f <filename>
    """

def filexists(fname):
    # does the file exist ?
    if os.path.isfile(fname):
        #print "ok file exists"
        pass
    else:
        print "Sorry, the file does not exist."
        exit()

# MAIN
import os, argparse

# parse input
parser= argparse.ArgumentParser()
parser.add_argument("-f", "--filename", help="filename to search - optional")
parser.add_argument("-s", "--search", help="search string (can be multiple words) to look for - at least one word is required", nargs='+')
args = parser.parse_args()

if args.filename:
    #print "filename is ", args.filename

    # does the file exist ?
    filexists(args.filename)

    # open the file for reading
    f = open(args.filename, 'r')
    paragraph = []
    LF_count = 0
    
    print "--------------------------------------------"

    for line in f:
        # split in paragraphs
        if line.strip(" ") == "\n":
             LF_count += 1
             # print "Linefeed detected, count is now ", LF_count
             if LF_count == 2:
                 #we have a full paragraph, but is the keyword in the paragraph ?
                 part = ''.join(paragraph)
                 
                 if ' '.join(args.search) in part:
                     #print "***paragraph found: ***"
                     print part
                 # reset counters
                 LF_count = 0
                 paragraph = []
        else:
            paragraph.append(line)
            
    # Finished file, print last collected paragraph
    part = ''.join(paragraph)
    if ' '.join(args.search) in part:
        print ''.join(paragraph)

else:
    # No file supplied, so search in supplied text
    # FUTURE
    pass


#Closure    
print "--------------------------------------------"
print "Search term was : ", ' '.join(args.search)










