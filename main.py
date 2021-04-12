alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def caesar(text,shift,derection):
  if derection == "decode":
    shift += -1
  cypher = ""
  for letter in text:
    if letter in alphabet:
      position = alphabet.index(letter)
      new_position = position + shift
      if new_position >= len(alphabet):
        new_position -= len(alphabet)
      cypher += alphabet[new_position]
    else :
      cypher += letter
  return cypher

status = False
while not status:
  derection = input("derection(encode/decode): ")
  text = input("text: ")
  shift = int(input("shift: "))
  if shift >= 26:
    shift %= 26
  print(derection, ":" ,caesar(text,shift,derection))
  restart = input("restart(yes/no):")
  if restart == "no":
    status = True


      

