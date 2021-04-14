import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user_cards = []
computer_cards = []
computer_cards_hidden = []

def draw_card(cards_on_hand):
  cards_on_hand.append(random.choice(cards))
def computer_turn():
  if sum(computer_cards) < 15:
    draw_card(computer_cards)
    computer_cards_hidden.append("?")
    print("Cards on hand of computer: ",computer_cards_hidden)
def drawing_began():
  draw_card(user_cards)
  draw_card(computer_cards)
  draw_card(user_cards)
  draw_card(computer_cards)
  draw_card(computer_cards_hidden)
  computer_cards_hidden.append("?")
  print("My hand: ",user_cards)
  print("Cards on hand of computer: ",computer_cards_hidden)
def A_card_point_checker(cards_on_hand):
  for index in range(0, len(cards_on_hand)):
    if cards_on_hand[index] == 11 and sum(cards_on_hand) > 21:
      cards_on_hand[index] = 1
def compare_point():
  A_card_point_checker(user_cards)
  A_card_point_checker(computer_cards)
  if sum(user_cards) > sum(computer_cards) or sum(computer_cards) > 21:
    print("Cards on hand of computer: ",computer_cards)
    print("Win")
  elif sum(user_cards) < sum(computer_cards) or sum(user_cards) > 21:
    print("Cards on hand of computer: ",computer_cards)
    print("Lose")
  else :
    print("Cards on hand of computer: ",computer_cards)
    print("Draw")
    
drawing_began()

status = False
while not status:
  con = input("U want to draw more card(y/n): ")
  if con == "y":
    draw_card(user_cards)
    print("My hand: ",user_cards)
    if sum(user_cards) > 21:
      print("U lose")
      break
    else:
      computer_turn()
  elif con == "n":
    compare_point()
    status = True

  
