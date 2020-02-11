'''
Craps赌博游戏
我们设定玩家开始游戏时有1000元的赌注
游戏结束的条件是玩家输光所有的赌注
'''


from random import randint

money = 1000

while money > 0:
    print('你的总资产为：{}'.format(money))
    while True:
        debt = int(input('请下注：'))
        if 0 < debt <= money:
            break
        else:
            print('穷比;你只剩{}'.format(money))
    first = randint(1,6) + randint(1,6)
    print('玩家摇出了{}点'.format(first))
    if first == 7 or first == 11:
        money += debt
        print('玩家胜')
    elif first == 2 or first == 3 or first == 12:
        money -= debt
        print('庄家胜')
    else:
        needs_go_on = True
    
    while needs_go_on:
        needs_go_on = False
        current = randint(1,6) + randint(1,6)
        print('玩家摇出了{}点'.format(current))
        if current == 7:
            money -= debt
            print('庄家胜')
        elif current == first:
            money += debt
            print('玩家胜')
        else:
            needs_go_on = True
print('你已破产') 
