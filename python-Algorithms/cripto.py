KEYS = {
    'a': 'w',
    'b': 'E',
    'c': 'x',
    'd': '1',
    'e': 'a',
    'f': 't',
    'g': '0',
    'h': 'C',
    'i': 'b',
    'j': '!',
    'k': 'z',
    'l': '8',
    'm': 'M',
    'n': 'I',
    'o': 'd',
    'p': '.',
    'q': 'U',
    'r': 'Y',
    's': 'i',
    't': '3',
    'u': ',',
    'v': 'J',
    'w': 'N',
    'x': 'f',
    'y': 'm',
    'z': 'W',
    'A': 'G',
    'B': 'S',
    'C': 'j',
    'D': 'n',
    'E': 's',
    'F': 'Q',
    'G': 'o',
    'H': 'e',
    'I': 'u',
    'J': 'g',
    'K': '2',
    'L': '9',
    'M': 'A',
    'N': '5',
    'O': '4',
    'P': '?',
    'Q': 'c',
    'R': 'r',
    'S': 'O',
    'T': 'P',
    'U': 'h',
    'V': '6',
    'W': 'q',
    'X': 'H',
    'Y': 'R',
    'Z': 'l',
    '0': 'k',
    '1': '7',
    '2': 'X',
    '3': 'L',
    '4': 'p',
    '5': 'v',
    '6': 'T',
    '7': 'V',
    '8': 'y',
    '9': 'K',
    '.': 'Z',
    ',': 'D',
    '?': 'F',
    '!': 'B',
    ' ': ' ',
}

def cypher(message):
    words = message.split(' ')
    cypher_message = []

    for word in words:
        cypher_word = ''
        for letter in word:
            cypher_word += KEYS[letter]


        cypher_message.append(cypher_word)

    return ' '.join(cypher_message)

def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher = ''

        for letter in word:
           
           for key,value in KEYS.items():
               if value == letter:
                   decipher += key

        decipher_message.append(decipher)

    return ' '.join(decipher_message)



def run():

    while True:

        command = str(input('''------ * ---------- * -------- * --------- *
        
        Welcome back my valedor to a cripto practice, tell me, what you want 2 do?

        
        A) Cypher a message

        B) Decipher a message

        Any other letter lol) Exit


        
          ''')).upper()

        if command == 'A':
            message = str(input('Please, type your message:'))
            cypher_message = cypher(message)
            print(cypher_message)
        elif command == 'B':
            message = str(input('Please, write your cipher: '))
            decypher_message = decipher(message)
            print(decypher_message)
        else:
            print('Bye my valedor')
            exit()

if __name__ == '__main__':
    print('ENIGMA')
    run()
