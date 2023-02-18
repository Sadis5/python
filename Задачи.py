coord = str(input('Введите координату: '))
num = int(coord[1])

if (coord[0] == 'a' or coord[0] == 'c' or coord[0] == 'e' or coord[0] == 'g') and num % 2 != 0:
    
    
    print('чёрная')
elif (coord[0] == 'b' or coord[0] == 'd' or coord[0] == 'f' or coord[0] == 'h') and num % 2 == 0:
   
    print('чёрная')  
else:
    print('белая')
