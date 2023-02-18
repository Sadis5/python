coord = str(input('Введите координату: '))
num = int(coord[1])

if (coord[0] == 'a' or coord[0] == 'c' or coord[0] == 'e' or coord[0] == 'g') and num % 2 != 0:
    
    
    print('чёрная')
elif (coord[0] == 'b' or coord[0] == 'd' or coord[0] == 'f' or coord[0] == 'h') and num % 2 == 0:
   
    print('чёрная')  
else:
    print('белая')

min = int(input('Кол-во минут: '))   
lim_min = 200
sms = int(input('Кол-во смс: '))
lim_sms = 50
total_sum = 350
if min > lim_min: 
    total_sum += (min - lim_min)*1.25
    print(total_sum)
if sms > lim_sms:
    total_sum += (sms - lim_sms)*5  
    print(total_sum)  
