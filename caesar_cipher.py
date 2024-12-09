alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def get_new_index(current_index, shift, type):
  if type == 'encode':
    new_index = current_index + shift
    if (new_index < len(alphabet)):
      return new_index
    else:
      return new_index - len(alphabet)
  else:
    return current_index - shift

def valid_letter(letter):
  found = False
  for char in alphabet:
    if (char == letter):
      found = True
      return found
  return found

running = True

while running:
  type = input("Type 'encode' to encrypt; type 'decode' to decrypt\n")
  if type.lower() != 'encode' and type.lower() != 'decode':
    print(f"'{type}' is not an option, please type either 'encode' or 'decode'.")
    continue
  message = input('Type your message:\n')
  while True:
    try:
      shift = int(input('The the shift number:\n'))
      break
    except ValueError:
      print('Please type a valid number.')
  output = ''
  for letter in message:
    if (valid_letter(letter)):
      letter_index = alphabet.index(letter)
      print(letter_index)
      output += alphabet[get_new_index(letter_index, shift, type)]
    else:
      output += letter
  print(f"Here's the {type}d response: {output}")
  while True:
    repeat = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
    if repeat.lower() != 'yes' and repeat.lower() != 'no':
      print(f"'{repeat}' is not an option, please type either 'yes' or 'no'.")
    else:
      break
  if (repeat == 'no'):
    break
