"""
Complete the following python code to reverse the string entered by the user.

Name: Braden Stanfield
Lab Time: Fri 3
"""

def reverse_string():
    # YOUR CODE HERE
    word = input()
    p = 1
    if word == "done":
        p = 0
    if word == "d":
        p = 0
    if word == "Done":
        p = 0
    while p == 1:
        
        drow = ""
        t = 1
        while len(drow) < len(word):
            drow += word[len(word) - t]
            t += 1
        print(drow)
        word = input()
        if word == "done":
            p = 0
        if word == "d":
            p = 0
        if word == "Done":
             p = 0

if __name__ == "__main__":
    reverse_string()