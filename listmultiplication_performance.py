import time
list1=[i for i in range(1000000)]
list2=[i for i in range(1000000)]
to=time.time()
prod_lists=list(map(lambda x, y:x*y, list1, list2))
tp=time.time()
print(tp-to)
