# 문제1. 예상 숫자를 맞추기 게임 --> # number_binggo.py

import random

print('>> 숫자 맞히기 게임 <<')
cnt = 20
com = random.randint(1, 100) # 1 ~ 100 랜덤 생성 ?

while True:
    my = int(input('예상 숫자를 입력하세요 : '))
    if com == my:
        print(f'예상 숫자를 맞추었습니다.')
        cnt = cnt - 1
        print(f'{cnt} 번 남았습니다. ')
        break
    elif my>com:
        print(f'예상숫자한 숫자보다 작습니다.')
        cnt = cnt - 1
        print(f'{cnt} 번 남았습니다. ')
    else:
        print(f'예상숫자 숫자보다 큽니다.')
        cnt = cnt - 1
        print(f'{cnt} 번 남았습니다. ')
