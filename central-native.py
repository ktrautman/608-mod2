# central-native.py
"""Count, Sum, Mean, Median and Mode of Data Set"""

# Initilization
data_set = [47, 95, 88, 73, 88, 84]
count_data_set = len(data_set)
set_sum = sum(data_set)

# Processing
    #MEAN
mean = set_sum / count_data_set
    #MEDIAN
if count_data_set % 2 == 0: # If Data_set contains even number of items
    median_lower = (sorted(data_set)[count_data_set//2])
    median_upper = (sorted(data_set)[count_data_set//2 - 1])
    median = (median_upper + median_lower)/2
else: 
    median = (sorted(data_set)[count_data_set//2]) # If Data_set contains off number of items
    #MODE
def mode(data_set):
    return max(set(data_set), key=data_set.count)

# Termination / Display
print('1. Count =', count_data_set)
print('2. Sum = ', set_sum)
print('3. Mean =', mean)
print('4. Median =', median)
print('5. Mode =', mode(data_set))

 