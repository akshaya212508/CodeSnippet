import random

# ----------------------------- Deck Setup -----------------------------
def createdeck():
    suits = ['diamonds', 'spades', 'clubs', 'hearts']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    [rank + '_' + 'of' + '_' + suit for suit in suits for rank in ranks]

def sortpile(deck):
    diamond_pile = [card for card in deck if 'diamonds' in card]
    normal_pile = [card for card in deck if 'diamonds' not in card]
    return diamond_pile, normal_pile

# ------------------------- Player Card Assignment -------------------------
def player_2(normal_pile):
    suits = ['spades', 'clubs', 'hearts']
    chosen_suits = random.sample(suits, 2)
    playing_cards = [card for card in normal_pile if any(suit in card for suit in chosen_suits)]
    suit1 = [card for card in playing_cards if chosen_suits[0] in card]
    suit2 = [card for card in playing_cards if chosen_suits[1] in card]
    return {"human": suit1, "computer": suit2}

# ------------------------- Value Setup -------------------------
values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7,
    '8': 8, '9': 9, '10': 10, 'jack': 11, 'queen': 12, 'king': 13, 'ace': 14
}

def extract_rank(card):
    return card.split(' ')[0]

# ------------------------- Strategies -------------------------
def strategy_highest(cards):
    return max(cards, key=lambda x: values[extract_rank(x)])

def strategy_lowest(cards):
    return min(cards, key=lambda x: values[extract_rank(x)])

def strategy_random(cards):
    return random.choice(cards)

def strategy_closest_higher(cards, diamond_card):
    diamond_value = values[extract_rank(diamond_card)]
    higher_cards = [c for c in cards if values[extract_rank(c)] > diamond_value]
    if higher_cards:
        return min(higher_cards, key=lambda x: values[extract_rank(x)])
    return min(cards, key=lambda x: abs(values[extract_rank(x)] - diamond_value))

def computer_strategy(cards, diamond_card, round_counter):
    strategies = [strategy_highest, strategy_lowest, strategy_random, strategy_closest_higher]
    current_strategy = strategies[round_counter % len(strategies)]
    if current_strategy == strategy_closest_higher:
        return current_strategy(cards, diamond_card)
    else:        
       return current_strategy(cards)

# ------------------------- Gameplay -------------------------
def initialize_game():
    deck = createdeck()
    random.shuffle(deck)
    diamond_pile, normal_pile = sortpile(deck)
    players = player_2(normal_pile)
    random.shuffle(diamond_pile)

    print("\n--- Game Start! ---")
    return diamond_pile, players


def play_rounds(diamond_pile, players):
    round_counter = 0
    human_score = 0
    computer_score = 0

    while diamond_pile and players['human'] and players['computer']:
        diamond_card = diamond_pile.pop(0)
        print(f"\nDiamond Card: {diamond_card}")

        # Show human cards
        print("Your Cards:")
        for i, card in enumerate(players['human']):
            print(f"{i+1}. {card}")

        # Get human move
        while True:
            try:
                choice = int(input("Choose a card to play (number): ")) - 1
                if 0 <= choice < len(players['human']):
                    human_card = players['human'].pop(choice)
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Enter a valid number.")

        # Computer move
        computer_card = computer_strategy(players['computer'], diamond_card, round_counter)
        players['computer'].remove(computer_card)

        print(f"You played: {human_card}")
        print(f"Computer played: {computer_card}")

        # Evaluate round
        human_val = values[extract_rank(human_card)]
        comp_val = values[extract_rank(computer_card)]
        diamond_val = values[extract_rank(diamond_card)]

        human_diff = abs(human_val - diamond_val)
        comp_diff = abs(comp_val - diamond_val)

        if human_val > comp_val:
            print("You win this round!")
            human_score += diamond_val
        elif comp_val > human_val:
            print("Computer wins this round!")
            computer_score += diamond_val
        else:
            print("It's a tie!")
            human_score += diamond_val / 2
            computer_score += diamond_val / 2

        round_counter += 1

    return human_score, computer_score


def conclude_game(human_score, computer_score):
    print("\n--- Game Over ---")
    print(f"Your Score: {human_score}")
    print(f"Computer Score: {computer_score}")

    if human_score > computer_score:
        print("Congratulations! You win!")
    elif computer_score > human_score:
        print("Computer wins! Better luck next time.")
    else:
        print("It's a draw!")


def play_game():
    diamond_pile, players = initialize_game()
    human_score, computer_score = play_rounds(diamond_pile, players)
    conclude_game(human_score, computer_score)


if __name__ == "__main__":
    play_game()
