from bitarray import bitarray
import pandas as pd
import mmh3

class BloomFilter:

    def __init__(self, datasetName:str, m:int, k:int, q:int) -> None:
        self.dataset = pd.read_csv(datasetName)
        self.filter = bitarray(m)
        self.numberHashFunctions = k
        self.qGrams = q

    def __init__(self, dataset:pd.DataFrame, m:int, k:int, q:int) -> None:
        self.dataset = dataset
        self.filter = bitarray(m)
        self.numberHashFunctions = k
        self.qGrams = q

    @property
    def dataset(self) -> pd.DataFrame:
        return self._dataset
    
    @dataset.setter
    def dataset(self, value:pd.DataFrame) -> None:
        self._dataset = value
    
    @property
    def filter(self) -> bitarray:
        return self._filter
    
    @filter.setter
    def filter(self, value:bitarray) -> None:
        self._filter = value

    @property
    def numberHashFunctions(self) -> int:
        return self._numberHashFunctions
    
    @numberHashFunctions.setter
    def numberHashFunctions(self, value:int) -> None:
        self._numberHashFunctions = value

    @property
    def qGrams(self) -> int:
        return self._qGrams
    
    @qGrams.setter
    def qGrams(self, value:int) -> None:
        self._qGrams = value

    def add(self, item) -> None:
        for i in range(self.numberHashFunctions):
            hash_val = mmh3.hash(item, i) % len(self.filter)
            self.filter[hash_val] = 1

    def check(self, item) -> bool:
        for i in range(self.numberHashFunctions):
            hash_val = mmh3.hash(item, i) % len(self.filter)
            if self.filter[hash_val] == 0:
                return False
        return True

    def __str__(self) -> str:
        with pd.option_context('display.max_rows', None, 'display.max_columns', None):
            toRet = self.filter + "\n" #+ self.dataset
        return toRet