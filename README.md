# Feature Processor
### Introduction
Feature processor is a python platform where you can do feature engineering to your dataset. All the underline
functionality in Feature Processor is based on pandas, scipy numpy, sklearn-pandas and other python libraries. This processing platform only support data in CSV format with headers.

### Prerequsites
	1. numpy
	2. scipy
	3. sklearn
	4. pandas
	5. sklearn-pandas
	6. h2o

### Getting Started
Loading modules into the project

### Frame
Frame is the data structure which holds the CSV data. IThe frame is the data structure which holds the CSV data. It also provides functionalities to do feature engineering to the dataset. Frame() constructor can take pandas frame or path to a CSV file as arguments.

```
from featureeng import Frame

data_frame = Frame('test.csv')
```

#### Feature engineeniring methods
1. Moving Average
2. Moving Median
3. Moving Variance
4. Moving Standard Deviation
5. Moving Probability
6. Moving Entropy
7. Moving K-Closest Average
8. Moving Median Centered Average
9. Moving Threshold Average

#### 1. Moving Average
Calculate average within a moving window

example :
```
# Apply moving average
data_frame.apply_moving_average(input_column='test', dest_column='test_moving_average', row_range=(0, None), window=5)
```
result :
```
     test  test_moving_average
0   5.299               0.0000
1   6.982               0.0000
2   5.363               0.0000
3   8.653               0.0000
4   3.321               5.9236
5   7.959               6.4556
6   8.738               6.8068
7   7.563               7.2468
8   5.134               6.5430
9   3.178               6.5144
10  5.374               5.9974
```

#### 2. Moving Median
Calculate median within a moving window

example :
```
	# Apply moving median
data_frame.apply_moving_median(input_column='test', dest_column='test_moving_median', row_range=(0, None), window=5)
```
result :
```
     test  test_moving_median
0   5.299               0.000
1   6.982               0.000
2   5.363               0.000
3   8.653               0.000
4   3.321               5.363
5   7.959               6.982
6   8.738               7.959
7   7.563               7.959
8   5.134               7.563
9   3.178               7.563
10  5.374               5.374
```

#### 3. Moving Variance
Calculate variance within a moving window

example :
```
	# Apply moving variance
data_frame.apply_moving_variance(input_column='test', dest_column='test_moving_var', row_range=(0, None), window=5)
```
result :
```
     test  test_moving_median
0   5.299            0.000000
1   6.982            0.000000
2   5.363            0.000000
3   8.653            0.000000
4   3.321            3.209552
5   7.959            3.677073
6   8.738            4.540183
7   7.563            4.044039
8   5.134            4.046009
9   3.178            4.233579
10  5.374            3.809019
```

#### 4. Moving Standard Deviation
Calculate standard deviation within a moving window

example :
```
# Apply moving standard deviation
data_frame.apply_moving_std(input_column='test', dest_column='test_moving_std', row_range=(0, None), window=5)
```
result :
```
     test  test_moving_median
0   5.299            0.000000
1   6.982            0.000000
2   5.363            0.000000
3   8.653            0.000000
4   3.321            1.791522
5   7.959            1.917570
6   8.738            2.130770
7   7.563            2.010980
8   5.134            2.011469
9   3.178            2.057566
10  5.374            1.951671
```

#### 5. Moving Probability
Calculate probability for a given window

example :
```
# Apply moving probability
data_frame.apply_moving_probability(input_column='test', dest_column='test_moving_probability', row_range=(0, None), window=10, no_of_bins=5)
```
result :
```
     test  test_moving_median
0   5.299                 0.0
1   6.982                 0.0
2   5.363                 0.0
3   8.653                 0.0
4   3.321                 0.0
5   7.959                 0.0
6   8.738                 0.0
7   7.563                 0.0
8   5.134                 0.0
9   3.178                 0.2
10  5.374                 0.3
11  6.431                 0.1
12  6.299                 0.2
13  4.982                 0.3
14  5.363                 0.4
15  6.653                 0.2
16  7.321                 0.2
17  7.959                 0.2
18  6.338                 0.4
```

#### 6. Moving Entropy
 Calculate entropy sum for a given window

example :
```
# Apply moving entropy
data_frame.apply_moving_entropy(input_column='test', dest_column='test_moving_entropy', row_range=(0, None), window=10, no_of_bins=5)
```
result :
```
     test  test_moving_entropy
0   5.299             0.000000
1   6.982             0.000000
2   5.363             0.000000
3   8.653             0.000000
4   3.321             0.000000
5   7.959             0.000000
6   8.738             0.000000
7   7.563             0.000000
8   5.134             0.000000
9   3.178             1.366159
10  5.374             1.366159
11  6.431             1.504788
12  6.299             1.557113
13  4.982             1.557113
14  5.363             1.470808
15  6.653             1.470808
16  7.321             1.279854
17  7.959             1.504788
18  6.338             1.470808
```

#### 7. Moving K-Closest Average
Calculate K nearest average for the last element at a given window

example :
```
# Apply moving k closest average
data_frame.apply_moving_k_closest_average(input_column='test', dest_column='test_moving_k_closest', row_range=(0, None), window=5, kclosest=3)
```
result :
```
     test  test_moving_k_closest
0   5.299               0.000000
1   6.982               0.000000
2   5.363               0.000000
3   8.653               0.000000
4   3.321               4.661000
5   7.959               7.864667
6   8.738               8.450000
7   7.563               8.058333
8   5.134               5.339333
9   3.178               5.291667
10  5.374               6.023667
11  6.431               6.456000
12  6.299               6.034667
13  4.982               5.551667
14  5.363               5.239667
15  6.653               6.461000
16  7.321               6.757667
17  7.959               7.311000
18  6.338               6.118000
```

#### 8. Moving Median Centered Average
Calculate the average around the median for a given window

example :
```
# Apply moving median centered average
data_frame.apply_moving_median_centered_average(input_column='test', dest_column='test_moving_med_cent_avg', row_range=(0, None), window=5, boundary=1)
```
result :
```
     test  test_moving_med_cent_avg
0   5.299                  0.000000
1   6.982                  0.000000
2   5.363                  0.000000
3   8.653                  0.000000
4   3.321                  5.881333
5   7.959                  6.768000
6   8.738                  7.325000
7   7.563                  8.058333
8   5.134                  6.885333
9   3.178                  6.885333
10  5.374                  6.023667
11  6.431                  5.646333
12  6.299                  5.602333
13  4.982                  5.551667
14  5.363                  5.678667
15  6.653                  6.031000
16  7.321                  6.105000
17  7.959                  6.445667
18  6.338                  6.770667
```

#### 9. Moving Threshold Average
Calculate average and check the difference between the calculated value and the last element in the given window. If it is under certain threshold, then calculated valu will be apply. Or else origin value will be applied.

example :
```
# Apply moving threshold average
data_frame.apply_moving_threshold_average(input_column='test', dest_column='test_moving_threshold_avg', row_range=(0, None), window=5, threshold=2)
```
result :
```
     test  test_moving_med_cent_avg
0   5.299                    0.0000
1   6.982                    0.0000
2   5.363                    0.0000
3   8.653                    0.0000
4   3.321                    3.3210
5   7.959                    6.4556
6   8.738                    6.8068
7   7.563                    7.2468
8   5.134                    6.5430
9   3.178                    3.1780
10  5.374                    5.9974
11  6.431                    5.5360
12  6.299                    5.2832
13  4.982                    5.2528
14  5.363                    5.6898
15  6.653                    5.9456
16  7.321                    6.1236
17  7.959                    6.4556
18  6.338                    6.7268
```

### Charts
Only for numerical visualization.

example :
```
from featureeng.presenting import Chart

data_frame = Frame('test.csv')

data_frame.apply_moving_average(input_column='test', dest_column='test_moving_avg', row_range=(0, None), window=5)
data_frame.apply_moving_std(input_column='test', dest_column='test_moving_std', row_range=(0, None), window=5)

Chart.presentData(data_frame=data_frame, columns=['test', 'test_moving_avg'])
```
![ ](https://github.com/roshanmadhushanka/FeatureProcessor/blob/master/resources/figure.png  "Chart")

