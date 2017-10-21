# python

## 계산기
  
  *사용법*

  00일 00시 후의 날짜

    python dday.py -d 1
    
    python dday.py -d 1 -h 10
    
    python dday.py -h 10
    
## 에러 출력

* Print Error
```python
import traceback
try:
    1/0
except:
    print(traceback.format_exc())
```

* Raise Error
```python
import sys
def printException():
    message = []
    for e in sys.exc_info():
        message.append(str(e))
    message = '\n'.join(message)
    print message
    return message

try:
    raise "Error"
except:
    printException()
```