name = ['bipin', 'shristy', 'bishal', 'esrar', 'aakash', 'harry']
name = [x
   for (i, x) in enumerate(name) if i not in (0, 4, 5)
]
print(name)