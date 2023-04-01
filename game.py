import time
import random
from time import sleep
hp = 100
speed = 0 
boost = 1
distance = 500
rock = 1
yeti = 2
sosed = 3
while True:
    if distance <= 0:
        print('Finish')
        break
    speed += boost
    distance -= speed
    print(f'Осталось: {distance} Текущая скорость: {speed}')
    
    if hp <= 0:
        print("YOU DEAD")
        break
     
    randnumb = random.randint(1, 5)
    if randnumb == rock:
        skills = random.randint(1,2)
        if skills == int(input('Впереди камень, что будете делать:\n 1: повернуть вправо\n 2:повернуть влево ')):
            print("вы объехали")
        else:
                
            hp -= speed // 2
            speed //= 2
            print("\nАЙ!!!", " Ostalos hp: ", hp)

    elif randnumb == yeti:
        hp -= 20
        speed //= 4
        print("\nЙЕТИ!!!", " Ostalos hp: ", hp)
    elif randnumb == sosed:
        hp -= 33
        speed = 0
        print("\nДА ОТДАМ Я ДОЛГ!!!", " Ostalos hp: ", hp)
        
    sleep(0.5)
    
