data = []
count = 0
with open('reviews.txt','r') as f:
	for line in f:
		data.append(line)
		count += 1 # count = count + 1
		if count % 10000 == 0:
			print(len(data)) # find the length(count of items) of list
print(len(data))

# print(data[0])
# print('----------------')
# print(data[1])