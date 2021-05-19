# bonus.py
"""Count, Sum, Mean, Median and Mode of 100+ Set of Data"""

# Initilization
import statistics
data_set = [*range(51), *range(50,1001,10)] #This will display list as 0-50, and 50-1001 by multiples of ten, with 50 being only value repeated twice
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
print('Data_Set = 0-50, by multiples of 1, and 50-1000 by multiples of 10')
print('1. Count =', count_data_set)
print('2. Sum = ', set_sum)
print('3. Mean =', mean)
print('4. Median =', median)
print('5. Mode =', mode)
