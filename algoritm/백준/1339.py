import sys
sys.stdin = open("1.txt","r")
import itertools

n = int(input())
first_box = []
word_box = []
for i in range(n):
    word = input()
    word_box.append(word)
    for j in range(len(word)):
        first_box.append(word[j])
box = list(set(first_box))
nums = []
for i in range(9, 9-len(box),-1):
    nums.append(i)
# print(box)
# print(nums)

if len(box) == len(first_box):
    permu = [nums]
    dic_2 ={}
else:
    max_len = 0
    second_len = 0
    max_loca = 0
    for i in range(len(word_box)):
        if len(word_box[i]) >= max_len:
            second_len = max_len
            max_len = len(word_box[i])
            max_loca = i
    dic_2 = {}
    for i in range(max_len-second_len):
        temp_dic = {word_box[max_loca][i] : nums[i]}
        box.remove(word_box[max_loca][i])
        dic_2.update(temp_dic)
    nums = nums[max_len-second_len:]

    permu = list(itertools.permutations(nums, len(nums)))
# print(word_box)
ans = 0
for i in range(len(permu)):
    temp_ans = 0

    dic = {name: value for name, value in zip(box, permu[i])}
    dic.update(dic_2)
    for j in range(len(word_box)):
        for k in range(len(word_box[j])):
            temp_ans += dic[word_box[j][k]]*(10**(len(word_box[j])-k-1))
    if temp_ans > ans:
        ans = temp_ans
print(ans)



