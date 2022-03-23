
import random
class game_rock_paper_scissor:

    def __init__(self):
        self.paper = 'paper'
        self.rock = 'rock'
        self.scissor = 'scissor'
        self.list = [self.paper, self.rock, self.scissor]
    
    def botRandom(self):
        return  str(random.choice(self.list))


    
    def play(self):
       
       while True :
            player1 =  int(input(f'1.{self.paper} 2.{self.rock} 3.{self.scissor}:=='))

            if player1 == 1 or player1==2 or player1 == 3:
               botplay = self.botRandom()

               if self.list[player1 - 1] == self.paper  and  botplay == self.rock:
                   print(f'player:{self.paper} vs bot:{self.rock}\nplayer winner !!')
                   continue
               elif self.list[player1 - 1] == self.rock  and  botplay == self.paper:
                   print(f'player:{self.rock} vs bot:{self.paper}\nbot winner !!')
                   continue
               elif self.list[player1 - 1] == self.paper  and  botplay == self.scissor:
                   print(f'player:{self.paper} vs bot:{self.scissor}\nbot winner !!')
                   continue
               elif self.list[player1 - 1] == self.scissor  and  botplay == self.paper:
                   print(f'player:{self.scissor} vs bot:{self.paper}\nplayer winner !!')
                   continue
               elif self.list[player1 - 1] == self.scissor  and  botplay == self.rock:
                   print(f'player:{self.scissor} vs bot:{self.rock}\nbot winner !!')
                   continue
               elif self.list[player1 - 1] == self.rock  and  botplay == self.scissor:
                   print(f'player:{self.rock} vs bot:{self.scissor}\nplayer winner !!')
                   continue
                
               else:
                   print('draw')
                   continue
                   

            else:
                break

        
           
           
        
           
           



game = game_rock_paper_scissor()
game.play()


