"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:Braden Stanfield
Lab Time: Fri 3
"""

def norm():
    # Write your code here
    t = int(input())
    r = 0
    list = [t]
    while r < t:
        num = input()
        list[r] = num
        r += 1
    print(list)

if __name__ == "__main__":
    norm()