from BloomFilter import BloomFilter as BF
import pandas as pd
import random

dataset = pd.read_csv("german-names.csv")
size = 1000 
nHashes = 5
qGrams = 2

filter = BF(dataset, size, nHashes, qGrams)

sampleD = dataset.sample(n=random.randint(5, 50), axis=0).transpose()

for sample in sampleD:
    filter.add(str(sample).encode())
    print(sample)
