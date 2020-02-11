def comp(x):
    return x["age"]
li=[{"age":20,"name":"def"},{"age":25,"name":"abc"},{"age":10,"name":"ghi"}]
li=sorted(li, key=comp)
print(li)
