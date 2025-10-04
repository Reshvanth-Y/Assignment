x=str(input("ENTER THE OPERATION(START OR STOP):"))

while x=="START":
    a=int(input("Enter the number:"))
    ans=a%2

    if ans==0:
        print("The number is even")
        print(f"Hence answer is:{a/2}")
    
    

    else:
        print("The number is odd")
        print(f"Hence the answer is:{a*3}")
  
    x=str(input("ENTER THE OPERATION(START OR STOP):"))

else:
    print("YOU STOPPED THE OPERATION")
