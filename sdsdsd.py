import number_game
answer = input('1~20까지 숫자중 아무 숫자를 말하세요 :')
while True:
    second_answer = input('1번이 말한 숫자를 예측하여 말해보세요 :')

    if second_answer < answer:
        print("더 작은 수 입니다.")
    elif second_answer > answer:
        print("더 큰 수 입니다.")
    else:
        print("정답입니다")
        break
        
