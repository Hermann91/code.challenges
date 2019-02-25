"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot seperating them.

It should look like this:

Sam Harris => S.H

Patrick Feeney => P.F
"""

def abbrevName(name):


    #ab = ".".join(c for c in name if c.isupper())
    f = name.split()[0][0].upper()
    l = name.split()[-1][0].upper()
    return  f+"."+l
