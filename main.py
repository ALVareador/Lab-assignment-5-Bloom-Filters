from BloomFilter import BloomFilter as BF
import pandas as pd
import random

predataset = pd.read_csv("pprl-attack-data\german-names.csv")
dataset = predataset.transpose()
size = 1000 
nHashes = 5
qGrams = 2

filter = BF(dataset, size, nHashes, qGrams)

for sample in dataset.sample(n=random.randint(5, 50), axis=0):
    filter.add(sample)
    print(sample)
