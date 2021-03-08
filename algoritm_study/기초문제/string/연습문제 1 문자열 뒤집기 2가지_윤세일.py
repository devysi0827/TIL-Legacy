s = 'reverse the strings'
#1
s= s[::-1]
print(s)
#2
s= list(s)
reverses = ''
for i in range(len(s)-1,-1,-1):
    reverses += s[i]
print(reverses)
#3
for i in range(len(s)//2):
    s[i], s[len(s)-1-i] = s[len(s)-1-i], s[i]
print(s)
