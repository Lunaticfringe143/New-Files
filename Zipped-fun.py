#zipper functionality

list1 = [1, 2, 3, 4]
list2 = ['one', 'two', 'three', 'four', 'five']

zipped = list(zip(list2, list1))

print(zipped)

unzipped = list(zip(*zipped))
print(unzipped)

items = ['banana', 'apple', 'orange']
counts = [3, 8, 4]
prices = [20, 30, 50]


sentences = []

def dummy():
	for (item, count, price) in zip(items, counts, prices):
		sentence = " I bought " + str(count) + "" + str(item) + 's at' + str(price) + 'each.'
		sentences.append(sentence)
	print(sentences)

dummy()

print(timeit(dummy))

