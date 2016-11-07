import random
from datetime import datetime
x = random.sample(xrange(10), 5)
x = [5,4,3,2,1]
start_time = datetime.now()
print x
def sort(x):
    for right in range (0, len(x)-1):
        left = (right+1)
        print x[right]
        print x[left]
        print x
        if x[left] < x[right]:
            print "left is bigger"

        if x[left] < x[right]:
            print "right is bigger"


print sort(x)
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
