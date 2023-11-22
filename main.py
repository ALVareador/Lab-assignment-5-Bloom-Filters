from BloomFilter import BloomFilter as BF
import pandas as pd
import random

def main():
    dataset = pd.read_csv(filepath_or_buffer="german-names.csv", names=["Name", "Frecuency"]).sort_values(by="Frecuency", ascending=False)
    size = 1000 
    nHashes = 5
    qGrams = 2

    filter = BF(dataset, size, nHashes, qGrams)

    for sample in dataset.sample(n=random.randint(5, 50), axis=0).transpose():
        filter.add(str(sample).encode())


if __name__ == "__main__":
    main()
