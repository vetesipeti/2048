
import random
import os
import shutil

def tab_start():

    global tab
    tab = []
    for i in range(4):
        tab.append([0,0,0,0])
    rand = []
    for r in range(4):
        rand.append(random.randrange(0,4))
    tab[rand[0]][rand[1]] = 2
    tab[rand[2]][rand[3]] = 2
    print("_"*32)
    print()
    for i in range(4):
        print("| %4d  | %4d  | %4d  | %4d  |" % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
        print("_"*32)
        print()
    return tab
        
def random_index_gen():
    global random_index_list
    random_index_list = []
    for x in range(4):
        for y in range(4):
            if tab[x][y] == 0:
                random_index_list.append([x,y])

def random_placement():
    random_index = random.choice(random_index_list)
    tab[random_index[0]][random_index[1]] = 2

def move_horizontal(a,b):

    global counter
    counter = 0
    for x in range(4):
        for rep in range(3):
            for y in range(3):
                if tab[x][y+a] == 0 and tab[x][y+b] != 0:
                    tab[x][y+a] = tab[x][y+b]
                    tab[x][y+b] = 0
                    counter += 1

def move_horizontal_after_addition(a,b):

    for x in range(4):
        for y in range(3):
            if tab[x][y+a] == 0 and tab[x][y+b] != 0:
                tab[x][y+a] = tab[x][y+b]
                tab[x][y+b] = 0


def move_vertical(up,down):

    global counter
    counter = 0
    for y in range(4):
        for rep in range(3):
            for x in range(3):
                if tab[x+up][y] == 0 and tab[x+down][y] != 0:
                    tab[x+up][y] = tab[x+down][y]
                    tab[x+down][y] = 0
                    counter += 1

def move_vertical_after_addition(up,down):

    for y in range(4):
        for x in range(3):
            if tab[x+up][y] == 0 and tab[x+down][y] != 0:
                tab[x+up][y] = tab[x+down][y]
                tab[x+down][y] = 0


def add_left():
    for x in range(4):
        for y in range(3):
            if tab[x][y] == tab[x][y+1]:
                tab[x][y+1] *= 2
                tab[x][y] = 0

def add_right():
    for x in range(4):
        for y in reversed(range(3)):
            if tab[x][y] == tab[x][y+1]:
                tab[x][y+1] *= 2
                tab[x][y] = 0

def add_up():
    for y in range(4):
        for x in range(3):
            if tab[x+1][y] == tab[x][y]:
                tab[x][y] *= 2
                tab[x+1][y] = 0

def add_down():
    for y in range(4):
        for x in reversed(range(3)):
            if tab[x+1][y] == tab[x][y]:
                tab[x][y] *= 2
                tab[x+1][y] = 0
                

def game_over():
    if fin == 0 and counter == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print ("GAME OVER")

def start_menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    columns = shutil.get_terminal_size().columns
    print("\033[1;32;45m \n"*5)
    print("\033[1;32;45m 1.Start game".center(columns))
    print("\033[1;32;45m 2.Goal".center(columns))
    print("\033[1;32;45m 3.Quit".center(columns))
   
    
    userinput = input()
    if userinput == "1":
        main()
    if userinput == "2":
        print("reach as many points as you can with move and merge the same numbers")
    if userinput == "3":
        exit()


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    tab_start()

    while True:
        move = input("Please enter direction!:  ")
        os.system('cls' if os.name == 'nt' else 'clear')

        if move == "a":
            move_horizontal(0,1)
            add_left()
            move_horizontal_after_addition(0,1)
            random_index_gen()
            if counter != 0:
                random_placement()
        
        
        elif move == "d":
            move_horizontal(1,0)
            add_right()
            move_horizontal_after_addition(1,0)
            random_index_gen()
            if counter != 0:
                random_placement()
    

        elif move == "w":
            move_vertical(0,1)
            add_up()
            move_vertical_after_addition(0,1)
            random_index_gen()
            if counter != 0:
                random_placement()
    

        elif move == "s":
            move_vertical(1,0)
            add_down()
            move_vertical_after_addition(1,0)
            random_index_gen()
            if counter != 0:
                random_placement()
    
        
        elif move == "x":
            exit()
    

        print()
        print("random_list: ", len(random_index_list))
        print()
        print()
        for i in range(4):
            print("  %4d    %4d    %4d    %4d   " % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
            print()
            print()

start_menu()