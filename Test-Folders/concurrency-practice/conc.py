import time
import threading
from threading import Lock

# def calc_square(numbers):
# 	print("[info] calculating square numbers...")
# 	for n in numbers:
# 		time.sleep(0.0001)
# 		# print('square: ', n*n)

sum = 0
lock = Lock()

def calc_cube(numbers):
	print("[info] calculating cube numbers...")
	for n in numbers:
		global sum 
		lock.acquire()
		sum = sum + 1
		lock.release()
		asdf = n*n*n

def split_list(list, amount):
	length = len(list)
	arrEndSize = int(length/amount)
	arr = []
	lastIndex = 0
	if ((length%2 == 0) and (amount%2 == 0)):
		for i in range(amount):
			print("lastIndex")
			arr.append(list[lastIndex:lastIndex+arrEndSize])
			lastIndex = lastIndex+arrEndSize
	return arr

arr = []
for i in range(40000):
	arr.append(i)

# t = time.time()
# # calc_square(arr)
# calc_cube(arr)
# print("Done in: ", time.time() - t)


# class Worker(Thread): 
# 	def __init__(self, array):
# 		self.array = array
		
	# def override run(self):
# 		for e in array:

# 		# do stuff

arr1, arr2, arr3, arr4 = split_list(arr, 4)

print("[info] starting time...")
t = time.time()
print("[info] time started")
t1 = threading.Thread(target=calc_cube, args=(arr1,))
t2 = threading.Thread(target=calc_cube, args=(arr2,))
t3 = threading.Thread(target=calc_cube, args=(arr3,))
t4 = threading.Thread(target=calc_cube, args=(arr4,))

t1.start()
t2.start()
t3.start()
t4.start()

t1.join()
t2.join()
t3.join()
t4.join()
print("Done in: ", time.time() - t)

print(sum)
total = 0
for i in range(40):
	total = total + 1
print(total)