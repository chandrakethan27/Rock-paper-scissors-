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
rock_paper=[rock, paper, scissors]
your_coice=int(input("what will you use? 0 for rock,1 for paper,2 for scissors"))
print("player chooses")
print(rock_paper[your_coice])


computer_choice=random.randint(0,2)
print("computer chooses")
print(rock_paper[computer_choice])

if(your_coice==0 and computer_choice==2):
 print("You win")
elif(your_coice==2 and computer_choice==0):
 print("You loose")

elif(your_coice==1 and computer_choice==0):
 print("You win")
elif(your_coice==0 and computer_choice==1):
 print("You loose")

if(your_coice==2 and computer_choice==1):
 print("You win")
elif(your_coice==1 and computer_choice==2):
  print("You loose")
if(your_coice==computer_choice):
 print("draw")


