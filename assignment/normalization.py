import numpy as np
import pandas as pd


def MaxMinNormalization(x, Max, Min):
    x = (x - Min) / (Max - Min)
    return x

def Z_scoreNormalization(x, mu, sigma):
    x = (x - mu) / sigma
    return x

np.random.seed(1)
data_train = pd.DataFrame(np.random.randn(4, 4) * 4 + 3)
with open("normalization.txt", "w") as f:
    f.write("")
data = open("")
# print(data_train)

data_train_norm1 = MaxMinNormalization(data_train, data_train.max(), data_train.min())
    # (data_train - data_train.min()) / (data_train.max() - data_train.min())
print(data_train_norm1)

data_train_norm2 = Z_scoreNormalization(data_train, np.mean(data_train), np.std(data_train))
print(data_train_norm2)