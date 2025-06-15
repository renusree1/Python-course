amount = int(input("How much amount do you want to withdraw- "))
note500= amount//500
note100= (amount%500) //100
note50= ((amount%500)%100)//50
note20= (((amount%500)%100)%50)//20
note10= ((((amount%500)%100)%50)%20) //10
print("500- ",note500)
print("100- ",note100)
print("50- ",note50)
print("20- ",note20)
print("10- ",note10)