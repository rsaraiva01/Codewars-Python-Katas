# Your task is to create a function that will take an integer and return the result of the look-and-say function on that integer. This should be a general function that takes as input any positive integer, and returns an integer; inputs are not limited to the sequence which starts with "1".

    #For example:
    #Start with 1.
    #There is one 1 --> 11
    #Start with 11. There are two 1 digits --> 21
    #Start with 21. There is one 2 and one 1 --> 1211
    #Start with 1211. There is one 1, one 2, and two 1s --> 111221
    #Sample inputs and outputs::

    #0 --> 10
    #2014 --> 12101114
    #9000 --> 1930
    #22322 --> 221322
    #222222222222 --> 122

def look_say(n):
    n = str(n)
    c = ""
    sl_in = 0

    for position, digit in enumerate(n):
        if digit != n[sl_in]:
            sl = slice(sl_in, position)
            r = str(len(n[sl])), n[position-1]
            c += "".join(r)
            sl_in = position
        if position == len(n)-1:
            sl = slice(sl_in, len(n))
            r = str(len(n[sl])), n[position]
            c += "".join(r)
    print(int(c)) #Debug
    return c   
        
num = 0 #Testing
look_say(num)
