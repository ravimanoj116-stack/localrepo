class address:
    def __init__(self , city , state):
        self.city = city
        self.state = state
    def location(self):
        print(f"my location is {self.city} in {self.state}")
class hometown:
    def __init__(self , city ,state):
        self.city = city
        self.state = state
    def location(self):
           print(f"my hometown location is {self.city} in {self.state}")
    
a = address("pindwara","jaipur")
a.location()
b = hometown("garhwa","jharkhand")
b.location()