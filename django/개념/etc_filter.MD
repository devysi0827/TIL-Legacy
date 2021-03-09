##  views.py에서

```html
def dinner(request):
    today = datetime.now()
    context = {
        'today': today,
        }
    return render(request, 'dinner.html', context)
```



##  templates -> dinner.html에서 

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Document</title>
</head>
<body>
  <p>{{ today|date:'Y년 m월 d일 (D) A H:i' }}는 날짜</p>
 
</body>
</html>
```

