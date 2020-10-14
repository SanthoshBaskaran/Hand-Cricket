import random
import time
whoBats="NONE";
print("Welcome to Hand-cricket game!!")
print("RULES ****IF ANY PLAYER ENTER GREATER THAN 6,BATSMAN WILL GET OUT****")
print("1.Heads 2.Tails")
print("Choose Your option")
toss=int(input())
while(toss!=None):
    if(toss>2):
        print("Invalid option")
        break
    toss1=random.randint(1,2)
    print("Processing......")
    time.sleep(2)
    if(toss1==1):
        print("you have won the toss")
        print("Choose Batting or Bowling")
        decision=int(input())
        if(decision>2):
            print("Invalid option")
            break
        if(decision==1):
            whoBats="YOU"
            time.sleep(0.5)
            print("You decided to bat first")
        elif(decision==2):
            time.sleep(0.5)
            whoBats="CPU"
            print("You decided to bowl first")
    elif(toss1==2):
        print("CPU won the toss")
        decision1=random.randint(1,2)
        if(decision1==1):
            whoBats="CPU"
            time.sleep(0.5)
            print("CPU Decided to bat first")
        elif(decision1==2):
            whoBats="YOU"
            time.sleep(0.5)
            print("CPU Decided to bowl first")
    score_user=0
    score_cpu=0
    def hand():
        global score_user
        global score_cpu
        user=int(input("you:"))
        cpu=random.randint(1,6)
        print("CPU:",cpu)
        if(cpu!=user and user<=6):
            score_user=score_user+user
            score_cpu=score_cpu+cpu
            hand()
    hand()
    def calculate():
        if(score_cpu1<score_user):
            print("CPU score:",score_cpu1)
            print("You won the game")
            print("CPU lose the game")
        elif(score_cpu1>score_user):
            print("CPU won the game")
            print("You lose the game")
        elif(score_cpu1==score_user):
            print("Match tied")
    def calculate1():
        if(score_user1<score_cpu):
            print("your score:",score_user1)
            print("CPU won the game")
            print("You lose the game")
        elif(score_user1>score_cpu):
            print("You won the game")
            print("CPU lose the game")
        elif(score_user1==score_cpu):
            print("Match tied")
    score_cpu1=0
    def hand1():#cpu Batting
        global score_cpu1
        user=int(input("you:"))
        cpu=random.randint(1,6)
        print("CPU:",cpu)
        if(cpu!=user and user<=6):
            score_cpu1=score_cpu1+cpu
            if(score_cpu1<target1):
                hand1()
            else:
                calculate()
        else:
            calculate()
    score_user1=0
    def hand2():#me
        global score_user1
        user=int(input("you:"))
        cpu=random.randint(1,6)
        print("CPU:",cpu)
        if(cpu!=user and user<=6 and cpu<=6):
            score_user1=score_user1+user
            if(score_user1<target2):
                hand2()
            else:
                calculate1()
        else:
            calculate1()
    if(whoBats=="YOU"):
        print("ohhh....it's Out!!!")
        print("Your Score : ",score_user)
        target1=score_user+1
        print("CPU needs",target1,"runs to win")
        hand1()
    elif(whoBats=="CPU"):
        print("CPU Out!!!")
        print("CPU Score : ",score_cpu)
        target2=score_cpu+1
        print("You need",target2,"runs to win")
        hand2() 
    break

