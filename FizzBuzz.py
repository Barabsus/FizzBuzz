
#Creating fizz_buzz function
def fizz_buzz():
    x= range(1,101)
    for i in x:
        if i % 15 == 0:
            print ('fizzbuzz')
        elif i%3 == 0:
            print ("fizz")
        elif i%5 == 0:
            print ('buzz')
        else:
            print (i)
            
#Run test

print(fizz_buz())



    
    
