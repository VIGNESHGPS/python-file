class hotel():
    def hotelname(self):
        namefile=open("C:\\Users\\GOD\\OneDrive\\Desktop\\SSBRIYANI.txt","r")
        for eachrow in namefile:
            print(eachrow)
            for single in range (0,len(eachrow)):
                print(eachrow[single])

obj=hotel()
obj.hotel