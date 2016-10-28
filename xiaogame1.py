import random
secret = random.randint(1,10)
tmp = input('猜一猜我心里想的数是什么：')
guess = int(tmp)
while guess != secret:
    if guess > secret:
        print('哥，大了大了~~~')
    else:
        print('嘿，小了，小了！！！')
    tmp = input('猜一猜我心里想的数是什么：')
    guess = int(tmp)
print("厉害了，我的哥！")
print("哼，猜中了也没有奖励")
print('游戏结束，不玩啦~~~')
    
