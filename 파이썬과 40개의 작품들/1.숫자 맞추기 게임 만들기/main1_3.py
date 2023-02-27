import random 

random_number = random.randint(1, 100)

#print(random_number)

game_count = 1

while True:
    try:
        my_number = int(input("1~100 사이의 숫자를 입력하세요:"))

        if my_number > random_number:
            print("Down")
        elif my_number < random_number:
            print("Up")
        elif my_number == random_number:
            print("축하합니다.{}회 만에 맞췄습니다.".format(game_count))
            print(random_number)
            break
        game_count += 1
    except:
        print("에러가 발생하였습니다. 숫자를 입력하세요")