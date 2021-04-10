def preorder(n):
    if n> 0:
        pre_order.append(n)
        preorder(left[n])
        preorder(right[n])

def middleorder(n):
    if n> 0:
        middleorder(left[n])
        middle_order.append(n)
        middleorder(right[n])

def endorder(n):
    if n> 0:
        endorder(left[n])
        endorder(right[n])
        end_order.append(n)

pre_order = []
middle_order = []
end_order = []

edge = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6 ,4, 7, 5, 8, 5, 9, 6, 10, 6, 11,7, 12, 11, 13]
v = max(edge)
e = int(len(edge)/2)
left = [0] *(v+1)
right = [0] *(v+1)
pa = [0] *(v+1)

for i in range(e):
    n1, n2 = edge[i * 2], edge[i * 2 + 1]
    if left[n1] == 0:
        left[n1] = n2
    else:
        right[n1] = n2

    pa[n2] = n1

root = 0
for i in range(1, v + 1):
    if pa[i] == 0:
        root = i
        break

preorder(root)
middleorder(root)
endorder(root)
print(pre_order)
print(middle_order)
print(end_order)