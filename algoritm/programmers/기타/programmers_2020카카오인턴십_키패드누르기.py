def solution(numbers, hand):
    answer = ''
    # 눈에 보기 좋은 참고박스
    # box = [[1, 2, 3],
    #  [4, 5, 6],
    # [7, 8, 9],
    # ['*', 0, '#']]

    #1. 현재 위치 기록(*,#)
    now_left = 3 * 3 + 1
    now_right = 3 * 3 + 3
    i = 0

    #2. 본문
    while i < len(numbers):
        # 2-0. 0 위치가 11이 아니므로 11로 맞추어준다.
        if numbers[i] == 0:
            numbers[i] = 11
        # box = [[1, 2, 3],
        #  [4, 5, 6],
        # [7, 8, 9],
        # [10, 11, 12]]

        #2-1. 왼손용이면 그냥 왼손이 치자
        if numbers[i] %3 == 1:
            # 문자열을 더하고
            answer += 'L'
            # 현재 숫자를 기준으로 잡고
            now_left = numbers[i]
            # i에 1더하기
            i += 1

        # 2-2. 오른손용이면 걍 오른손이 치자
        elif numbers[i] %3 == 0:
            answer += 'R'
            now_right = numbers[i]
            i += 1


        # 2-3. 중립이면??
        elif numbers[i]%3 ==2:

            # 2-3-2. 3으로 나눈 몫은 x좌표, 3으로 나눈 나머지 == y좌표
            x = numbers[i]//3
            y = numbers[i]%3


           # 2-3-2-1. 오른손의 현재 위치 계산
            x_r = now_right//3
            y_r = now_right%3
            # right가 만약 3의 배수이면 위 조건이 안 맞으므로 조건에 맞게 처리해준다.
            if y_r == 0:
                y_r +=3
                x_r -=1

            # 2-3-2-2. 왼손의 현재 위치 계산
            x_l = now_left// 3
            y_l = now_left%3
            # left가 만약 3의 배수이면 위 조건이 안 맞으므로 조건에 맞게 처리해준다.
            if y_l == 0:
                y_l +=3
                x_l -=1

            # 2-3-3. 현재 좌표 기준으로 거리계산
            dis_r = abs(x-x_r)+abs(y-y_r)
            dis_l = abs(x-x_l)+abs(y-y_l)

            #2-3-4. 왼손이 가까우면 l
            if dis_l < dis_r:
                answer += 'L'
                now_left = numbers[i]
                i += 1

            # 2-3-5. 거리가 같으면 원하는 손으로
            elif dis_l == dis_r :
                if hand == 'right':
                    answer += 'R'
                    now_right = numbers[i]
                    i += 1
                elif hand == 'left':
                    answer += 'L'
                    now_left = numbers[i]
                    i += 1

            # 2-3-6. 왼손이 가까우면 r
            else:
                answer += 'R'
                now_right = numbers[i]
                i += 1

    return answer

numbers = 	[7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
print(solution(numbers, "right"))