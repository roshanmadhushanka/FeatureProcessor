from featureeng import Frame
import pandas as pd

df = pd.read_csv('test.csv')

data_frame = Frame(df)

# Apply moving average
#data_frame.apply_moving_average(input_column='test', dest_column='test_moving_average', row_range=(0, None), window=5)

data_frame.display()