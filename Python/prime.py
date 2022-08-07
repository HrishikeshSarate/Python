def primeChecker(a):
    if a>1:
       for i in range (2, a):
            if (a%i) == 0 :
                print(a,"is not a prime no.")
            else:
                print(a,"is a prime no.")
                break
    else:
     print(a,"is not a prime no.")


a = int(input("Enter a prime no."))
primeChecker(a)

































# def PrimeChecker(a):  
     
#     if a > 1:  
       
#         for j in range(2, a):  
            
#             if (a % j) == 0:  
#                 print(a, "is not a prime number")  
#                 break  
       
#         else:  
#             print(a, "is a prime number")  
#     else:
#         print(a,"Not a prime no.")        
    


# a = int(input("Enter an input number:"))  
 
# PrimeChecker(a)  