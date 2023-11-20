from Crypto.Util.number import *
from cards import Heart, Spade, Club, Diamond
from secret import flag

def choose_card(num):
    x = (num>>5)%4
    if x == 0:
        return (Heart[(num>>6)%13]), 'Heart'
    if x%4 == 1:
        return (Spade[(num>>6)%13]), 'Spade'
    if x%4 == 2:
        return (Diamond[(num>>6)%13]), 'Diamond'
    else:
        return (Club[(num>>6)%13]), 'Club'

def GAME():
    banner = ''' 
 ####    ##   #####  #####      ####    ##   #    # ###### 
#    #  #  #  #    # #    #    #    #  #  #  ##  ## #      
#      #    # #    # #    #    #      #    # # ## # #####  
#      ###### #####  #    #    #  ### ###### #    # #      
#    # #    # #   #  #    #    #    # #    # #    # #      
 ####  #    # #    # #####      ####  #    # #    # ######
'''
    print(banner)

    meum = '''option:
    1: start game
    2: get hint
    3: exit
    '''
    print(meum)

    while True:
        print('input your option: ', end='')
        your_input = input()

        if your_input == '1':
            n = getPrime(36)
            m = getPrime(16)
            c = getPrime(16)
            seed = getPrime(36)
            out = seed
            round = 0
            score = 0
            res = []
            while True:
                round += 1
                res = []
                print(f'round:{round}')
                print(f'score:{score}')
                for i in range (3):
                    out = (out*m+c)%n
                    res.append(out)
                if round == 1:
                    for i in res:
                        card, suit = choose_card(i)
                        print(card)
                elif round==2 or round==3:  #gift
                    for i in res:
                        card, suit = choose_card(i)
                        print(card)
                    print(f'gift: {res}')
                else:
                    cards = []
                    suits = []
                    for i in range(len(res)):
                        card, suit = choose_card(res[i])
                        cards.append(card)
                        suits.append(suit)
                    print("Give me your guess: (example: Heart_1 Club_2 Diamond_3)")  
                    try:
                        g_1, g_2, g_3 = input().split()
                        g_1, g_2, g_3 = g_1.split('_'), g_2.split('_'), g_3.split('_')
                    except ValueError:
                        print("Please enter in the correct format.")
                        return
                    if (g_1[0] == suits[0] and g_1[1] == cards[0][15]) and (g_2[0] == suits[1] and g_2[1] == cards[1][15]) and (g_3[0] == suits[2] and g_3[1] == cards[2][15]):
                        for i in cards:
                            print(i)
                        print("Congratulations! You matched the cards!")
                        score += 1
                    else:
                        for i in cards:
                            print(i)
                        print("Try again!")
                if score == 50:
                    print('The flag is your reward!')
                    print(flag)
                    return
                else:
                    continue
        
        if your_input == '2':
            print("Have you ever heard of LCG?")

        if your_input == '3':
            break

if __name__ == '__main__':
    GAME()