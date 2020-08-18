# Password System So that only you can access your program
#You can change the password in the code if you want 

password = "python1234"
entered_password = str(input("ENTER PASSWORD: "))

#ENTER YOUR CODE HERE IN THE IF STATEMENT I ENTERED A SIMPLE HELLO WORLD 
if entered_password == password:
        print("hello world")
else:
    print("INVALID PASSWORD YOU CAN'T ACCESS THIS CODE. GOODBYE!")
    exit(0)
