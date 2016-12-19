from featureeng.math import Filter
import pandas as pd

df = pd.read_csv('resources/test1.csv')
data = [1.0, 1.2, 1.2, 3.4, 1.2, 0.99, 1.02, 10.5, 5.6, 1.21, 0.98, 1.0, 1.2, 1.0, 1.1, 1.012, 1.21, 9, 1.2, 0.9]
threesigma_filter = Filter.threeSigma(series=data, threshold=2)

print df
df = Filter.filterData(panda_frame=df, columns=['test'], removal_method='threesigma', threshold=3)
print df