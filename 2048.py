
import random
import os
import shutil
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#DEFINITION ////////////////////////////////////////////////////////////////////////////////////
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def start_menu():
    print (       )
    score = 0
    os.system('cls' if os.name == 'nt' else 'clear')
    columns = shutil.get_terminal_size().columns
    print("\033[1;32;39m \n\033[0m"*5)
    print("\033[1;32;44m 1:Start game\033[0m".center(columns))
    print("\033[1;32;44m 2:Goal\033[0m".center(columns))
    print("\033[1;32;44m 3:Quit\n\033[0m".center(columns))
    print("\033[1;32;44m(Please play it in full screen!)\033[0m".center(columns))
   
    userinput = input()
    if userinput == "1":
        main()
    if userinput == "2":
        goal()
    if userinput == "3":
        exit()


def print_tab():
    print()
    print("Score: ", score)
    print("\n"*3)
    for i in range(4):
        print("                      \033[1;32;33m  %4d    %4d    %4d    %4d   \033[0m" % (tab[i][0],tab[i][1],tab[i][2],tab[i][3]))
        print("\n"*2)


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
    print_tab()
    return tab
    

def goal():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n"*3)
    columns = shutil.get_terminal_size().columns
    print("\033[1;32;45m Reach as many points as you can with move and merge the same numbers!\033[0m".center(columns))
    print("\n")
    print("\033[1;32;45m Move with 'w','a','s','d'\033[0m".center(columns))
    print("\n")
    userinput = input("\033[1;32;45m Press any letter to return to Start Menu or 'x' to exit!  \033[0m")
    if userinput == 'x':
        exit()
    else:
        start_menu()

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
    random_index_list.remove(random_index)


def move_horizontal(right,left):

    global counter
    counter = 0
    for x in range(4):
        for rep in range(3):
            for y in range(3):
                if tab[x][y+right] == 0 and tab[x][y+left] != 0:
                    tab[x][y+right] = tab[x][y+left]
                    tab[x][y+left] = 0
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


def move_vertical_after_addition(a,b):

    for y in range(4):
        for x in range(3):
            if tab[x+a][y] == 0 and tab[x+b][y] != 0:
                tab[x+a][y] = tab[x+b][y]
                tab[x+b][y] = 0


def add_left():
    global score
    global counter_add
    counter_add = 0
    for x in range(4):
        for y in range(3):
            if tab[x][y] == tab[x][y+1]:
                tab[x][y+1] *= 2
                score += tab[x][y+1]
                tab[x][y] = 0
                counter_add += 1


def add_right():
    global score
    global counter_add
    counter_add = 0
    for x in range(4):
        for y in reversed(range(3)):
            if tab[x][y] == tab[x][y+1]:
                tab[x][y+1] *= 2
                score += tab[x][y+1]
                tab[x][y] = 0
                counter_add += 1


def add_up():
    global score
    global counter_add
    counter_add = 0
    for y in range(4):
        for x in range(3):
            if tab[x+1][y] == tab[x][y]:
                tab[x][y] *= 2
                score += tab[x][y]
                tab[x+1][y] = 0
                counter_add += 1


def add_down():
    global score
    global counter_add
    counter_add = 0
    for y in range(4):
        for x in reversed(range(3)):
            if tab[x+1][y] == tab[x][y]:
                tab[x+1][y] *= 2
                score += tab[x][y]
                tab[x][y] = 0

                counter_add += 1

def game_over_check():

    if len(random_index_list) == 0:

        for x in range(4):
            for y in range(3):
                if tab[x][y] == tab[x][y+1]:
                    return False

        for x in range(3):
            for y in range(4):
                if tab[x][y] == tab[x+1][y]:
                    return False
        return True
    return False 

        
def game_over():

    os.system('cls' if os.name == 'nt' else 'clear')
    columns = shutil.get_terminal_size().columns
    print("\033[1;32;45m \n\033[0m"*5)
    print("\033[1;32;45m GAME OVER\033[0m".center(columns))
    print("\033[1;32;45m \n\033[0m"*5)
    print("\033[1;32;45m 1. Start Menü\033[0m".center(columns))
    userinput = input("Press '1' to return to Start Menü, or any button to exit!")
    if userinput == "1":
        start_menu()
    else:
        exit()    


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
   
    tab_start()

    while True:
        move = input("Please enter direction!(or 'x' to return to Start Menu):  ")
        os.system('cls' if os.name == 'nt' else 'clear')

        if move == "a":
            move_horizontal(0,1)
            add_left()
            move_horizontal_after_addition(0,1)
            random_index_gen()
            if counter != 0 or counter_add != 0:
                random_placement()
            if game_over_check() == True:
                game_over()

        elif move == "d":
            move_horizontal(1,0)
            add_right()
            move_horizontal_after_addition(1,0)
            random_index_gen()
            if counter != 0 or counter_add != 0:
                random_placement()
            if game_over_check() == True:
                game_over()

        elif move == "w":
            move_vertical(0,1)
            add_up()
            move_vertical_after_addition(0,1)
            random_index_gen()
            if counter != 0 or counter_add != 0:
                random_placement()
            game_over_check()
            if game_over_check() == True:
                game_over()
    
        elif move == "s":
            move_vertical(1,0)
            add_down()
            move_vertical_after_addition(1,0)
            random_index_gen()
            if counter != 0 or counter_add != 0:
                random_placement()
            game_over_check()
            if game_over_check() == True:
                game_over()
        
        elif move == "x":
            start_menu()
    
        print_tab()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#RUNING \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
score = 0
start_menu()