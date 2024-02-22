"""
Complete the following python code to take in a list of values from the user and then normalize them

Name:Braden Stanfield
Lab Time: Fri 3
"""

def norm():
    # Write your code here
    t = int(input())
    r = 0
    list = []
    
    while r < t:
        num = input()
        list.append(num)
        r += 1
    lar = float(list[0])
    for i in range (1,t):
        if float(list[i]) > lar:
            lar = float(list[i])
    for k in range(0,t):
        list[k] = float(list[k]) / float(lar)

    for j in range (0,t):
        print(f'{float(list[j]):.2f}')

if __name__ == "__main__":
    norm()