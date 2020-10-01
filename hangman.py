TRIES = 10
OFFER_NEXT_GAME = 'Would you like to have another try? (y/n)\n'
GAME_WON_PHRASE = 'Congratulations!'
GAME_LOST_PHRASE = 'GAME OVER'
LETTERS_LEFT = 'Letters left:'
INPUT_PROMPT = 'Guess a letter:\n'
INVALID_INPUT = 'Invalid input, try again'
REMAINING_TRIES = 'Tries left:'

word_list = ['COLLECTION', 'APPLE', 'LIBRARY', 'NINJA']
word_list2 = ['ROOM', 'SUPERIOR', 'PLANET', 'BOULDER']
word_list3 = ['LASAGNA', 'BEAVER', 'BATHROOM', 'EMPIRE']

def initialize(word_list):
    for word in word_list:
                alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
                letters = ''
                tries = len(word)
                print('\nGuess the word:\n')
                printword(word, letters)
                while tries > 0:
                        print('\nYou have ' + str(tries) + ' tries left')
                        char = input('\n'+ alphabet + ': ')
                        char = char.upper()
                        if len(char) > 1:
                                if char == word:
                                        letters = char
                                else:
                                        tries = 1
                        elif char in word:
                                letters += char
                                alphabet = alphabet.replace(char, '')
                        printword(word, letters)
                        if allin(word, letters):
                                print('\n\n******************************** \n')
                                print('Correct! The word is ' + word + '\n')
                                print('\n******************************** \n')
                                break
                        tries -= 1
                if tries == 0:
                        print('\nSorry, you lose.\n')
                        print('The word was ' + word)
                        return False

def allin(word, letters):
	return set(word) == set(letters)

def printword(word, letters):
	print()
	for char in word:
		if char in letters:
			print(char, end=' ')
		else:
			print('_', end=' ')
	print()

def play_game(play, word_list):
        print('\nRound 1')
        if initialize(word_list) == False:
                print('\nBetter luck next time.\n')
                return False
        print('Round 2')
        if initialize(word_list2) == False:
                print('\nBetter luck next time.\n')
                return False
        print('Final Round!')
        if initialize(word_list3) == False:
                print('\nBetter luck next time.\n')
                return False
        print('\nCONGRATULATIONS!')

play = 'Y'
while play == 'Y':
        for wl in [word_list, word_list2, word_list3]:
                if play_game(play, wl) == False:
                        break
        play = input('Try again?(Y/N)\n')
        play = play.upper()
