import time
import threading

# def calc_square(numbers):
# 	print("[info] calculating square numbers...")
# 	for n in numbers:
# 		time.sleep(0.0001)
# 		# print('square: ', n*n)

def calc_cube(numbers):
	print("[info] calculating cube numbers...")
	for n in numbers:
		if n < 1:
			continue
		# time.sleep(0.0001)
		# print('cube: ', n*n*n)

def split_list(list, amount):
	length = len(list)
	arrEndSize = int(length/amount)
	arr = []
	lastIndex = 0
	if ((length%2 == 0) and (amount%2 == 0)):
		for i in range(amount):
			arr.append(list[lastIndex:lastIndex+arrEndSize])
	return arr

arr = []
for i in range(40000):
	arr.append(i)

t = time.time()
# calc_square(arr)
calc_cube(arr)
print("Done in: ", time.time() - t)


# class Worker(Thread): 
# 	def __init__(self, array):
# 		self.array = array
		
	# def override run(self):
# 		for e in array:

# 		# do stuff

arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8 = split_list(arr, 8)

print(len(arr1))
print(len(arr2))
print(len(arr3))
print(len(arr4))
print(len(arr5))
print(len(arr6))
print(len(arr7))
print(len(arr8))

print("[info] starting time...")
t = time.time()
print("[info] time started")
t1 = threading.Thread(target=calc_cube, args=(arr1,))
t2 = threading.Thread(target=calc_cube, args=(arr2,))
t3 = threading.Thread(target=calc_cube, args=(arr3,))
t4 = threading.Thread(target=calc_cube, args=(arr4,))
t5 = threading.Thread(target=calc_cube, args=(arr5,))
t6 = threading.Thread(target=calc_cube, args=(arr6,))
t7 = threading.Thread(target=calc_cube, args=(arr7,))
t8 = threading.Thread(target=calc_cube, args=(arr8,))

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
print("Done in: ", time.time() - t)
