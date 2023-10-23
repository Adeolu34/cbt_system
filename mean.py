#input to calculate the mean, mode and median of any input
L = input("Enter your dataset separated by spaces: ")
calc = L.split()
math = [int(num) for num in calc if num.isdigit()]
sorteddata = sorted(math)
Num = all(isinstance(item, int) for item in math)
if Num:
     print("please wait")
else:
     print("There is a non integer in your dataset")
#to calculate the median
medianCounter = len(sorteddata)
holder1 = round(medianCounter/2)
index1 = holder1 - 1
index2 = holder1
if medianCounter%2 == 0 :     
     median = (sorteddata[index1] + sorteddata[index2])/2
     print("The median is: " + str(median))
elif medianCounter%2 > 0:
     median = sorteddata[index2]
     print("The median is: " + str(median))
#calculate the mean of an input
meanEntry = sum(sorteddata)
mean = meanEntry/medianCounter
print("The mean is: " + str(mean))
#calculate the mode
count = {}
for num in sorteddata:
     if num in count:
          count[num] += 1
     else:
          count[num] = 1
mode = max(count, key=count.get)
print("The mode is: " + str(mode))
