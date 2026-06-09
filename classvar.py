class address:
    total = 0#class variable
    def __init__(self ,city , state,substate):
        self.city = city
        self.state = state
        self.substate = substate
        address.total += 1
    def location(self):
        print("location")
a = address("jaipur","rajasthan","kashi")
b = address("bhilwara","rajasthan",)
print(a.total)
print(b.total)