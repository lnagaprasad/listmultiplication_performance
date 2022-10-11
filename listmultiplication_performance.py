import time
list1=[i for i in range(1000000)]
list2=[i for i in range(1000000)]
to=time.time()
prod_lists=list(map(lambda x, y:x*y, list1, list2))
tp=time.time()
print(tp-to)
list_time=tp-to

import numpy as np
ar1=np.array(list1)
ar2=np.array(list2)
to=time.time()
prodlist=ar1*ar2
tp=time.time()
print(tp-to)
numpy_time=tp-to
print("The ratio of time taken is {}".format(list_time/numpy_time))
