# def solution(n):
#     if n == 2:
#         return 1
#
#     answer = 1
#     for i in range(2, n + 1):
#         for j in range(2, int(i ** (1 / 2)) + 1):
#             if i % j == 0:
#                 break
#         else:
#             answer += 1
#
#     return answer


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

# def solution(n):
#     primes = [2]
#
#     for number in range(3,n+1):
#         check =1
#
#         for prime in primes:
#             if number % prime == 0:
#                 check = 0
#                 break
#         if check == 1 :
#             for i in range(primes[-1]+1, int(number/2)+1):
#                 if number % i == 0:
#                     break
#             else:
#                 primes.append(number)
#
#     return len(primes)
