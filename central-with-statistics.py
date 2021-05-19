# central-with-statistics.py
"""Count, Sum, Mean, Median and Mode of Data Set Using Statistics Module"""

# Initilization
import statistics
data_set = [47, 95, 88, 73, 88, 84]
count_data_set = len(data_set)
set_sum = sum(data_set)

# Processing
    #MEAN
mean = statistics.mean(data_set)
    #MEDIAN
median = statistics.median(data_set)
    #MODE
mode = statistics.mode(data_set)

# Termination / Display
print('1. Count =', count_data_set)
print('2. Sum = ', set_sum)
print('3. Mean =', mean)
print('4. Median =', median)
print('5. Mode =', mode)
