import random
n=random.randbytes(3)
print(random.randrange(1,8))
print(random.randrange(100,211))
mylist={"jadeja","Ashwin","Rahane","shami","Dhoni","virat"}
mylist1={"jadeja","Ashwin","Rahane","shami","Dhoni","virat"}
print(random.choice(mylist))
#print{random.choice{mylist}}
random.shuffle(mylist)
print(mylist)