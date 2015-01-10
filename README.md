Small python script to search for one or more words in a file and display the corresponding paragraphs.

Adaptation from C code found on http://forums.macrumors.com/showthread.php?t=1833952

    Program to read text from a file, buffering text and searching for a string.
    When 2 CRs are found (a paragraph) if a match was found in it the buffer is
    printed.  The buffer is cleared and reading continued.
    The effect is to print the entire paragraph if it contains a match.

Usage: python stringintext.py -s one or more words to search for -f filename

Parapgraphs are defined as have two empty lines between them.
