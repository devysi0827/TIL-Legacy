
arr = [1,2,3,4,5]
n = len(arr)
sel_list = [0] * n

def powerset(idx):
    if idx == n:
        ans= []
        sum = 0
        for i in range(n):
            if sel_list[i]:
                sum += arr[i]
                ans.append(arr[i])

        if sum == 10:
            print(ans)

    else:
        for i in range(2):
            sel_list[idx] = i
            powerset(idx+1)

powerset(0)
