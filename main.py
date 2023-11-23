from BloomFilter import BloomFilter as BF
import pandas as pd
import random
from tabulate import tabulate

def frequencyBasedAttack(filter:BF, names, expectedQGrams, threshold):
    candidateQGrams = dict()
    reidentifiedNames = list()

    for name in names:
        candidateQGrams[name] = list()
        for i in range(len(str((name))) - filter.qGrams + 1):
            qgram = name[i:i + filter.qGrams]
            candidateQGrams[name].append(qgram)

    for position in range(filter.qGrams):
        position_qgrams = [qgrams[position] for qgrams in candidateQGrams.values()]
        qgram_counts = {qgram: position_qgrams.count(qgram) for qgram in set(position_qgrams)}

        for name, qgrams in candidateQGrams.items():
            if max(qgram_counts.values()) >= threshold and qgrams[position] in qgram_counts:
                if filter.check(name):
                    reidentifiedNames.append(name)

    return candidateQGrams, reidentifiedNames

def main(size:int, n:int, nHashes:int, qGrams:int) -> None:
    dataset = pd.read_csv(filepath_or_buffer="german-names.csv", names=["Name", "Frequency"]).sort_values(by="Frequency", ascending=False)

    filter = BF(dataset, size, nHashes, qGrams)

    samples = dataset.sample(n=n, axis=0)
    for index, row in samples.iterrows():
        filter.add(str(row['Name']).encode())

    AttactDataset = pd.read_csv(filepath_or_buffer="german-names.csv", names=["Name", "Frequency"]).sort_values(by="Frequency", ascending=False)
    candidateQGrams, reidentifiedNames = frequencyBasedAttack(filter, AttactDataset['Name'].to_list(), qGrams, 2)
    
    positives = 0
    falsePositives = 0
    for victim in reidentifiedNames:
        print(victim + ": " + str(candidateQGrams[victim]))
        if samples['Name'].to_list().count(victim) != 0:
            positives = positives + 1
        else:
            falsePositives = falsePositives + 1
    
    print("\nPositives: " + str(positives) + 
        "\nFalse Positives: " + str(falsePositives))

if __name__ == "__main__":
    size = 1000
    n = 20
    nHashes = 5
    qGrams = 2
    main(size, n, nHashes, qGrams)
