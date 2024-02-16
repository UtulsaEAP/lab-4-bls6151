"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name:Braden Stanfield
Lab Time: Fri 3

"""


def reverse_binary():
    user_num = int(input())
    # YOUR CODE HERE
    x = user_num
    a = ""
    while x > 1:
        a+= str(int(x % 2))
        x = x/2
    print(a)
if __name__ == "__main__":
    reverse_binary()