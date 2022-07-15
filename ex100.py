def FirstFactorial(num):
    a = 1
    for i in range(2 , num):
        a *= i
        
  # code goes here r
    print(a)
    num = a
    return num

# keep this function call here 
print(FirstFactorial(8))