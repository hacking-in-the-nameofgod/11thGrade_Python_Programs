import math
option=0

nr = 0


num=0


    
while option !=6:
        print ("1. Palindrome" , "2. Prime Number" , "3. Perfect Number" , "4. Armstrong Number", "5. Strong Number" , "6. End" , sep="\n")
        option = int(input("Enter Option:"))
        num = int(input("Enter the Number to check:"))
        zzzz=num
        
      
        stuff = 0
        g=0
        tot=0
        s = 0
        powe = 0
        
        a=2

        
        if option == 1:
                while num>0:
                    m= num%10
                    num=num//10
                    g=g*10+m
                if g == zzzz:
                    print ("The number is a palindrome.")

                else:
                    print ("The number is not a palindrome.")

                print ()

                
        elif option == 2:
            
            while a < num:
                
                xyz = num%a
                if xyz == 0:
                    s+= a

                else:
                    aksafjkjksf=1
                a +=1
                

            if  s== 0:
                print ("The number is prime.")
            else:
                print ("The number is not Prime.")
            print ()


        elif option == 3:
            while a<num:
                if num %a == 0:
                    s+= a

                else:
                    nr+=a
                a +=1

            if s+1== num:
                    print ("The number is perfect.")
            else:
                    print ("The number is not perfect.")

            print ()

        elif option == 4:
        
            if num>0:
                while num>0:
                    pppp = num%10
                    num = num//10
                    powe+=1
                num = zzzz
                while num>0:
                    m = num%10
                    num = num//10
                    stuff = stuff+ (m**powe)
                    

                if stuff == zzzz:
                    print("The number is an Armstrong Number.")

                else:
                    print ("The number is not an Armstrong Number.")
            else:
                print ("The number cannot be determined to be Amrstrong or not.")

                

        elif option == 5:
                while num>0:
                    m= num%10
                    num=num//10
                    tot = tot + math.factorial(m)
                
                if tot == zzzz:
                    print ("The number is a strong number.")

                else:
                    print ("The number is not a strong number.")


        elif option == 6:
            print ("Ending the Program.")
            break

        else:
            print ("Error")
            break



