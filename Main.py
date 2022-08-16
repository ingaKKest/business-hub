1import random
import os
import time
import collections
import string
# adds colour to words
from termcolor import cprint

# ensures there are no errors


def sample():
    # loops program till user selects valid input
    while True:
        var = input(' ')
        if var not in ['1', '2', '3']:
            print('Please enter a valid input')
        else:
            break
    return var

# ensures there are no errors


def samplev2():
    # loops program till user selects valid input
    while True:
        var = input(' ')
        if var not in ['1', '2']:
            print('Please enter a valid input')
        else:
            break
    return var

# ensures there are no errors


def errorfixer():
    how_much = input(
        "How much money do you want to put down? ")
    valid = 'True'
    # avoids error in the program
    while valid == 'True':
        try:
            how_much = int(how_much)
            valid = 'False'
        except ValueError:
            print("This is not a number")
            how_much = input(
                "How much money do you want to put down? ")
    return how_much

# ensures there are no errors


def errorfixerv2(money, how_much):
    # loops program till user selects valid input
    while True:
        if int(how_much) > money:
            print("you do not have enough money")
        elif int(how_much) < 0:
            print("That is a negative number")
        else:
            break
        return int(how_much)

# ensures there are no errors


def errorfixerv3(how_much):
    valid = 'True'
    # avoids error in the program
    while valid == 'True':
        try:
            how_much = int(how_much)
            valid = 'False'
        except ValueError:
            print("This is not a number")
            how_much = input(
                "How much money do you want to put down? ")

    return how_much

# ensures there are no errors


def errorfixerv4(text):
    how_much = input(text)
    valid = 'True'
    # avoids error in the program
    while valid == 'True':
        try:
            variable = int(how_much)
            valid = 'False'
        except ValueError:
            print("This is not a number")
            how_much = input(
                text)
    return variable


# list of all stocks
stocks = [
    ("JNUG", 4.47, "volatile"),
    ("GOOGL", 1214.27, "stable"),
    ("JDST", 34.00, "volatile"),
    ("KGC", 3.47, "stable"),
    ("NEM", 39.50, "stable"),
    ("LPI", 0.47, "volatile"),
    ("COP", 31.38, "stable"),
    ("FBT", 127.14, "volatile"),
    ("SWN", 2.12, "stable"),
    ("ZBIO", 11.84, "volatile"),
    ("HNDL", 21.89, "volatile"),
    ("AAPL", 277.97, "stable"),
    ("FXTL", 32.84, "volatile"),
    ("NOCT", 31.06, "volatile"),
    ("BRK.A", 289000.00, "stable"),
    ("MSFT", 19.77, "stable")
]

# sets users starting money, inventory, shares, and all stocks
playerMoney = 10000
numbers = ['1', '2', '3', '4', '5', '6', '7', ' 8', '9', '10',
           '11', '12', '13', '14', '15']
inventory = []
sharesList = []
allStocks = []
stocksList = ["JNUG", "GOOGL", "JDST", "KGC", "NEM", "LPI",
              "COP", "FBT", "SWN", "ZBIO", "HNDL", "AAPL",
              "FXTL", "NOCT", "BRK.A", "MSFT"]

year = 2022


# allows the program to access the stock attributes
class StockNames:
    global playerMoney
    # assings stocks with their name, cost and volatilty

    def __init__(self, name, cost, volatility):
        # assings stock with name
        self.name = name
        # gives stock the cost
        self.cost = cost
        # gives stock the volatility
        self.volatility = volatility
        self.displayBuying1 = ('''
    Name:''' + self.name + '''
    Stock Price:''' + str(self.cost) + '''
    Volatility:''' + self.volatility + '''
    ''')
        self.displayBuying = (self.name + ": " + str(self.cost))
    # Used for asking user how mch they want to bet in later parts of program

    def how_much(self):
        # make sure there are no errors
        how_much = errorfixer()
        # loops program till user selects valid input
        while True:
            if how_much < 1:
                print("you cannot enter a negative number")
            else:
                order_value = self.cost * how_much
                break
            return order_value

# allows user to skip a year, causing price to increase / decrease
    def skipAnYear(self):
        # determines if stock will go up or down, 1 meaning up, 2 meaning down
        PlusOrMinus = random.choice([1, 2])
    # if stock is volatile or stable the price will change accordingly
        if self.volatility == "volatile":
            volatilityNumber = 3
        elif self.volatility == "stable":
            volatilityNumber = 1
        change = volatilityNumber * (self.cost / 10)
    # increases stock price
        if PlusOrMinus == 1:
            self.cost += change
            self.cost = round(self.cost, 2)
    # decreases stock price
        elif PlusOrMinus == 2:
            self.cost -= change
            self.cost = round(self.cost, 2)
    # rounds up price so it does not go below 1
        if self.cost < 1:
            self.cost = 1
            # changes stock value in players inventory
        for stock in inventory:
            if self.name == stock[0]:
                stock[1] = self.cost

    # allows user to purchase stock
    def buy(self, order_value):
        global playerMoney
    # minuses stock cost from players money
        accountBalance = playerMoney - order_value
        if accountBalance > 0:
            print("You've successfully bought stock " + self.name)
            playerMoney -= order_value
            inventory_addition = order_value / self.cost
            # adds stock to players inventory
            for i in range(int(inventory_addition)):
                inventory.append(self.name)
        else:
            print("You do not have enough funds for this transaction.")
            input("")
            os.system('clear')

    # adds stock to share list
    # counts how many stocks you have and prints it
    def displayAfterBuying(self):
        # adds shares to inventory
        for i in range(0, len(inventory)):
            if inventory[i] == self.name:
                sharesList.append(inventory[i])
        stockNumbers = len(sharesList)
        print("You have " +
              str(stockNumbers) + " shares of " +
              self.name + ", and they now cost:" +
              str(self.cost))
        sharesList.clear()

    # sells stock
    def sell(self):
        global playerMoney
        sellingShare = input(
            'Which shares would you like to sell? ' +
            '(Use the name of the stock): ')
        if sellingShare in inventory:
            # inventory.remove(sellingShare)
            for stock in allStocks:
                if stock.name == sellingShare:
                    selling = stock.how_much()
                    playerMoney += selling
                    inventory_addition = selling / stock.cost
                    # removes shares from players inventory
                    for i in range(int(inventory_addition)):
                        inventory.remove(sellingShare)

            print(
                "You've successfully sold one of your shares of " +
                sellingShare)
            input("")
            os.system('clear')
        else:
            print("You don't have stock " + sellingShare)
            input("")
            os.system('clear')

# main user game


def fullGamestock(year):
    # assings all stock variables
    for i in range(0, 15):
        stock = stocks[i]
        name = stock[0]
        price = stock[1]
        volatility = stock[2]
        # assigns the stock value
        realStock = StockNames(name, price, volatility)
        allStocks.append(realStock)

    # loops program till user selects valid input
    while True:
        global playerMoney
        os.system('clear')
        print("Year: " + str(year))
        print("Money: $" + str(round(playerMoney, 2)))
        question = input('''Would you like to:-
    1. Invest in stocks
    2. Skip an year
    3. See how your stocks are doing
    4. Leave Game
    Choice: ''')

    # allows user to purchase stock
        if question == "1":
            os.system('clear')
            # allows user to find out more information / buy stock
            for i in range(1, 16):
                zeStock = allStocks[i - 1]
        # prints stock info
                print(str(i) + ". " + zeStock.name + ": " + str(zeStock.cost))
                print("")
        # allows user to choose what stock they want to purchase
            print("Type in the number to buy, type in the name to" +
                  " learn more information.")
            # ensures there are no errors if they type the wrong input
            while True:
                choice = input("Choice: ")
        # allows user to purchase stock
                if choice in numbers:
                    numberChoice = int(choice) - 1
                    stockChoice = allStocks[numberChoice]
                    buying = stockChoice.how_much()
                    stockChoice.buy(buying)
                    break
        # allows user to see information about the stock
                elif choice in stocksList:
                    os.system('clear')
                    # if they choose to see more information it appears
                    for stockio in allStocks:
                        if stockio.name == choice:
                            print(stockio.displayBuying1)
                            input('')
                            os.system('clear')
                            break
                else:
                    print("please enter a valid input")

                # skips year and adjusts all prices
        if question == "2":
            # allows stock to change price after a year
            for i in range(0, 15):
                zeStock = allStocks[i]
                zeStock.skipAnYear()
            year += 1
            os.system('clear')

            os.system('clear')

        # allows user to sell and manage stocks
        if question == "3" and len(inventory) != 0:
            # ensures there are no errors
            while True:
                os.system('clear')
                # allows stock to see the display message after stock
                for i in range(0, 15):
                    zeStock = allStocks[i]
                    zeStock.displayAfterBuying()
                    print("")
                question = input("Press E to go back or Press S to sell:")
                if question.lower() == "e":
                    break
                elif question.lower() == "s":
                    zeStock = allStocks[0]
                    zeStock.sell()
                    os.system('clear')
                else:
                    break
        elif question == "3" and len(inventory) == 0:
            print("You have nothing in your inventory.")
            input("")
            os.system('clear')
        if question == '4':
            # loops program till user selects valid input
            while True:
                print("Are you sure you want to leave game?")
                print("Y. Yes")
                print("N. No")
                decision = input(" ")
                if decision not in ['Y', 'N']:
                    print('Please enter a valid input')
                else:
                    break
            break


# Stock Market Game


# allows user to select how many days they want to play for

def amount_of_days():
    print("\n\nIn this game your goal is to buy low" +
          " and sell high for HUGE gains in the stock market\n\n")
    # ensures there are no errors
    while True:
        how_many_days = "How many days would you like to play the " + "stock market for?: "
        days = errorfixerv4(how_many_days)

        if days < 1:
            print("you cannot enter a negative number")
        else:
            break
    return days


# clears the text on screen to make it easier to read
def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


# allows user to play full game
def FullGameStockEASY():
    days = amount_of_days()
    clearConsole()
    i = 0
    average = 0
    avg = 0
    times = 0
    share = 0
    bal = 1000
# while days are more tha zero the game will continue
    while i < int(days):
        left = int(days) - i
        print("\n===============================" +
              "============================================" +
              "=================\n")
        print("Days Left: " + str(left), end='   -   ')
        print("Balance: $" + str(bal), end='   -   ')
        print("Shares: " + str(share), end='   -   ')
        print("Average Buy Cost: $" + str(avg))
        print(" \n")
        # randomly selects the price each day
        stock = random.randint(1, 1100)
        print("Today's stock price: $" + str(stock))
        i = i + 1
        # allows user to buy the max amount
        maxbuy = (bal / stock)
        maxbuy = int(maxbuy)
        # allows user to choose what they want to do
        invest = str(input(
            "\nWhat would you like to do?    Buy(1)?    Sell(2)?" +
            " Or wait to the next day(3)?\n\nYour Choice?: "))
        print("\n----------")
        # allows user to purchase shares
        if(invest == "1"):
            print(
                "The max amount of shares you can buy is: " +
                str(maxbuy) +
                "\n----------")
            print("If you want to buy max shares type '12345'.\n-")
            # ensures there aree no errors
            while True:
                shares_bought = "How many shares would you like to buy?: "
                amount = errorfixerv4(shares_bought)

                if amount < 0:
                    print("You cannot enter a negative number")
                else:
                    break
            print("----------")
            if(str(amount) == "12345"):
                amount = maxbuy
            elif(amount > maxbuy):
                print(
                    "----------\n you do not have enough money so " +
                    "I'm buying the max amount you can afford instead.")
                amount = maxbuy
                time.sleep(1.75)
                # calulates users balance
            bal = (bal - amount * stock)
            share = (share + amount)
            if(maxbuy > 0):
                if(amount > 0):
                    if(amount == 12345):
                        times = times + 1
                        average = average + stock
                    else:
                        times = times + 1
                        average = average + stock
    # allows user to sell their stock
        elif(invest == "2"):
            print(
                "The max amount of shares you can sell is " +
                str(share) +
                ".\n----------")
            print("If you would like to sell all of your shares type " +
                  "'12345' else...")
            # ensures there are no errors
            while True:
                sellings = "How many shares would you like to sell?: "
                sell = errorfixerv4(sellings)

                if sell < 0:
                    print("You cannot enter a negative number")
                else:
                    break

            if(str(sell) == "12345"):
                sell = share
                bal = bal + sell * stock
                share = share - sell
            elif(sell > share):
                print("----------\n\n You do not have enough " +
                      " shares\n\n----------")
                time.sleep(1.5)
            else:
                bal = bal + sell * stock
                share = share - sell
        else:
            print("You skipped the day... Don't you feel USELESS sometimes?!")
            time.sleep(0.675)
        if(times > 0):
            avg = average / times
            avg = int(avg)
        clearConsole()
        # once user runs out of days they are able to convert without having to
        # sell
    if(share > 0):
        lprice = random.randint(50, 1050)
        print("Last day's stock price: " + str(lprice) + "\n----------")
        convert = int(input(
            "Would you like me to convert your shares to dollars" +
            " using the last share price? Yes(1) No(2): "))
        # once user finishes they are able to see how they did
        if(convert == 1):
            bal = (bal + share * int(lprice))
            share = 0

    print("----------\n\nYou have 0 days left to make money. " +
          "Lets see how you did!\n\n----------")

    print(
        "\nAfter " +
        str(days) +
        " days you have made $" +
        str(bal) +
        " dollars.\n\n-")
    print("\nYou own " + str(share) + " shares.\n\n----------")
    if(bal < 1000):
        print("\n\nYOU LOST THE MONEY!!!")
    elif(bal == 1000):
        print("\n\nAre you sure that you played the game at all?!?!?!")
    elif(bal < 1000000):
        print(
            "\n\nPretty good but I think you can do better, maybe " +
            "if you play for longer?!")
    elif(bal < 1000000000):
        print("\n\nWOW, very good indeed")
    elif(bal < 1000000000000):
        print("\n\nCan you teach me your ways? Because that was amazing!")
    else:
        print("\n\nVERY VERY Impressive!!! Now just do that in the real " +
              "world and you will be set")

# end of stock easy program


# start of business wordle program

def getGuess(clues, guessWords):
    # ensures that the user does not type an incorrect input
    while True:
        print()
        guess = input("Enter your guess: ").lower()
        # checks if word is in the alphabet
        if len(guess) != 5 or not guess.isalpha():
            print("Guess must be 5 letters")
            continue
        elif guess not in guessWords:
            print("Word not in dictionary")
            continue

        return guess

# cahnges colour accordinglign depending on guess


def colorResult(guess, word):
    guessColors = ['on_grey'] * 5  # default to grey

    # find greens
    for i in range(len(word)):
        if word[i] == guess[i]:
            guessColors[i] = 'on_green'

    # find yellows
    left = [x for x in range(len(word)) if guessColors[x] != 'on_green']
    # finds yellows
    for wordIndex in left:
        for guessIndex in left:
            w = word[wordIndex]
            g = guess[guessIndex]
            if w == g and guessColors[guessIndex] == 'on_grey':
                guessColors[guessIndex] = 'on_yellow'
                break

    # print guess
    for i, x in enumerate(guess):
        cprint(x.upper(), 'white', guessColors[i], attrs=['bold'], end=' ')
    print()

    return guessColors

# adjusts keyboard display


def printLetterBank(targetWord, guesses, guessColorsList):
    keyboard = list("qwertyuiopasdfghjklzxcvbnm")
    keyColors = {}
    # changes colour of alphabet letters
    for k in keyboard:
        keyColors[k] = 'on_grey'  # default color if it hasn't been guessed

    # determine colours for keyboard
    for letter in keyboard:
        # checks letters
        for g in range(len(guesses)):
            guess = guesses[g]
            guessColors = guessColorsList[g]
            # finds a matching letter
            for guessLetterInd in range(len(guess)):
                if guess[guessLetterInd] == letter:  # found a matching letter
                    guessColor = guessColors[guessLetterInd]
                    if guessColor == 'on_green':
                        keyColors[letter] = 'on_green'
                    elif guessColor == 'on_yellow':
                        if keyColors[letter] != 'on_green':
                            keyColors[letter] = 'on_yellow'
                    elif guessColor == 'on_grey':
                        g = keyColors[letter]
                        if g != 'on_green' and g != 'on_yellow':
                            # used as a key, not an actual color
                            keyColors[letter] = 'wrong'

    # print keyboard
    print()
    # checks all guesses and darkens if it is wrong
    for k in keyboard:
        if keyColors[k] == 'wrong':  # a wrong guess will be dark
            cprint(
                k.upper(),
                'white',
                'on_grey',
                attrs=[
                    'bold',
                    'dark'],
                end=' ')
        else:
            cprint(k.upper(), 'white', keyColors[k], attrs=['bold'], end=' ')
        if k == 'p':
            print('\n ', end='')
        elif k == 'l':
            print('\n   ', end='')
    print()

# allwos user to play main game


def mainwordlegame():
    os.system('clear')
    print("Welcome to Business Wordle!")
    print("improve your business vocabulary")

    # read in word banks
    with open('business.txt', 'r') as FILE:
        # opens text file
        words = [word.rstrip() for word in FILE]
    choices = [w for w in words if len(w) == 5]
    with open('dictionary.txt', 'r') as FILE:
        words = [word.rstrip() for word in FILE]
    guessWords = words + choices

    # randomly choose a target word
    word = random.choice(choices)
    guesses = []

    print("Enter anything to start the game.")
    inp = input()

    # keep track of clues for hard mode
    clues = ['on_grey'] * 5

    # start game
    print("\nYou have 6 tries to guess the 5-letter word.")
    # allows user to guess word
    while True:
        # prompt player for guess
        guess = getGuess(clues, guessWords)
        guesses.append(guess)

        # print guess results
        os.system('clear')
        guessColorsList = []
        # prints result from guess
        for g in guesses:
            guessColors = colorResult(g, word)
            guessColorsList.append(guessColors)

            # update clues
            for i in range(len(guessColors)):
                if guessColors[i] == 'on_green':
                    clues[i] = 'on_green'
                elif guessColors[i] == 'on_yellow':
                    try:
                        letterIndex = word.index(guess[i])
                    except ValueError:
                        letterIndex = -1
                    if letterIndex != -1 and clues[letterIndex] != 'on_green':
                        clues[letterIndex] = 'on_yellow'

        # print keyboard
        printLetterBank(word, guesses, guessColorsList)

        # check for win/lose
        if guess == word:
            print('\nYou Win!')
            break
        elif len(guesses) == 6:
            print("\nSorry, you ran out of guesses.")
            print("The word was:", word.upper())
            break

# deals cards


def dealerTurn(start, playerTotal):
    total = start

    # Dealer will continue to hit until their total is > 21 OR they have beat
    # the player
    while total <= playerTotal and total <= 21:
        card = getCard()
        total = total + card
        print("Dealer gets a " + str(card) + ". He now shows " + str(total))

    return total

# gets user bet


def getBet(max):
    # ensures there are no errors
    while True:
        bet = errorfixer()
        # Ensure the player doesn't bet more than they have.
        if bet <= 0 or bet > max:
            print("Enter an amount between $1 and $" + str(max))
        else:
            break

    return bet

# gets user card


def getCard():
    deal = int(random.random() * 13) + 1
    if deal > 10:
        # If the card is above 10 (Jack, Queen, King), the function returns 10.
        value = 10
    else:
        value = deal

    return value

# introduces the user


def introduction():
    print("Welcome to BlackJack")

# allows user to hit or stand


def playerTurn(start):
    total = start

    # Loop until the player selects "s" to stand or they bust.
    while True:    # This simulates a Do Loop
        print("Hit or stand?  (h/s)")
        choice = input()
        if choice == "h":
            card = getCard()
            print("You are dealed a " + str(card))
            total = total + card
        print("You show: " + str(total))
        if not(total <= 21 and choice != "s"):
            break  # Exit loop

    return total

# allows user to win


def playerWon(playerTotal, dealerTotal):
    # This logic can be simplied to a single expression. However,
    # let's keep it readable.
    if playerTotal > dealerTotal:
        if playerTotal <= 21:
            won = True
        else:
            won = False
    else:
        if dealerTotal <= 21:
            won = False
        else:
            won = True

    return won


# allows user to play game
def blackjackmain():
    cash = 1000
    introduction()
    # loops program till money is below 0
    while cash > 0:
        print("You now have $" + str(cash) + ". Enter your bet.")
        bet = getBet(cash)
        playerCards = getCard() + getCard()
        dealerCards = getCard()
        print("Dealer gives you two cards...")
        print("You show: " + str(playerCards))
        print("Dealer shows: " + str(dealerCards))
        playerCards = playerTurn(playerCards)
        if playerCards <= 21:
            dealerCards = dealerTurn(dealerCards, playerCards)
        if playerWon(playerCards, dealerCards):
            print("YOU WIN!")
            cash = cash + bet
        else:
            print("YOU LOSE!")
            cash = cash - bet
    print("Game over!")

# allows user to play on the slot machines

# allows user to play the slot machine


def slotmachine():
    print("Welcome to the Slot Machnine")
    money = 1000
    # allows user to play while money is greater than 0
    while money > 0:
        print("You have $ {} left".format(money))
        print("")

        how_much = input(
            "How much money do you want to put down? (Enter L to leave game) ")
        if how_much == 'L':
            break
        else:
            how_much = errorfixerv3(how_much)
            errorfixerv2(money, how_much)
            money = money - how_much
            digits = string.digits
            letter_digit_list = list(string.digits + string.ascii_letters)
# shuffle random source of letters and digits
            random.shuffle(letter_digit_list)
# now create random string of length 6 which is a combination
# of numbers and string
# next concatenate it with sample_str
            sample_str = ''.join(
                (random.choice(letter_digit_list) for i in range(3)))
            aList = list(sample_str)
            random.shuffle(aList)

            final_str = ''.join(aList)
            print("Slot Machine:", final_str)

            d = collections.defaultdict(int)

            for c in final_str:
                d[c] += 1
        # finds if the final str has matching letters
        for c in sorted(d, key=d.get, reverse=True):
            if d[c] == 2:
                money = how_much * 10000 + money
            elif d[c] == 3:
                money = how_much * 1000000 + money

# allows user to play roulete


def roluette():
    print("Welcome to the Roulette")
    money = 1000
    # allows user to play while money greater than 0
    while money > 0:
        print("You have $ {} left".format(money))
        print("")
        how_much = errorfixer()
        errorfixerv2(money, how_much)
        money = money - how_much
        # loops program till user selects valid input
        while True:
            blue = input("Red or Black? ")
            if blue == 'red':
                if random.random() < 0.5:
                    money = roluettecalculations(how_much, money)
                    break
                else:
                    print("it was Black")
                    break
            elif blue == 'black':
                if random.random() < 0.5:
                    money = roluettecalculations(how_much, money)
                    break
                else:
                    print("it was Red")
                    break
            else:
                print("please type red or black")


def roluettecalculations(how_much, money):
    money = money + how_much * (2)
    return money


# allows user to play main game
def mainhub():
    # puts code in infinite loop
    while True:
        print(" ")
        print(" ")
        print("\033[1m" + "BUSINESS" + "\033[93m " + "HUB" + "\033[0m")
        print(" ")
        print(" ")
        print("What would you like to do?")
        print("1. Stock Simulator")
        print("2. Business Wordle")
        print("3. Gambling")
        # ensures that program does not have errors
        game = sample()
        if game == '1':
            print('Would you Like to play :')
            print("1. Easy / Arcade Mode")
            print("2. Advanced / Realistic")
            stock_sim = samplev2()
            if stock_sim == '1':
                FullGameStockEASY()
            elif stock_sim == '2':
                fullGamestock(year)
        elif game == '2':
            mainwordlegame()
        elif game == '3':
            print('Would you Like to play :')
            print("1. BlackJack")
            print("2. Slot Machine")
            print("3. Roulette")
            gamble_sim = sample()
            if gamble_sim == '1':
                clearConsole()
                blackjackmain()
            elif gamble_sim == '2':
                clearConsole()
                slotmachine()
            elif gamble_sim == '3':
                clearConsole()
                roluette()


mainhub()
