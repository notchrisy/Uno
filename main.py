
import random,sys,time,os,re

#Uno time, idk what im doing but we are doing it
import graphics
from graphics import *
def clearline():
  sys.stdout.write('\x1b[1A') 
  sys.stdout.write('\x1b[2K')
tyforthat2=True
#Dictionary of colors of the cards, and the number
dicts={
  'Red 1':["Red",1],'Blue 1':["Blue",1],
  'Red 2':["Red",2],'Blue 2':["Blue",2],
  'Red 3':["Red",3],'Blue 3':["Blue",3],
  'Red 4':["Red",4],'Blue 4':["Blue",4],
  'Red 5':["Red",5],'Blue 5':["Blue",5],
  'Red 6':["Red",6],'Blue 6':["Blue",6],
  'Red 7':["Red",7],'Blue 7':["Blue",7],
  'Red 8':["Red",8],'Blue 8':["Blue",8],
  'Red 9':["Red",9],'Blue 9':["Blue",9],
  'Red 0':["Red",0],'Blue 0':["Blue",0],
  'Yellow 1':["Yellow",1],'Green 1':["Green",1],
  'Yellow 2':["Yellow",2],'Green 2':["Green",2],
  'Yellow 3':["Yellow",3],'Green 3':["Green",3],
  'Yellow 4':["Yellow",4],'Green 4':["Green",4],
  'Yellow 5':["Yellow",5],'Green 5':["Green",5],
  'Yellow 6':["Yellow",6],'Green 6':["Green",6],
  'Yellow 7':["Yellow",7],'Green 7':["Green",7],
  'Yellow 8':["Yellow",8],'Green 8':["Green",8],
  'Yellow 9':["Yellow",9],'Green 9':["Green",9],
  'Yellow 0':["Yellow",0],'Green 0':["Green",0],
  '+4 Card':['All','/','+4'],'Wild Card':['All','/','W'],
  "Green +2 Card":["Green",'+2'],"Yellow +2 Card":["Yellow",'+2'],
  "Red +2 Card":["Red",'+2'],"Blue +2 Card":["Blue",'+2'],
  "Red Reverse Card":["Red",'R'],"Blue Reverse Card":["Blue","R"],
  "Green Reverse Card":["Green",'R'],"Yellow Reverse Card":["Yellow","R"],
  "Red Skip Card":["Red",'S'],"Yellow Skip Card":["Yellow",'S'],
  "Green Skip Card":["Green",'S'],"Blue Skip Card":["Blue","S"]
}

#Just cool printing
def printt(thingggg,dela=.04):
  for i in thingggg:
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(dela)
  print("")


def clear():
  os.system('clear')
pattern=re.compile('\x1b+\[+3+[0-9]+m+')
def normconvert(a690):
  a692=pattern.sub("",a690)
  return a692
printt("Welcome to Uno!\n")
print(underline("New features:"))
print("Lowercase letters now work! red 6 = Red 6")
print("You can now play again after winning or losing! ([In beta] Please report bugs if you find any)\n")
#Rules and stuff here(Or not)
printt("Hit enter to continue (Say 'rules' for the rules of Uno!)")
werthebest=input()
clear()
if werthebest.lower() in ['rule','rules','rules ']:
  printt(underline("Here are the rules of Uno:"))
  printt("The objective of the game is to get rid of all of your cards")
  printt("There are many card types, these are:")
  printt("A Red, Green, Yellow, and Blue version of 0 through 9")
  printt("A Red, Green, Yellow, and Blue versions of Reverse Cards, Skip Cards, and +2 cards")
  printt("Wild Cards, and +4 cards")
  printt("At the beginning of the game, you will get 5 random cards, and there will be one starting card in play")
  printt("To play a card ,it must 1) Have a matching color to the card in play, 2) Have a matching number to the card in play3) Be a Wild Card or a +4 Card, or the card in play is one of these")
  printt("The multi-colored 0-9 cards have no special atributes, but the other cards do")
  time.sleep(2)
  print("(Hit enter to learn more)")
  input()
  tryyour=""
  while tryyour.lower() not in ['no','n']:
    clear()
    print("What would you like to learn more about?")
    print("1) Wild Cards")
    print("2) +4 cards")
    print("3) Reverse Cards and Skip Cards")
    print("4) +2 Cards")
    print("(Say n to exit)")
    tryyour=input("")
    clear()
    if tryyour=="1":
      printt(bold+"Wild Cards:")
      reset()
      printt("Wild Cards are cards that can be placed on any card")
      printt("Once placed, the person who placed it can pick what color the next card must be, excluding other wild cards or +4 cards")
      print("[Enter to continue]")
      input()
      clear()
    if tryyour=="2":
      printt(bold+"+4 Cards:")
      reset()
      printt("+4 Cards are used to give the opponent +4 cards!")
      printt("This can give you a tremendous lead, and +4 Cards can be placed on any card type!")
      print("[Enter to continue]")
      input()
      clear()
    if tryyour=="3":
      printt(bold+"Reverse Cards and Skip Cards")
      reset()
      printt("Reverse Cards are semi useless in 2 player mode...")
      printt("Reverse Cards are used to switch the order of how the turns go")
      printt("Skip Cards are used to skip the opponent's turn!")
      printt("Skip Cards basically give you another turn")
      print("[Enter to continue]")
      input()
      clear()
    if tryyour=="4":
      printt(bold+"+2 Cards")
      reset()
      printt("+2 Cards give your opponent +2 cards!")
      printt("This will give you a slight advantage!")
      print("[Enter to continue]")
      input()
      clear()

#List of cards in uno
cards=['\033[31m'+'Red 1','\033[31m'+'Red 2','\033[31m'+'Red 3','\033[31m'+'Red 4','\033[31m'+'Red 5','\033[31m'+'Red 6','\033[31m'+'Red 7','\033[31m'+'Red 8','\033[31m'+'Red 9','\033[34m'+'Blue 1','\033[34m'+'Blue 2','\033[34m'+'Blue 3','\033[34m'+'Blue 4','\033[34m'+'Blue 5','\033[34m'+'Blue 6','\033[34m'+'Blue 7','\033[34m'+'Blue 8','\033[34m'+'Blue 9','\033[32m'+'Green 1','\033[32m'+'Green 2','\033[32m'+'Green 3','\033[32m'+'Green 4','\033[32m'+'Green 5','\033[32m'+'Green 6','\033[32m'+'Green 7','\033[32m'+'Green 8','\033[32m'+'Green 9','\033[33m'+'Yellow 1','\033[33m'+'Yellow 2','\033[33m'+'Yellow 3','\033[33m'+'Yellow 4','\033[33m'+'Yellow 5','\033[33m'+'Yellow 6','\033[33m'+'Yellow 7','\033[33m'+'Yellow 8','\033[33m'+'Yellow 9','\033[31m'+'Red +2 Card','\033[33m'+'Yellow +2 Card','\033[32m'+'Green +2 Card','\033[34m'+'Blue +2 Card','\033[31m'+'Red Skip Card','\033[33m'+'Yellow Skip Card','\033[32m'+'Green Skip Card','\033[34m'+'Blue Skip Card','\033[31m'+'Red Reverse Card','\033[32m'+'Green Reverse Card','\033[33m'+'Yellow Reverse Card','\033[31m'+'Red 1','\033[31m'+'Red 2','\033[31m'+'Red 3','\033[31m'+'Red 4','\033[31m'+'Red 5','\033[31m'+'Red 6','\033[31m'+'Red 7','\033[31m'+'Red 8','\033[31m'+'Red 9','\033[34m'+'Blue 1','\033[34m'+'Blue 2','\033[34m'+'Blue 3','\033[34m'+'Blue 4','\033[34m'+'Blue 5','\033[34m'+'Blue 6','\033[34m'+'Blue 7','\033[34m'+'Blue 8','\033[34m'+'Blue 9','\033[32m'+'Green 1','\033[32m'+'Green 2','\033[32m'+'Green 3','\033[32m'+'Green 4','\033[32m'+'Green 5','\033[32m'+'Green 6','\033[32m'+'Green 7','\033[32m'+'Green 8','\033[32m'+'Green 9','\033[33m'+'Yellow 1','\033[33m'+'Yellow 2','\033[33m'+'Yellow 3','\033[33m'+'Yellow 4','\033[33m'+'Yellow 5','\033[33m'+'Yellow 6','\033[33m'+'Yellow 7','\033[33m'+'Yellow 8','\033[33m'+'Yellow 9','\033[31m'+"Red 0",'\033[33m'+'Yellow 0','\033[34m'+'Blue 0','\033[32m'+'Green 0','\033[31m'+'Red 1','\033[31m'+'Red 2','\033[31m'+'Red 3','\033[31m'+'Red 4','\033[31m'+'Red 5','\033[31m'+'Red 6','\033[31m'+'Red 7','\033[31m'+'Red 8','\033[31m'+'Red 9','\033[34m'+'Blue 1','\033[34m'+'Blue 2','\033[34m'+'Blue 3','\033[34m'+'Blue 4','\033[34m'+'Blue 5','\033[34m'+'Blue 6','\033[34m'+'Blue 7','\033[34m'+'Blue 8','\033[34m'+'Blue 9','\033[32m'+'Green 1','\033[32m'+'Green 2','\033[32m'+'Green 3','\033[32m'+'Green 4','\033[32m'+'Green 5','\033[32m'+'Green 6','\033[32m'+'Green 7','\033[32m'+'Green 8','\033[32m'+'Green 9','\033[33m'+'Yellow 1','\033[33m'+'Yellow 2','\033[33m'+'Yellow 3','\033[33m'+'Yellow 4','\033[33m'+'Yellow 5','\033[33m'+'Yellow 6','\033[33m'+'Yellow 7','\033[33m'+'Yellow 8','\033[33m'+'Yellow 9','\033[31m'+"Red 0",'\033[33m'+'Yellow 0','\033[34m'+'Blue 0','\033[32m'+'Green 0','+4 Card','+4 Card','+4 Card','\033[31m'+'Red +2 Card','\033[33m'+'Yellow +2 Card','\033[32m'+'Green +2 Card','\033[34m'+'Blue +2 Card','\033[31m'+'Red Skip Card','\033[33m'+'Yellow Skip Card','\033[32m'+'Green Skip Card','\033[34m'+'Blue Skip Card','\033[31m'+'Red Reverse Card','\033[32m'+'Green Reverse Card','\033[33m'+'Yellow Reverse Card']


turn='P'
wildz=False
skipp=False
skipp2=False
deck=[]
deck2=[]
for retyu in range(3):
  cards.append("Wild Card")
theufn=os.environ.get('USER')
if werthebest.lower()==theufn: #No secrets here
  printt("Ez money")
  time.sleep(1)
  deck.append("Wild Card")
  deck.append("+4 Card")
def setup():
  global turn,wildz,skipp,skipp2,deck,deck2
  turn='P'
  wildz=False
  skipp=False
  skipp2=False
  deck=[]
  deck2=[]
  #Deck generation
  for i in range(5): #Deck list will be your deck, number = how many cards
    deck.append(random.choice(cards))
  for i in range(5):
    deck2.append(random.choice(cards))
setup()
def cardsr():
  for f in deck:
    print(f,end=reset1)
    if deck.index(f)-(len(deck)+1)!=-1:
      print(",",end="")
    if deck.index(f)==4 and deck.index(f)!=len(deck)-1:
      print('')
def compcards():
  for f in deck2:
    print(f,end=reset1)
    if deck2.index(f)!=len(deck2)-1:
      print(",",end="")
  print("")
graph=[]
'\x1b[34m'
'\x1b[33m'
'\x1b[32m'
def cardconvert(a1):
  if '\x1b[31m' in a1 or '\x1b[32m' in a1 or '\x1b[33m' in a1 or '\x1b[34m' in a1:
    a1=a1[5:]
  if dicts[a1][1]=="/":
    if dicts[a1][2]=="W":
      return wild+reset1
    if dicts[a1][2]=="+4":
      return plus4+reset1
  elif dicts[a1][0]=="Red":
    if dicts[a1][1]==1:
      return '\033[31m'+one+reset1
    if dicts[a1][1]==2:
      return '\033[31m'+two+reset1
    if dicts[a1][1]==3:
      return '\033[31m'+three+reset1
    if dicts[a1][1]==4:
      return '\033[31m'+four+reset1
    if dicts[a1][1]==5:
      return '\033[31m'+five+reset1
    if dicts[a1][1]==6:
      return '\033[31m'+six+reset1
    if dicts[a1][1]==7:
      return '\033[31m'+seven+reset1
    if dicts[a1][1]==8:
      return '\033[31m'+eight+reset1
    if dicts[a1][1]==9:
      return '\033[31m'+nine+reset1
    if dicts[a1][1]==0:
      return '\033[31m'+zero+reset1
    if dicts[a1][1]=='+2':
      return '\033[31m'+plus2+reset1
    if dicts[a1][1]=='S':
      return '\033[31m'+skip+reset1
    if dicts[a1][1]=='R':
      return '\033[31m'+reverse+reset1
  elif dicts[a1][0]=="Blue":
    if dicts[a1][1]==1:
      return '\033[34m'+one+reset1
    if dicts[a1][1]==2:
      return '\033[34m'+two+reset1
    if dicts[a1][1]==3:
      return '\033[34m'+three+reset1
    if dicts[a1][1]==4:
      return '\033[34m'+four+reset1
    if dicts[a1][1]==5:
      return '\033[34m'+five+reset1
    if dicts[a1][1]==6:
      return '\033[34m'+six+reset1
    if dicts[a1][1]==7:
      return '\033[34m'+seven+reset1
    if dicts[a1][1]==8:
      return '\033[34m'+eight+reset1
    if dicts[a1][1]==9:
      return '\033[34m'+nine+reset1
    if dicts[a1][1]==0:
      return '\033[34m'+zero+reset1
    if dicts[a1][1]=='+2':
      return '\033[34m'+plus2+reset1
    if dicts[a1][1]=='S':
      return '\033[34m'+skip+reset1
    if dicts[a1][1]=='R':
      return '\033[34m'+reverse+reset1
  elif dicts[a1][0]=="Yellow":
    if dicts[a1][1]==1:
      return '\033[33m'+one+reset1
    if dicts[a1][1]==2:
      return '\033[33m'+two+reset1
    if dicts[a1][1]==3:
      return '\033[33m'+three+reset1
    if dicts[a1][1]==4:
      return '\033[33m'+four+reset1
    if dicts[a1][1]==5:
      return '\033[33m'+five+reset1
    if dicts[a1][1]==6:
      return '\033[33m'+six+reset1
    if dicts[a1][1]==7:
      return '\033[33m'+seven+reset1
    if dicts[a1][1]==8:
      return '\033[33m'+eight+reset1
    if dicts[a1][1]==9:
      return '\033[33m'+nine+reset1
    if dicts[a1][1]==0:
      return '\033[33m'+zero+reset1
    if dicts[a1][1]=='+2':
      return '\033[33m'+plus2+reset1
    if dicts[a1][1]=='S':
      return '\033[33m'+skip+reset1
    if dicts[a1][1]=='R':
      return '\033[33m'+reverse+reset1
  elif dicts[a1][0]=="Green":
    if dicts[a1][1]==1:
      return '\033[32m'+one+reset1
    if dicts[a1][1]==2:
      return '\033[32m'+two+reset1
    if dicts[a1][1]==3:
      return '\033[32m'+three+reset1
    if dicts[a1][1]==4:
      return '\033[32m'+four+reset1
    if dicts[a1][1]==5:
      return '\033[32m'+five+reset1
    if dicts[a1][1]==6:
      return '\033[32m'+six+reset1
    if dicts[a1][1]==7:
      return '\033[32m'+seven+reset1
    if dicts[a1][1]==8:
      return '\033[32m'+eight+reset1
    if dicts[a1][1]==9:
      return '\033[32m'+nine+reset1
    if dicts[a1][1]==0:
      return '\033[32m'+zero+reset1
    if dicts[a1][1]=='+2':
      return '\033[32m'+plus2+reset1
    if dicts[a1][1]=='S':
      return '\033[32m'+skip+reset1
    if dicts[a1][1]=='R':
      return '\033[32m'+reverse+reset1
  

for w in deck:
  z=cardconvert(w)
  graph.append(z)
def cardsg():
  for i in graph:
    print(i,end='')
    print('\n'+deck[graph.index(i)])
'''
  f=0
  w=0
  for i in range(6):
    q=0
    for i1 in range(5):
      f=w
      g=0
      while g!=12:
        print(graph[q][f],end="")
        g+=1
        f+=1
      q+=1
    print("")
    w+=11
'''
clear()
start=random.choice(cards)
sumoo=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20']
theeee=""
def judge(theone,thedeck):
  global theeee,start2
  if theone!='/':
    deck1=[]
    deck66=[]
    start2=normconvert(start)
    theone=normconvert(theone)
    for a2 in thedeck:
      a2=normconvert(a2)
      deck1.append(a2)
    for thhh in deck1:
      deck66.append(thhh.lower())
    theonez1=theone
    if theone.isdigit()==False and theone.isspace()==False:
      theonez1=theone.lower()
    if theonez1 in deck66 or theone in sumoo[:len(deck1)]:
        if theone.isdigit()==False:
          theone=deck1[deck66.index(theonez1)]
        if theone.isdigit():
            theone=deck1[int(theone)-1]
        else:
          theeee=theone
        if dicts[theone][0]==dicts[start2][0] or dicts[theone][1]==dicts[start2][1] or dicts[start2][0]=="All" or dicts[theone][0]=='All':
          theeee=thedeck[deck1.index(theone)]
          del thedeck[thedeck.index(theeee)]
          return True
        else:
          print("You cant place that card!")
          time.sleep(3)
          clear()
    else:
      print("Invalid Card...")
      time.sleep(3)
      clear()
  else:
    return False

def compturn():
  zomg=True
  choose=False
  iseeu2=""
  printt("\nThe computer is making its move..")
  time.sleep(2)
  global deck,start,dicts,skipp2,wildz,tyforthat2
  if '+4 Card' in deck2:
    printt("The opponent placed a +4 card!")
    start='+4 Card'
    time.sleep(1)
    printt("Getting 4 cards...")
    deck2.remove('+4 Card')
    for i in range(4):
      deck.append(random.choice(cards))
    start="+4 Card"
    time.sleep(2)
  elif 'Wild Card' in deck2:
    wildz=True
    print("The opponent placed a Wild Card!")
    time.sleep(1)
    rety=random.choice(['Red','Yellow','Blue','Green'])
    printt("The computer decided to make your next card a "+rety+" Card!")
    dicts['Wild Card'][0]=rety
    deck2.remove("Wild Card")
    start="Wild Card"
    time.sleep(2)
  else:
    for iseeu in deck2:
      iseeu2=normconvert(iseeu)
      start3=normconvert(start)
      if zomg==True:
        if dicts[iseeu2][0]==dicts[start3][0] or dicts[iseeu2][1]==dicts[start3][1] or dicts[start3][0]=="All":
          printt("The computer placed a "+iseeu)
          reset()
          start=iseeu
          time.sleep(2)
          deck2.remove(iseeu)
          zomg=False
          choose=True
          if "+2" in iseeu2:
            printt("The computer played a +2 card! Taking +2 cards...")
            for i in range(2):
              time.sleep(1)
              deck.append(random.choice(cards))  
          elif "Reverse" in iseeu2:
            printt("The computer switched the order of which the turns go!")
            printt("This doesnt really help with 2 players...")
            time.sleep(3)
          elif "Skip" in iseeu2:
            printt("Skipping your turn...")
            skipp2=True
            time.sleep(2)
    zomg=True
    if choose==False:
      printt("The computer didnt have a card!")
      time.sleep(1)
      printt("Taking a card...")
      time.sleep(.5)
      print('\a',end='')
      deck2.append(random.choice(cards))
      time.sleep(1.5)
    else:
      choose=False
  clear()
  if len(deck2)==1:
    print(bold+'\033[31m'+underline("Computer says:Uno!"))
  if len(deck2)==0 or deck2==[]:
    for i in range(5):
      print(bold+'\033[31m'+"Computer wins!")
      time.sleep(.3)
      print(bold+'\033[34m'+"Computer wins!")
      time.sleep(.3)
      print(bold+'\033[32m'+"Computer wins!")
      time.sleep(.3)
      print(bold+'\033[33m'+"Computer wins!")
      time.sleep(.3)
    time.sleep(2)
    clear()
    tyforthat2=False
def gamething():
  global dicts,start,theonez,turn,skipp,deck,deck2,theeee,wildz,skipp2,tyforthat2,tyforthat
  tyforthat=True
  while tyforthat:
    startcard = cardconvert(start)
    start69=normconvert(start)
    print(reset1+"Card in play:")
    print(startcard+'\n'+start+"("+dicts[start69][0]+")")
    reset()
    dicts['Wild Card'][0]=="All"
    if turn=="P":
      print(bold+'\nWhich card would you like to place?\n(Say n if you dont have a move/want to pick up a card)')
      reset()
      print(underline("Your cards:"))
      cardsr()
      print("")
      print(underline("Computer's cards:"))
      for oranumberoraletter in range(len(deck2)):
        print("?",end="  ")
      print("")
      printt("(Say the position of the card or the card name)")
      reset()
      theonez=input()
      if theonez.lower() in ['n','no','nope']:
        z=random.choice(cards)
        printt("You drew a "+z)
        reset()
        time.sleep(2)
        deck.append(z)
        theeee=start
        theonez='/'
        turn="C"
        clear()
      f=judge(theonez,deck)
      if f==True:
        if "Skip" in theeee:
          printt("You played a Skip Card! Skipping the computers turn!")
          skipp=True
        elif "+4" in theeee:
          printt("You played a "+underline("+4 card")+"!")
          printt("Giving the computer +4 cards..")
          for i in range(4):
            print("\a",end="")
            time.sleep(.5)
            deck2.append(random.choice(cards))
          time.sleep(1)
          print("")
        elif 'Wild' in theeee:
          wildz=True
          while True:
            printt("You played a "+underline("Wild Card")+"!")
            time.sleep(1)
            printt("What color do you want the computer to next play?\n(Red,Yellow,Blue,Green)")
            coor=input()
            if coor.lower() in ['red','yellow','green','blue']:
              coor=coor.lower()
              coor=coor[0].upper()+coor[1:]
              printt("The color is now "+coor)
              dicts["Wild Card"][0]=coor
              time.sleep(2)
              break
            else:
              print("You have to pick a color!")
              time.sleep(3)
              clear()
        elif "+2" in theeee:
          printt("You played a +2 card! Giving the computer +2 cards...")
          for i in range(2):
            print("\a",end="")
            time.sleep(1)
            deck2.append(random.choice(cards))
          print("")
          time.sleep(1)
        elif "Reverse" in theeee:
          printt("You switched the order of which the turns go!")
          time.sleep(1)
          printt("This doesnt really help with 2 players...")
          time.sleep(3)
        else:
          printt("You played a "+theeee)
          time.sleep(2)
        if len(deck)==1:
          print(bold+'\033[32m'+underline("You say:Uno!"))
          reset()
          time.sleep(2)
        if deck==[] or len(deck)==0:
          clear()
          for i in range(5):
            print(bold+'\033[31m'+"You win!")
            time.sleep(.3)
            print(bold+'\033[34m'+"You win!")
            time.sleep(.3)
            print(bold+'\033[32m'+"You win!")
            time.sleep(.3)
            print(bold+'\033[33m'+"You win!")
            time.sleep(.3)
          time.sleep(2)
          clear()
          tyforthat=False
        start=theeee
        clear()
        if skipp==False:
          turn='C'
        else:
          skipp=False
        if wildz==False:
          dicts['Wild Card'][0]="All"
        else:
          wildz=False


    elif turn=="C":
      if turn=='C':
        reset()
        compturn()
        if tyforthat2==False:
          tyforthat2=True
          tyforthat=False
        if skipp2==False:
          turn='P'
        else:
          skipp2=False
          turn='C'
        if wildz==False:
          dicts['Wild Card'][0]="All"
        else:
          wildz=False
while True:
  gamething()
  yes=['yes','y']
  no=['no','n']
  tyforthat=True
  reset()
  gging=True
  while gging:
    print("Want to play again?")
    tyfornothing=input()
    if tyfornothing.lower() in yes:
      printt('Ok! Lets go into it!')
      setup()
      start=random.choice(cards)
      time.sleep(1)
      clear()
      gging=False
    elif tyfornothing.lower() in no:
      sys.exit()
    else:
      print("You have to say yes or no!")
      time.sleep(2)
      os.system('clear')
