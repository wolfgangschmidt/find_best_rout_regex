import re

# this is the test list of directions, feel free to add or remove elements
instructions = ["WEST", "SOUTH","NORTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST", "WEST", "NORTH",
              "SOUTH", "WEST", "EAST", "NORTH", "WEST", "EAST" , "WEST", "NORTH", "SOUTH", "EAST",
              "EAST", "SOUTH", "NORTH", "NORTH", "WEST", "NORTH", "SOUTH", "EAST", "EAST", "NORTH",
              "WEST", "EAST" , "WEST", "NORTH", "SOUTH",]

SETS = [r"/NORTH/SOUTH", r"/SOUTH/NORTH", r"/EAST/WEST", r"/WEST/EAST"]


def makestring(directions):
    """I decided to transform the list into a string to apply regex principles. """
    return '/'.join(directions).upper()
    

def dirReduc(x):
    """ option 1 is more artesanal no imports used. """
    x = x.replace(SETS[0], '').replace(SETS[1], '').replace(SETS[2],'').replace(SETS[3], '')
    if any( y in x for y in SETS):
        dirReduc(x)
    else:
        result = x.split('/')
        print(result)
    

def dirRedux(x):
    """ option 2 does the same but using the re library. """
    patterns = SETS
    for pattern in patterns:
        x = re.sub(pattern, '', x )
    if any( y in x for y in patterns):
        dirRedux(x)
    else:
        result = x.split('/')
        print(result)


def main():
    string = makestring(instructions)
    dirReduc(string)
    dirRedux(string)


""" I am sure there are probably better ways of addressing this problem in more traditional ways
    but I found this to be a straight forward and practicle way. if this isn't in anyway the expected
    path or acceptable way to solve this problem please do give a feedback so I can improve myself.
"""
