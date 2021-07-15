import sys
sys.stdin = open("1.txt","r")

n, m = list(map(int,input().split()))
arr = list(map(int,input().split()))
usetab = []

ans = 0
for i in range(m):
    if arr[i] in usetab:
        continue

    elif len(usetab) < n:
        usetab.append(arr[i])

    else:
        largest_use_loca = 0
        for j in range(len(usetab)):
            if usetab[j] not in arr[i:]:
                del_tab = j
                break
            elif arr[i:].index(usetab[j]) > largest_use_loca:
                largest_use_loca = arr[i:].index(usetab[j])
                del_tab = j

        usetab[del_tab] = arr[i]
        ans += 1
print(ans)




        #
        # min_use = 9999999
        # min_use_tab = 9999999
        # for j in range(len(usetab)):
        #     future_use = 99999999
        #     for k in range(i,m):
        #         if arr[k] == usetab[j]:
        #             future_use +=1
        #     if future_use < min_use:
        #         future_use = min_use
        #         min_use_tab = usetab[j]
        # usetab.remove(min_use_tab)
        # usetab.append(arr[i])
        # ans += 1



