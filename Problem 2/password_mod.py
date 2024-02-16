"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

Name:Braden Stanfield
Lab Time: Fri 3
"""

def password_mod():
    word = input()
    password = ''
    t = 0
    # Type your code here.
    while(len(password) < len(word)) :
        if word[t] == "i":
            password += "1"
            t += 1
        elif word[t] == "a":
            password += "@"
            t += 1
        elif word[t] == "m":
            password += "M"
            t += 1
        elif word[t] == "B":
            password += "8"
            t += 1
        elif word[t] == "s":
            password += "$"
            t += 1
        else:
            password += word[t]
            t += 1
    print(password + "!")

    
if __name__ == "__main__":
    password_mod()