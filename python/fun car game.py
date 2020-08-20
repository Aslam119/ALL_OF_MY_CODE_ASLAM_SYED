started = False
print('''
                                    CAR GAME
''')
start = "start - to start car"
stop = "stop - to stop car"
Quit = "quit - to quit"
fuel = 20
print(start)
print(stop)
print(Quit)

command = ''
while command != "quit" or fuel == 0:
    print("YOUR FUEL IS ",fuel)
    command = str(input("> ").lower())
    if command == "start" and started is False and fuel > 1:
        print("Car started")
        fuel -= 5
        started = True
    elif command == "start" and started is True:
        print("Car already started")
    elif command == "start" and started is False and fuel < 1:
        print("fuel over")
        exit(0)
    elif command == "stop" and started is True:
        print("Car stopped")
        fuel -= 5
        started = False
    elif command == "stop" and started is False:
        print("Car is already stopped")
    elif command == "quit":
        print("THANK YOU FOR PLAYING")
        exit(0)
    elif fuel == 0:
        print("fuel over thanks for playing")
        exit(0)
    else:
        print("I DON'T UNDERSTAND ", command)
