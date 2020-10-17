# API XML JSON, материалы лекции 8

```python
import requests
text = requests.get('http://py4e-data.dr-chuck.net/comments_42.xml').text
obj = BeautifulSoup(text, features="xml")

total = 0
for id in obj.commentinfo.comments.find_all('comment'):
    total += int(id.count.text)
print(total)
```

## дз - сделать запрос хотя бы 1