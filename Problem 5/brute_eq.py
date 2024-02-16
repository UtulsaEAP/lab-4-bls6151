"""
Complete the python code to find the solution to the system of linear equations entered by the user. 
The equations are of the form ax + by = c and dx + ey = f. The solution should be printed in the form x = # and y = #. 
If there is no solution, print "There is no solution".

Name:Braden Stanfield
Lab Time: Fri 3
"""

def brute_eq():
    #Read in first equation, ax + by = c 
    a = int(input())
    b = int(input())
    c = int(input())

    #Read in second equation, dx + ey = f
    d = int(input())
    e = int(input())
    f = int(input())

    # YOUR CODE HERE
    x = -10
    y = -10
    p = ""
    while x < 10:
        y = -10
        while y < 10:
            if ((x*a) + (y*b) == c):
                if ((x*d) + (y*e) == f):
                    p = ("x = " + str(x) + ", y = " + str(y))
                    x = 10
                    y = 10
                else:
                    x += 1
            else:
                y += 1
        x += 1
    if p == "":
        print("There is no solution")
    else:
        print(p)

if __name__ == "__main__":
    brute_eq()