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
    counter = 1
    string = ""

    for pos in range(1, len(n)):
                
        if n[pos] == n[pos-1]:
            counter += 1
        else:
            string += str(counter) + n[pos-1]
            counter = 1

    string += str(counter) + n[len(n)-1]        
         
    print(string)
        
num = 9000 #Testing
look_say(num)
