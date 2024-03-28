def same_parity(numbers):
    if len(numbers) == 0:
        return numbers
    else:
         testNumber = numbers[0] % 2
         res = [] 
         for i in numbers:
            if i % 2 == testNumber:
                res.append(i)
         return(res)




print(same_parity([]))
