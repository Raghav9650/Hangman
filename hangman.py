import random
word_list=['camel','dog','cat','monkey','raju','ramya']
hangmann=['''      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___''','''      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___''','''      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___''','''      _______
     |/      |
     |      (_)
     |      \|/
     |       
     |      
     |
    _|___''','''      _______
     |/      |
     |      (_)
     |      
     |       
     |      
     |
    _|___''','''      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___''']
print('lives is 5')
wrd=random.choice(word_list)
l=len(wrd)
strg=[]
print(wrd)
for i in range (0,l):
    strg+='_'
k=0
lives=5
while k<l:
    flag=0
    chr=input("guess the letter").lower()
    t=0
    for i in wrd:
        if chr==i:
            strg[t]=i
            flag=1
            k+=1
        t+=1
    s=''
    for i in strg:
        s+=i
    print(s)
    if flag==1:
        print(lives)
        print(hangmann[(lives)])
    elif flag==0:
        lives-=1
        print('lifes left is: ',lives)
        print(hangmann[(lives)])
    if lives==0:
        print("You loose")
        break
if lives!=0:
    print("You win!")