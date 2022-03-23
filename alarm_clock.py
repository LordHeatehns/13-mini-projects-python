from datetime import datetime
from  playsound import playsound




class Alarm :
    def __init__(self , time , minute):
        
        self.time = int(time)
        self.minute = int(minute)

    def validate(self):
        
        if self.time > 24 :
           return print('invalid time foramat ! please try again')

        else:
            if self.minute > 59 : 
               return print('invalid minute foramat ! please try again')

            else:
                return True
    def playSound(self):
        count = 0
        while True :
            now = datetime.now()
            currentTime =  now.strftime('%H')
            currentMinute = now.strftime('%M')    
                
            if  self.time <= int(currentTime) and self.minute <= int(currentMinute):
                    print("Wake up Master")
                    playsound('/python_projects/Dreaming On - NEFFEX.mp3')
                    count += 1
                    print(count)

                    if  count == 3 :
                        break

                    else:
                        continue

                    
                    
                
                

            

      


    def play(self , valid):

        if not valid :
            print("wrong try again please")
        else:
            print(f"Setting alarm for {self.time}:{self.minute}...")
            self.playSound()

    def show(self):
        print(self.time)
        print(self.minute)


be = Alarm(14,10)
be.show()
bes = be.validate()

set = be.play(bes)




        


