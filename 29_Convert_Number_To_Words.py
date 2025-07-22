n1 = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']
n2 = ['','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
n3 = ['Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety','Hundred']
n4 = ['Thousand']

n = int(input("Enter a number between 1 and 1000: "))

def convert_number_to_words(n):
        if n>0 and len(str(n))<=3:
                if  n<=10:
                        print(n1[n])
                elif n>10 and  n<20:
                        n = n-10
                        print(n2[n])
                elif n<100:
                        rem = n%10
                        q = n // 10
                        print(n3[q-2],n1[rem].lower())
                elif n==100:
                        print(n3[len(n3)-1])
                elif n>100:
                        h = "Hundred and"
                        h1 = "Hundred"
                        rem = n%100            
                        if rem ==0 and rem!=100:
                                n = n // 100                   
                                print(n1[n],h1)
                        elif rem <=10:
                                print(h,n1[rem].lower())
                        else:
                                rem = n%100                         
                        
                                number3 = n%10                 
                                n = n//10                            
                                number2 = n%10                 
                                n = n//10                            
                                number1 = n%10                 

                                if number2 == 1:
                                        print(n1[number1],h,n2[number3].lower())
                                else:
                                        print(n1[number1],h,n3[number2-2],n1[number3].lower())
                else:
                        print("No results")
        elif n==1000:
                print(n1[1],n4[0])
        elif len(str(n))>3:
                print("Please enter a number between 1 and 1000")
        else:
                print("Please enter positive number")

convert_number_to_words(n)


