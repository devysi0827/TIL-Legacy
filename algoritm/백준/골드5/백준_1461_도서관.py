import sys
sys.stdin = open("1.txt","r")

# input 후 정렬
m, n = list(map(int, input().split()))
box = list(map(int, input().split()))
box = sorted(box)
# print(box)

def book_move(minus_box,end) :
    ans = 0
    count = 0

    # 가장 긴 배열이 있는 박스
    if end == 1:
        for i in range(len(minus_box)):
            if i == 0:
                ans -= minus_box[i]
            elif count % n == 0:
                ans -= minus_box[i] * 2
            count += 1

    else:
        for i in range(len(minus_box)):
            if count % n == 0:
                ans -= minus_box[i] * 2
            count += 1

    return ans

minus_box = []
plus_box = []
for i in range(len(box)):
  if box[i]>0:
    plus_box.append(box[i])
  else:
    minus_box.append(box[i])
# print(minus_box)
# print(plus_box)

# 박스세팅,ans 초기화
for i in range(len(plus_box)):
    plus_box[i] = plus_box[i] * -1
plus_box = sorted(plus_box)

# 걸음계산
ans = 0
if len(minus_box) == 0:
    ans += book_move(plus_box,1)
elif len(plus_box) == 0:
    ans += book_move(minus_box,1)
elif abs(minus_box[0]) > abs(plus_box[0]) :
    ans += book_move(plus_box,0)
    ans += book_move(minus_box,1)
else:
    ans += book_move(plus_box,1)
    ans += book_move(minus_box,0)

print(ans)











