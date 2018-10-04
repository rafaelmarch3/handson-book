import os
import tarfile
from six.moves import urllib
import pandas as pd
import matplotlib.pyplot as plt

HOUSING_PATH = os.path.join("datasets","housing")

def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)

def main():
    housing = load_housing_data()
    print(type(housing))
    print(housing.head())
    print(housing.info())
    print(housing["ocean_proximity"].value_counts())

    housing.hist(bins=50, figsize=(20,15))
    plt.show()

if __name__=='__main__':
    main()
