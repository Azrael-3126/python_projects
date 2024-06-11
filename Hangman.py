stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''
                   
                   
                  

word_list = ['abruptly', 'absurd', 'abyss', 'askew', 'awkward', 'axiom', 'azure', 'bagpipes', 'bandwagon', 'banjo', 'bayou', 'beekeeper', 'bikini', 'blitz', 'blizzard', 
'boggle', 'bookworm', 'boxcar', 'boxful', 'buckaroo', 'buffalo', 'buffoon', 'buxom', 'buzzard', 'buzzing', 'buzzwords', 'caliph', 'cobweb', 'cockiness', 'croquet',
 'crypt', 'curacao', 'cycle', 'daiquiri', 'dirndl', 'disavow', 'dizzying', 'duplex', 'embezzle', 'equip', 'espionage', 'euouae', 'exodus', 'faking', 'fishhook', 'fixable', 
 'fjord', 'flapjack', 'fluffiness', 'flyby', 'foxglove', 'frazzled', 'frizzled', 'fuchsia', 'funny', 'gabby', 'galvanize', 'gazebo', 'giaour', 'gizmo', 'glowworm', 
 'glyph', 'gnarly', 'gnostic', 'gossip', 'grogginess', 'haiku', 'haphazard', 'hyphen', 'iatrogenic', 'icebox', 'injury', 'ivory', 'ivy', 'jackpot', 'jaundice', 'jawbreaker', 
 'jaywalk', 'jazziest', 'jazzy', 'jigsaw', 'jinx', 'jockey', 'jogging', 'joking', 'jovial', 'joyful', 'juicy', 'jukebox', 'jumbo', 'kayak', 'kazoo', 'keyhole', 'khaki', 
 'kilobyte', 'kiosk', 'kiwifruit', 'klutz', 'knapsack', 'larynx', 'lengths', 'lucky', 'luxury', 'lymph', 'matrix', 'microwave', 'mnemonic', 'mystify', 'naphtha', 'nightclub', 
 'nowadays', 'numbskull', 'nymph', 'onyx', 'ovary', 'oxidize', 'oxygen', 'pajama', 'peekaboo', 'phlegm', 'pixel', 'pizazz', 'pneumonia', 'polka', 'pshaw', 'psyche', 
 'puppy', 'puzzling', 'quartz', 'quips', 'quixotic', 'quiz', 'quizzes', 'quorum', 'razzmatazz', 'rhubarb', 'rhythm', 'rickshaw', 'schnapps', 'scratch', 'shaker',
  'snazzy', 'sphinx', 'spritz', 'squawk', 'staff', 'strength', 'strengths', 'stretch', 'stronghold', 'stymied', 'subway', 'swivel', 'syndrome', 'thriftless', 'thumbscrew',
   'topaz', 'transcript', 'transgress', 'transplant', 'triphthong', 'twelfth', 'twelfths', 'unknown', 'unworthy', 'unzip', 'uptown', 'vaporize', 'vixen', 'vodka',
   'vortex', 'voyeurism', 'walkway', 'waltz', 'wave', 'wavy', 'waxy', 'wellspring', 'wheezy', 'whiskey', 'whizzing', 'whomever', 'wimpy', 'witchcraft', 'wizard'
    'woozy', 'wristwatch', 'wyvern', 'yachtsman', 'yippee', 'yoked', 'youthful', 'yummy', 'zephyr', 'zigzag', 'zigzagging', 'zilch', 'zipper', 'zodiac', 'zombie', ]

"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""________________________________________________________The game code starts here________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""
"""_________________________________________________________________________________________________________________________________________________"""

import random




def game():
	chosen_word = random.choice(word_list)
	word_length = len(chosen_word)
	display = []
	for _ in range(word_length):
		display += "_"
	lives = 6
	player_points=0
	
	print(logo)
	
	end_of_game = False
	while not end_of_game:
	
		guess = input("Guess a letter: ").lower()
		if guess in display:
			print(f'Sorry,guess another letter you have already guessed "{guess}".')
		for position in range(word_length):
			letter = chosen_word[position]
        
			if letter == guess:
				display[position] = letter
		if guess not in chosen_word:
			print(f'You have guessed "{guess}" ,which is not in the word, So you lose a life.')
			lives -= 1
			if lives == 0:
				end_of_game = True
				print(f'You lose.The solution to the game is "{chosen_word}" .')
		print(f"{' '.join(display)}") 
 
		if "_" not in display:
			end_of_game = True
			print("You win.")
			player_points+=1
        
		print(stages[lives])
		

game()
gameplay=input("Do you want to play the game again? y/n :")
if gameplay=="y":
	game()
else:
	print(f'Thank you for playing this game. Your highscore in this game is {player_points}.')






























































