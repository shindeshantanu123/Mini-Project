class charc():
    def __init__(self,name):
        self.name=name
        self.__life=3
        self.__score=0

    def kicked(self):
        self.__score+=10

    def punched(self):
        self.__score+=5

    def stabbed(self):
        self.__life-=1

    def displaylife(self):
        return self.__life

    def displayscore(self):
        return self.__score

    def intro(self):
        Print(f"name:{s.name}\nlife:{s.__life}\n:{s.__score}")
     
name=input("enter your name: ").title()
print(f"hii{name}\nwelcome to mario")
mario=charc(name)

print("k: for kicked\np:for punched\ns:for stabbed\nE:for Exit")

while(True):
    
    c=input("enter your move: ")
    if(c=="k"):
        mario.kicked()
        print("score 10 point")
        print("new score",mario.displayscore())
    elif(c=="p"):
        mario.punched()
        print("score 5 point")
        print("new score",mario.displayscore())
    elif(c=="s"):
        count=mario.displaylife()
        mario.stabbed()
        print("got stabbed..lost in 1")
        print("life remaining:",mario.displaylife())
        if  count>1:
            continue
        else:
            print("game over")
            break

    elif(c=="e"):
        a=input("are you sure?,(y/n)")
        if(a=="y"):
            break
        elif(a=="n"):
            continue
        else:
            print("invalid")
                
