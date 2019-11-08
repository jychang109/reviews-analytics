data = []
length = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line.strip())
		length += len(line)

length = length / len(data)
print('平均留言長度:', length)