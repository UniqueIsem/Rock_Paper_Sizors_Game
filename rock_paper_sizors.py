import random

def main():
    options = ['rock', 'paper', 'sizors']
    computerChoice = options[random.randint(0, 2)]

    while True:
        welcomeMessage = """
        OPCIONES DEL JUEGO
        1. ROCK
        2. PAPER
        3. SIZORS
        Ctrl + C to Exit the game
        """
        print(welcomeMessage)

        try:
            userChoice = int(input("Select an option between 1 to 3: "))
            while (userChoice != 1) and (userChoice != 2) and (userChoice != 3):
                userChoice = int(input("Select an option between 1 to 3: "))

            print(gameLogic(userChoice=userChoice, computerChoice=computerChoice, options=options))

        except ValueError:
            print("ERROR -> You can ONLY select an integer option between 1 to 3.")

def gameLogic(userChoice, computerChoice, options):
    tie = 'ITS A TIE!'
    win = 'YOU WIN :D'
    lose = 'YOU LOSE :('
    rock = 'ROCK'
    paper = 'PAPER'
    sizors = 'SIZORS'

    if userChoice == 1:
        userChoice = rock
        print(f'YOU: {userChoice} VS PC: {computerChoice}')

        if computerChoice == options[0]:
            return tie
        elif computerChoice == options[1]:
            return lose
        elif computerChoice == options[2]:
            return win
        
    elif userChoice == 2:
        userChoice = paper
        print(f'YOU: {userChoice} VS PC: {computerChoice}')

        if computerChoice == options[0]:
            return win
        elif computerChoice == options[1]:
            return tie
        elif computerChoice == options[2]:
            return lose
        
    elif userChoice == 3:
        userChoice = sizors
        print(f'YOU: {userChoice} VS PC: {computerChoice}')

        if computerChoice == options[0]:
            return lose
        elif computerChoice == options[1]:
            return win
        elif computerChoice == options[2]:
            return tie

if __name__ == '__main__':
    main()