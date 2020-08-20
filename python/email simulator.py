senderFirstName = str(input("Enter sender's first name: "))
senderLastName = str(input("Enter sender's last name: "))
senderMail = str(input("Enter sender's mail: "))
recieverFirstName = str(input("Enter reciever's first name: "))
recieverLastName = str(input("Enter reciever's last name: "))
recieverMail = str(input("Enter reciever's mail: "))

print(f'''
    {senderMail} has succesfully sent an email to {recieverMail}
    Sender's details:
    Sender Name: {senderFirstName} {senderLastName}
    Sender mail: {senderMail}

    Reciever's details:
    Reciever Name: {recieverFirstName} {recieverLastName}
    Reciever mail: {recieverMail}
''')
