class book_ticket:
    global n1,n2
    n1=100# bus base fare
    n2=5 #no of available seat
    print ("available seats",n2)
    def female (self,gender,transp,n3):
        if (gender=="female" and transp=="bus" and n3<=n2):
            c="no bus spare"
            print("you are identified as an female")
            print("you are opted to travel bus")
            print("you are FREE to travel")
            print("number of seats booked",n3)
            print("you have to pay"+str(n3*0))
        elif (gender == "female" and transp == "bus" and n3 > n2):
            print("only "+str(n2)+" seats are available")
        elif (gender == "female" and transp == "train"):
            print("the base fare for train is",90)
            print("choose bus for free transport")
            print("you have to pay"+ str(n3*90))
    def male (self,gender,transp,n3):
        if (gender=="male" and transp=="bus" and n3<=n2):
            print("you are identified as male")
            print("you are opted to travel in bus")
            print(n1,"is you bus fare")
            print("number of seats booked", n3)
            print("you have to pay"+ str(n3*n1))
        elif (gender == "male" and transp == "bus" and n3 > n2):
            print("only "+str(n2)+" seats are available")
        elif (gender == "male" and transp == "train"):
            print("the base fare for train is",90)
            print("choose train for better transport")
    def invalid (self,gender,transp,n3):
        if(gender != "female"):
            if(gender !="male"):
                print("enter valid gender")
            if (transp != "bus"):
                if (gender != "train"):
                    print("enter the valid mode of transport")



a1=input("Enter the gender MALE OR FEMALE  ")
a2=input("Enter the mode of transport BUS OR TRAIN   ")
a3=int(input("Enter the number of seats neede   "))
n=book_ticket()
n.female(a1,a2,a3)
n.male(a1,a2,a3)
n.invalid(a1,a2,a3)
