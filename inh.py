class user:
   def __init__(self,name,age,city,state):
       self.name = name
       self.age = age
       self.city = city
       self.state = state
       def UserName(self):
           print(f"my name is {self.name}")
       def UserDetails(self):
           print(f"my age is{self.age} and my location is (self.city) in {self.state}")
u = user ("manoj",20,"kkukas","rajasthan")
u.UserName()
u.UserDetails()