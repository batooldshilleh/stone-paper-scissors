import random 
rock=( '''
        _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
    ''')
pibar=('''
         _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
    ''')
    
sic=('''
        _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')
ch = [rock,pibar,sic]
   
chose=int(input("enter 0 to roke , 1 to paper , 2 to sicors : \n"))
print(ch[chose])
chose2 = random.randint(0,2)

print(ch[chose2])
if chose == chose2 :
    print("neutralize")
elif (chose == 0 and chose2 ==2) or (chose ==1 and chose2 == 0) or (chose == 2 and chose2 ==1):
    print("you are win")
else :
    print("you are lose")