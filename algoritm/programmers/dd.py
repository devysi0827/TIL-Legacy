print(6)

# def solution(n, k):
#     change_list = []
#     while n >= k:
#         change_list.append(n % k)
#         n = n // k
#     change_list.append(n)
#     change_list = list(reversed(change_list))
#     change_list.append(0)
#
#     num_list = []
#     num_str = ""
#     for i in range(len(change_list)):
#         if change_list[i] != 0:
#             num_str += str(change_list[i])
#         else:
#             if num_str != "":
#                 if num_str == "1":
#                     num_str = ""
#                 else:
#                     number = int(num_str)
#                     num_list.append(number)
#                     num_str = ""
#
#     prime_list = []
#     over_flag = 0
#     max_num = max(num_list) + 10
#     if max_num > 10000000:
#         max_num = 10000000
#         over_flag = 1
#     aristo = [True] * max_num
#
#     m = int(max_num ** 0.5)
#     for i in range(2, m + 1):
#         if aristo[i] == True:
#             for j in range(i + i, max_num, i):
#                 aristo[j] = False
#
#     primes = []
#     for i in range(2, max_num):
#         if aristo[i] == True:
#             primes.append(i)
#
#     if over_flag == 0:
#         for i in range(len(num_list)):
#             if num_list[i] in primes:
#                 prime_list.append(num_list[i])
#     else:
#         for i in range(len(num_list)):
#             prime_flag = 1
#             for j in range(len(primes)):
#                 if num_list[i] % primes[j] == 0:
#                     prime_flag = 0
#                     break
#             if prime_flag == 1:
#                 prime_list.append(num_list[i])
#
#     return len(prime_list)
