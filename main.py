import time, sys, os
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
store = []
chars = 0
forward_and_back = True

def print_quickly(str):
    for char in str:
      time.sleep(0)
      sys.stdout.write(char)
      sys.stdout.flush()

print('type a character. if finished type "done".')
message = input(">")

for c in range(len(message)):
  for i in range(26):
    if message[c] == alphabet[i]:
      if forward_and_back == True:
        store.append(alphabet[((i-chars) % 26)])
        forward_and_back = False
        break
      else:
        store.append(alphabet[((i+chars) % 26)])
        forward_and_back = True
        break
for i in range(store):
  print_quickly(i)
print()