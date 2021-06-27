import sys
sys.stdin = open("1.txt","r")
import itertools

n = int(input())
box = []
word_box = []
for i in range(n):
    word = input()
    word_box.append(word)
    for j in range(len(word)):
        box.append(word[j])
box = list(set(box))
nums = []
for i in range(9, 9-len(box),-1):
    nums.append(i)
print(box)
print(nums)
permu = list(itertools.permutations(nums, len(nums)))
print(word_box)
for i in range(len(permu)):
    dic = {name: value for name, value in zip(box, nums)}
    print()


