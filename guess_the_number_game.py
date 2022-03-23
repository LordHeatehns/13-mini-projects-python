import random





def game(randoms , time):
    ranNum =  random.randint(1,randoms)
    times = 0
    for i in range(time):
        times += i
        user = int(input(f"guess a number 1-10  chance {time - i} times: "))

        if user == ranNum :
           return print(f'you winner . the answer is a {ranNum}')
        
        elif times == time:
           return print(f'you lose. the anwser is {ranNum}')
        else:
            continue


game(10,3)
