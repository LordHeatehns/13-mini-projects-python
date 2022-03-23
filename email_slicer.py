

class emailSlice:
    def __init__(self,email):
        self.email = str(email)
        self. result = None

    def sliceV1(self):
        seperated =  self.email.split('@')
        self.result = seperated 
        return  print(f'your name is {self.result[0]} and your domain name is {self.result[1]}\n\n')  

    def sliceV2(self):
        seperated = self.email
        user_name = seperated[:seperated.index('@')]
        domain_name = seperated[seperated.index('@')+1:]
        

        return  print(f'your name is {user_name} and your domain name is {domain_name}')  





be = emailSlice('nut@hotmail.com')

be.sliceV1()
be.sliceV2()
