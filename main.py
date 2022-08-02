import sys, os, random
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
specialchars = [" ", ".", "!", "?", ",", "-", ":"]
store = []
randnum = random.randint(0, 35)
chars = randnum-1
forward_and_back = False

def print_quickly(char):
      sys.stdout.write(char)

while True:
  print('type a your message. if finished type "done".')
  message = input(">")
  chars += len(message)
  while chars > 36:
    chars -= 36
  
  for c in range(len(message)):
    chars+=1
    for i in range(36): #repeats 36 times b/c there are 36 things in alphabet
      if message[c] == alphabet[i]: #checks if character in message is in alphabet. if it does it will ether add that letter plus or minus chars to store. otherwise it will send it to special chars to see if it is in there. if not it will not not add to store.
        if forward_and_back == True:
          store.append(alphabet[((i-chars) % 36)])#goes backwards from i to c. so if i was 2 and c was 1 it would go back to 1 and result in a b/c b back 1 is a 
          forward_and_back = False
          break
        else:
          store.append(alphabet[((i+chars) % 36)])#opposite of above
          forward_and_back = True
          break
    for i in range(len(specialchars)): #checks if character is in special chars. if it is it adds it to store. otherwise it does not change store.
      if message[c] == specialchars[i]:
        store.append(specialchars[i])
        break
  store.insert(0, str(randnum))
  for i in store:
    print_quickly(i)
  
  print("\nwould you like to input another code? (y/n must use lower case)")
  while True:
    again = input(">")
    if again == "y" or again == "n":#if again gets an acceptable awnser it breaks the while true and allows the program to asses the respons
      break
  if again == "y": #resets all the nessisary variables and reruns the code from the top while loop
    os.system("clear")
    store = []
    chars = 0
    forward_and_back = False
  else: #exits the program
    exit()