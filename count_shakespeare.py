import matplotlib.pyplot as plt
import numpy as np


with open('Shakespeare.txt') as f:
	data = f.read().rstrip().split(' ')

data = [x.lower() for x in data if x!='' and x!='\n']

counts = {}

for word in data:
	try:
		counts[word] += 1
	except:
		counts[word] = 0

sorted_counts = dict(sorted(counts.items(), key=lambda item: item[1], reverse=True))
pop_words = list(sorted_counts.keys())[:100]

print("Top 100 words appearing in Shakespeare plays:")
print(pop_words)


counts = list(sorted_counts.values())[:5000]

plt.yscale('log')
plt.xscale('log')
plt.ylabel('Frequency')
plt.xlabel('Words')
plt.plot(counts)
plt.show()