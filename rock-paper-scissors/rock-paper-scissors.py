import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

list = [rock, paper, scissors]

you_choose = int(
    input(
        "What do you choose? Type 0 for Rock, 1 for Paper or 2 for scissors\n")
)

if you_choose >= 3 or you_choose < 0:
    print("You typed an invalid number, You LOSE")
else:
    print(list[you_choose])

    computer_choose = random.randint(0, 2)
    print("Computer Chose:\n" + list[computer_choose])

    if you_choose == 0 and computer_choose == 2:
        print("You WON.")
    elif you_choose == 2 and computer_choose == 1:
        print("You WON.")
    elif you_choose == 1 and computer_choose == 0:
        print("You WON.")
    elif you_choose == computer_choose:
        print("Draw")
    else:
        print("You LOSE.")
