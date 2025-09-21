#enter -1 to stop
x=int(input("Enter the number of kilometers travelled:"))
payment=0
convience_fee=0
while x!= -1:

    if 0<= x <=5:
        payment=payment+10
    elif 6<= x <=15:
        payment= payment+10+ (x-5)*2
    elif 16<= x <=25:
        payment=payment+30+ (x-15)*3
    elif x>25:
        payment=payment+60+ (x-25)*5
    else:
        payment=payment+0
    convience_fee=convience_fee+100
    x=int(input("Enter the number of kilometers travelled:"))
else:
    print("You Asked me to stop")

payment=payment+convience_fee
print("Total Collection:")
print(payment)
