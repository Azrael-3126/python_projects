import random
logo = """
 _______               ___.                                                      .__                                               
 \      \  __ __  _____\_ |__   ___________     ____  __ __   ____   ______ _____|__| ____    ____      _________    _____   ____  
 /   |   \|  |  \/     \| __ \_/ __ \_  __ \   / ___\|  |  \_/ __ \ /  ___//  ___/  |/    \  / ___\    / ___\__  \  /     \_/ __ \ 
/    |    \  |  /  Y Y  \ \_\ \  ___/|  | \/  / /_/  >  |  /\  ___/ \___ \ \___ \|  |   |  \/ /_/  >  / /_/  > __ \|  Y Y  \  ___/ 
\____|__  /____/|__|_|  /___  /\___  >__|     \___  /|____/  \___  >____  >____  >__|___|  /\___  /   \___  (____  /__|_|  /\___  >
        \/            \/    \/     \/        /_____/             \/     \/     \/        \//_____/   /_____/     \/      \/     \/  """


def check_number(number,real_number):
  if number > real_number:
    print("Too high")
  elif number < real_number:
    print("Too low")
  else:
    print(f"That's is correct. The answer is {real_number} !")


print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("choose a difficulty level - type 'easy' or 'hard' : ")
if level == "easy":
  attempts = 10
  print(f"You have {attempts} attempts to guess the number.")
else:
  attempts = 5
  print(f"You have {attempts} attempts to guess the number.")



real_number = random.randint(1,100)
number = 0

while number != real_number:
  number = int(input ("Please make a guess : "))
  check_number(number,real_number)
  attempts -= 1
  print(f"You have {attempts} attempts left .")
  if attempts == 0:
    print(f"You have run out of guesses. You lose! The answer was {real_number}")
    break
