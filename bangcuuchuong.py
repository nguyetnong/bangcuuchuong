


row = ""
for i in range(1, 10):
    
   
    for number in range(1,10):
        
        row = row + str(number) + ' x ' + str(i) + ' = ' + str(number*i).ljust(2) +"    "
    print(row)
    row = ""