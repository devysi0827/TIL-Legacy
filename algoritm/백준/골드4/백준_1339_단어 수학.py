import sys
sys.stdin = open("1.txt","r")

n = int(input())
box = []
alpabets = {}
for i in range(n):
    word = input()
    for j in range(len(word)):
        if word[j] in alpabets:
            alpa = alpabets[word[j]]
            alpa += 10**(len(word)-j-1)
            temp_dic = {word[j]: alpa}
            alpabets.update(temp_dic)
        else:
            alpa = 10 ** (len(word) - j - 1)
            temp_dic = {word[j]: alpa}
            alpabets.update(temp_dic)

sorted_alpabets = sorted(alpabets.values(), reverse = True)

max_num = 9
ans =0
for i in range(len(sorted_alpabets)):
    ans += sorted_alpabets[i]*max_num
    max_num -= 1
print(ans)






