#a=10
#b=20
#conditional statement
# if elif else
#if a<b:
    #print("b is greater")

ticketPrice=100
numberOfTicket=input("please enter the number of tickets")
numberOfTicket=int(numberOfTicket)

if numberOfTicket==5:
    print("10% discount")
elif numberOfTicket==10:
    print("20% discount")
elif numberOfTicket==50:
    print("30% discount")
else:
    print("incorrect")
