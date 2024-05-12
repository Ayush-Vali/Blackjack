import random


def comp_game():
    if calculate_card(cp_card) < 17:
        c3 = random.choice(compcards)
        cp_card.append(c3)
        comp_game()
    else:
        print(f"Computer cards: {cp_card}")
        print(f"Computer cards total sum: {calculate_card(cp_card)}")


def play_game():
    print(f"Player cards: {pl_card}")
    print(f"Player cards total sum: {calculate_card(pl_card)}")

    us2 = input("Do you want to deal the cards again?Type 'y' or 'n': ")
    if us2 == "y":

        uniplaycard(us2)

    else:
        userscore = calculate_card(pl_card)
        compscore = calculate_card(cp_card)
        print(compare(userscore, compscore))


def uniplaycard(useropt):
    if useropt == "y":

        n3 = random.choice(playcards)
        pl_card.append(n3)
        print(f"Your cards: {pl_card}")
        print(f"Player cards total sum: {calculate_card(pl_card)}")

        us3 = input("Want to go for next card: y or n ")
        if us3 == "y":
            playcards.remove(
                n3)  #iteration unknown:remove existing the card from list
            uniplaycard(us3)
        else:
            userscore = calculate_card(pl_card)
            compscore = calculate_card(cp_card)
            print(compare(userscore, compscore))
    else:
        pass


#sum and compare has many conditions so needed to make it in function
def calculate_card(card):
    if sum(card) == 21 and len(card) == 2:
        return 0
    if 11 in card and sum(card) > 21:
        card.remove(11)
        card.append(1)
        pass

    return sum(card)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "You lose"


begin = True
while begin:
    start = input("Do you want to play the game? Type 'y' or 'n': ")

    compcards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    playcards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    pl_card = []
    cp_card = []

    n1 = random.choice(playcards)
    c1 = random.choice(compcards)
    #first time remove existing card from the list
    playcards.remove(n1)
    compcards.remove(c1)

    n2 = random.choice(playcards)
    c2 = random.choice(compcards)
    pl_card = pl_card + [n1, n2]
    cp_card = cp_card + [c1, c2]

    #second time remove existing card from the list so in function directly choose new card
    playcards.remove(n2)
    compcards.remove(c2)

    if start == "y":
        comp_game()
        play_game()
