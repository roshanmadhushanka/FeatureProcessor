from featureeng import Frame
from featureeng.presenting import Chart

data_frame = Frame('test.csv')

data_frame.apply_moving_average(input_column='test', dest_column='test_moving_avg', row_range=(0, None), window=5)
data_frame.apply_moving_std(input_column='test', dest_column='test_moving_std', row_range=(0, None), window=5)

Chart.presentData(data_frame=data_frame, columns=['test', 'test_moving_avg'])

data_frame.display()