# hadoop_streaming

### streaming

- 하둡을 파이썬이나 기타 다른 언어로 돌리는 방법



### code

```python
#!/usr/bin/env python

import sys
for line in sys.stdin:
	line = line.strip()
	words = line.split()
	
	for word in words:
		print ('%s\t%s' % (word,1))

```



```python
#!/usr/bin/python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
	line = line.strip()
	word, count = line.split('\t',1)
	try:
		count = int(count)
	except ValueError:
		continue
		
	if current_word == word:
		current_count +=count
	else:
		if current_word:
			print ('%s\t%s' % (current_word, current_count))
		current_count = count
		current_word = word
		
if current_word == word:
	print ('%s\t%s' % (current_word, current_count))
```



### 결과![image-20210908235042219](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210908235042219.png)
