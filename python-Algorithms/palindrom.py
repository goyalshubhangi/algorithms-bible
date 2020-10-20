
def palindrome2(word):
    reversed_word = word[::-1]

    if reversed_word == word:
        return True
    return False

def palindrome(word):
    reversed_letters = []

    for letter in word:
            reversed_letters.insert(0,letter)
    
    reversed_word = ''.join(reversed_letters)

    if reversed_word == word:
        return True
    return False

if __name__ == '__main__':
  word = str(input('Type a word my valedor:' ))

  result = palindrome2(word)
  
  if result is True:
      print('{} is a palindrome.'.format(word))
  else:
      print('{} is not a palindrome.'.format(word))