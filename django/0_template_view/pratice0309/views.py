from django.shortcuts import render
from django.http.response import HttpResponse
import requests
import random

# Create your views here.
def ping(request):
    return render(request,'pratice0309/ping.html')

def pong(request):
    return render(request,'pratice0309/pong.html')

def var_route(request, value):

    return HttpResponse(value)

def lotto(request):  #,time
    # 1. 현실 로또 번호를 가져온다.
    url = f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=953'
    response = requests.get(url).json()
    lotto_list = []
    for key, value in response.items():
        if key == 'drwtNo4' or key == 'drwtNo1' or key == 'drwtNo2'or key == 'drwtNo3'or key == 'drwtNo5'or key == 'drwtNo6':
            lotto_list.append(value)
    lotto_list = sorted(lotto_list)
    bonus = response['bnusNo']

    # 2. 로또번호 저장공간을 만든다
    result = {f'{i}등': 0 for i in range(1,6)}
    result['꽝'] = 0

    # 3. 로또를 랜덤으로 만들고 천회 시행한다.
    for _ in range(1000):
        my_numbers = random.sample(range(1,46),6)
        match_cnt = len(set(lotto_list) &set(my_numbers))
        if match_cnt == 6:
            result['1등'] += 1
        elif match_cnt == 5 and response['bnusNo'] in lotto_list: 
            result['2등'] += 1
        elif match_cnt == 5:
            result['3등'] += 1
        elif match_cnt == 4:
            result['4등'] += 1
        elif match_cnt == 3:
            result['5등'] += 1
        else:
            result['꽝'] += 1

    # 4. 필요한 정보를 딕셔너리형태로 정리한다,
    context = {
        'lotto_list' : lotto_list,
        'my_numbers': sorted(my_numbers),
        'bonus' : bonus,
        'result' : result
    }

    # 5. 웹으로 반환한다.
    return render(request, 'pratice0309/lotto.html', context)



