print("Script to encrypt the way vigenere..!?")


import math

text = str(input("Enter the text >> "))

key = str(input("Enter the key >> "))


if len(text) <= len(key):

  coped_key = key[:len(text)]

else:

  ceil = math.ceil(len(text) / len(key))

  new_key = []

  for i in range (0,ceil):

    for l in key:

      new_key.append(l)

  coped_key = new_key[:len(text)]

def encrypt(txt,key):

  test_list = []

  for (l,k) in zip(txt,key):

    text_position = ord(l)  

    key_position = ord(k)

    new_letter = chr(text_position + key_position)

    test_list.append(new_letter)


  t = ''.join(test_list)


  print(t)

encrypt(text,coped_key)



