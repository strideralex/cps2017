from __future__ import print_function # must be first in file
import random
import time
import sys

    # all of the codes above are necessary for the game to function.



    
def rpsls():
    u = 0
    while u == 0:
        name = raw_input('What is your name?\n')
        u += 1
    choice(name)
    
    
def choice(name):  
    y = 0  
    while y == 0:
        a = raw_input('\n\nRock, Paper, Scissors, Lizard, or Spock?:\n\n')
        p1 = a.lower()
        print('\n')
        
        if p1 == 'paper':
            paper(name)
        
        elif p1 == 'rock':
            rock(name)
        
        elif p1 == 'scissors':
            scissors(name)
        
        elif p1 == 'lizard':
            lizard(name)
        
        elif p1 == 'spock':
            spock(name)
        
        elif p1 == 'end':
            byebye(name)
            sys.exit()   
        
        else:
            wiseass()       

    
    

def rock(name):
    cpu = random.randint(1,5)    
    if cpu == 1:
        print (name,' chose Rock and the CPU chose Rock. Tie!')
        cf(name)
    
    if cpu == 2:
        print ('The CPU chose Paper and' ,name, 'chose Rock. You lose!') 
    
    if cpu == 3:
        print (name,' chose Rock and the CPU chose Scissors. You win!') 
    
    if cpu == 4:
        print (name,' chose Rock and the CPU chose Lizard. You win!')
    
    if cpu == 5:
        print ('The CPU chose Spock and' ,name, 'chose Rock. You lose!')  

def paper(name):
    cpu = random.randint(1,5)    
    if cpu == 1:
        print (name, 'chose Paper and the CPU chose Rock. You win!')
            
    elif cpu == 2:
        print (name, ' chose Paper and the CPU chose Paper. Tie!')
        cf(name)
            
    elif cpu == 3:
        print ('The CPU chose Scissors and' ,name, 'chose Paper. You lose!') 
    
    elif cpu == 4:
        print ('The CPU chose Lizard and' ,name, 'chose Paper. You lose!')
    
    elif cpu == 5:
        print (name, 'chose Paper and the CPU chose Spock. You win!')     

def scissors(name):
    cpu = random.randint(1,5)    
    if cpu == 1:
        print ('The CPU chose Rock and' ,name, 'chose Scissors. You lose!')
            
    elif cpu == 2:
        print (name,' chose Scissors and the CPU chose Paper. You win!')
            
    elif cpu == 3:
        print (name,' chose Scissors and the CPU chose Scissors. Tie!')
        cf(name)
    
    elif cpu == 4:
        print (name,' chose Scissors and the CPU chose Lizard. You win!')
    
    elif cpu == 5:
        print ('The CPU chose Spock and' ,name, 'chose Scissors. You lose!')

def lizard(name):
    cpu = random.randint(1,5)    
    if cpu == 1:
        print ('The CPU chose Rock and' ,name, 'chose Lizard. You lose!')
            
    elif cpu == 2:
        print (name,' chose Lizard and the CPU chose Paper. You win!')
            
    elif cpu == 3:
        print ('The CPU chose Scissors and' ,name, 'chose Lizard. You lose!')
        
    elif cpu == 4:
        print (name,' chose Lizard and the CPU chose Lizard. Tie!')
        cf(name)
    
    elif cpu == 5:
        print (name,' chose Lizard and the CPU chose Spock. You win!')        

def spock(name):
    cpu = random.randint(1,5)    
    if cpu == 1:
        print (name,' chose Spock and the CPU chose Rock. You win!')
            
    elif cpu == 2:
        print ('The CPU chose Paper and' ,name, 'chose Spock. You lose!')
            
    elif cpu == 3:
        print (name,' chose Spock and the CPU chose Scissors. You win!')
        
    elif cpu == 4:
        print ('The CPU chose Lizard and' ,name, 'chose Spock. You lose!')
    
    elif cpu == 5:
        print (name,' chose Spock and the CPU chose Spock. Tie!')    
        cf(name)

blah = "Wiseass\n"

def wiseass():
    for l in blah:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)

def bot():
    o = 1
    while o < 21:
        time.sleep(1)
        p = ['rock', 'Rock', 'paper', 'Paper', 'scissors', 'Scissors', 'I am a turd']
        a = random.choice(p)
        p1 = a.lower()
        print ('\n\nTest #',o)
        print ('\n''Word: ',a, '\n')
        print ('Lowercased: ' ,p1,'\n')
        if p1 == 'paper':
            o += 1
            paper()
        elif p1 == 'rock':
            o += 1
            rock()
        elif p1 == 'scissors':
            o += 1
            scissors()
        else:
            o += 1
            wiseass()       

def cf(name):
        b = raw_input('\n\nHeads or Tails?:\n\n')
        p2 = b.lower()
        print('\n')
        if p2 == 'heads':
            heads(name)
        elif p2 == 'tails':
            tails(name)
        elif p2 == 'end':
            byebye(name)
            sys.exit()
        
        elif p2 != 'heads' or 'tails':
            wiseass()


def heads(name):
    cpu = random.randint(1,2)
    if cpu == 1:
            print(name, 'chose Heads, you got it right. YOU WIN!!!')
            choice(name)
    if cpu == 2:
            print(name, 'chose Tails, you got it wrong. YOU LOSE!!!')
            choice(name)

def tails(name):
    cpu = random.randint(1,2)
    if cpu == 1:
        print(name, 'chose Heads, you got it wrong. YOU LOSE!!!')
        choice(name)
    if cpu == 2:
        print(name, 'chose Tails, you got it right. YOU WIN!!!')
        choice(name)


           
            
def byebye(name):
    v = "Have a nice day " ,name, "!\n" 
    for l in v:
        sys.stdout.write(l)
        sys.stdout.flush()
        time.sleep(0.2)


        
