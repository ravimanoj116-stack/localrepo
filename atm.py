balance = 3000
#int(input(" enter your balance:"))
while True:
    amount = int (input("enter your amount :"))
    
    if amount == 0:
        break
    password = int(input("enter your password :"))
    if password !=7631:
        print("incorrect password :plaese try again")
    else:    
     if amount <= balance:
       balance -= amount    
       print ("remaining balance:",balance)
       print("cogratulation : please collect your money")
     else:
        print("balance is not enough")   
