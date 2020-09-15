leave = ''


def food():
    foodItems = '''
(1)Lays Chips[5$]   (2)Turkey Sandwich[5$]    (3)Pastry[5$]
(4)Pizza[8$]       (5)Twix Chocolate[8$]      (6)Chocobar[8$]
(7)Candy Bar[10$]    (8)Crossiant[10$]           (9)Cupcake[10$]
'''
    print(foodItems)


budget = int(input('ENTER YOUR BUDGET: '))

while leave != 'y' and budget > 0:
    food()
    pick = int(input('PICK: '))

    if pick == 1 and pick <= 5 and pick > 0:
        budget -= 5
        print(f'YOU HAVE BOUGHT LAYS CHIPS YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

    elif pick == 2 and pick <= 5 and pick > 0:
        budget -= 5
        print(f'YOU HAVE BOUGHT TURKEY SANDWICH YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

    elif pick == 3 and pick <= 5 and pick > 0:
        budget -= 5
        print(f'YOU HAVE BOUGHT PASTRY YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))



    elif pick == 4 and pick <= 8 and pick > 0:
        budget -= 8
        print(f'YOU HAVE BOUGHT PIZZA YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

    elif pick == 5 and pick <= 8 and pick > 0:
        budget -= 8
        print(f'YOU HAVE BOUGHT Twix Chocolate YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

    elif pick == 6 and pick <= 8 and pick > 0:
        budget -= 8
        print(f'YOU HAVE BOUGHT Chocobar YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))


    elif pick == 7 and pick <= 10 and pick > 0:
        budget -= 10
        print(f'YOU HAVE BOUGHT CANDY BAR YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

    elif pick == 8 and pick <= 10 and pick > 0:
        budget -= 10
        print(f'YOU HAVE BOUGHT CROSSSIANT YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

    elif pick == 9 and pick <= 10 and pick > 0:
        budget -= 10
        print(f'YOU HAVE BOUGHT CUPCAKE YOUR BUDGET IS {budget}')
        leave = str(input('do you want to leave:'))

print('----------------BYE----------------')
