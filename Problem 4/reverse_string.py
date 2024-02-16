"""
Complete the following python code to reverse the string entered by the user.

Name: Braden Stanfield
Lab Time: Fri 3
"""

def reverse_string():
    # YOUR CODE HERE
    word = ""
    while input() != "done":
        word = input()
        drow = ""
        t = 0
        while len(drow) < len(word):
            drow += word[len(word) - t]
            t += 1
        print(drow)

if __name__ == "__main__":
    reverse_string()