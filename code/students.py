n = int(input("Please input number of students:"))
data = {}
Subjects = {'Physics', 'Maths', 'History'}
for i in range(0,n):
    name = input("Please input student'name:{}".format(i+1))
    marks = []
    for x in Subjects:
        marks.append(int(input("Please Input marks{}".format(x))))
    data[name] = marks

for x,y in data.items():
    total = sum(y)
    print("{}'s total marks {}".format(x,total))
    if total < 120:
        print(x,"failed:()")
    else:
        print(x,"passed")
