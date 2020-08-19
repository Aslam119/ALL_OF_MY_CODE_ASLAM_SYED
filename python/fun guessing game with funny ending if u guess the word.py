secretWord = "giraffe"
clues = ["", "animal in movie madagascar", "large animal", "animal with longest neck", "HAHA TOUGHT IT WAS A CLUE, YOU LOST"]
guess = ""
guessCount = 0
while guess != secretWord:
    print("GUESS ", guessCount, " :-")
    print("")
    guess = str(input("Enter guess: "))

    if guess == secretWord:
        print("YOU WIN!!")
        print("A GIRAFFE PIC FOR YOU")
        print('''
              
  |_|
<(+ +)>
 ( u )
    \\
     \\
      \\               )
       \\             /
        \\___________/
        /|          /|
       //||      ( /||
      // ||______//_||
     //  ||     //  ||
    //   ||    //   ||
    \\   ||    \\   ||
     \\  ||     \\  ||
     //  ||     //  ||
    /_\ /__\   /_\ /__\
        ''')

    else:
        guessCount += 1
        print("CLUE :", clues[guessCount])
    if guessCount >= 4:
        print("EXCEEDED GUESS LIMIT U LOSSE")
        exit(0)
