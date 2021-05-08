import sys
sys.stdin = open("test_input.txt","r",encoding="UTF-8")

case_num = 10
for case in range(case_num):
    trash = input()
    word = list(input())
    sentence = list(input())
    count = 0
    for i in range(len(sentence)-len(word)+1):
        check = True
        if sentence[i] == word[0]:
            for j in range(1,len(word)):
                if word[j] != sentence[i+j]:
                    check = False
                    break
            if check == True:
                count +=1

    print("#{} {}".format(case+1,count))