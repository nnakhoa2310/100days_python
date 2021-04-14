import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
computer_cards_hidden = []

def draw_card(cards_on_hand):
  cards_on_hand.append(random.choice(cards))
def score(cards_on_hand):
  if 11 in cards_on_hand and sum(cards_on_hand) > 21:
    cards_on_hand.remove(11)
    cards_on_hand.append(1)
  return sum(cards_on_hand)
def computer_turn():
  if score(computer_cards) < 15:
    draw_card(computer_cards)
    computer_cards_hidden.append("?")
    print("Cards on hand of computer: ",computer_cards_hidden)
def compare_point():
  if score(user_cards) > score(computer_cards) or score(computer_cards) > 21:
    print("Cards on hand of computer: ",computer_cards)
    print("Win")
  elif score(user_cards) < score(computer_cards) or score(user_cards) > 21:
    print("Cards on hand of computer: ",computer_cards)
    print("Lose")
  else :
    print("Cards on hand of computer: ",computer_cards)
    print("Draw")
    
def start_game():
  ##draw 2 card
  for i in range(2):
    draw_card(user_cards)
    draw_card(computer_cards) 
  draw_card(computer_cards_hidden)
  computer_cards_hidden.append("?")
  print("My hand: ",user_cards,"score:",score(user_cards))
  print("Cards on hand of computer: ",computer_cards_hidden)
  
  status = False
  while not status:
    con = input("U want to draw more card(y/n): ")
    if con == "y":
      draw_card(user_cards)
      print("My hand: ",user_cards,"score:",score(user_cards))
      if score(user_cards) > 21:
        print("U lose")
        break
      else:
        computer_turn()
    elif con == "n":
      compare_point()
      status = True
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  start_game()
    

  
