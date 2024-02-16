"""
Complete the following python code to print all numbers between the two values incrementing by 5 from the initial value to the final value. The initial value and final value are entered by the user. If the final value is less than the initial value, print "Second integer can't be less than the first.

Name: Braden Stanfield
Lab Time: Fri 3
"""

def inc_5():
    num1 = int(input())
    num2 = int(input())
    # Write your code here
    a = ""
    if num2 >= num1:
        while num1 <= num2:
            a += str(num1) + " "
            num1 = int(num1) + 5
        print(a)
    else:
        print("Second integer can't be less than the first.")



if __name__ == '__main__':
    inc_5()