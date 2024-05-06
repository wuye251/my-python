lst = []
# 2.
lst2 = [1,2,3,4,5,6,7,8]
# 3.
length = len(lst2)
# 4.
first, middle, last = lst2[0], lst2[length//2], lst2[-1]
# 5.
mixed_data_types = ['John', 25, 1.75, 'Single', '123 Main St']
# 6.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'Ibm', 'Oracle' ,'Amazon']
# 7.
print(it_companies)
# 8.
for i in it_companies:
    print(i)
# 9.
print(it_companies[0], it_companies[len(it_companies)//2], it_companies[-1])
# 10.
it_companies[0] = "HHG"
print(it_companies)
# 11.
it_companies.append("HHG2")
# 12.
it_companies.insert(len(it_companies)//2, "HHG3")
# 13.
it_companies = [i.upper() for i in it_companies if i != "Ibm"]
# 14.
it_companies = it_companies+["#"]
# 15.
does_exist = "HHG" in it_companies
print(does_exist)
# 16.
it_companies.sort()
print("sort:",it_companies)
# 17.
it_companies.reverse()
print("reverse:",it_companies)
# 18.
it_companies.pop(3)
print("first 3:",it_companies)
# 19.
it_companies.pop(-3)
print("last 3:",it_companies)
# 20.
it_companies.pop(len(it_companies)//2)
print("middle:",it_companies)
# 21.
it_companies.pop(0)
print("remove first:",it_companies)
# 22.
it_companies.pop(len(it_companies)//2)


'''
Exercises: Level 2
1. The following is a list of 10 students ages:
    ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
    - Sort the list and find the min and max age
    - Add the min age and the max age again to the list
    - Find the median age (one middle item or two middle items divided by two)
    - Find the average age (sum of all items divided by their number )
    - Find the range of the ages (max minus min)
    - Compare the value of (min - average) and (max - average), use abs() method
2. Find the middle country(ies) in the countries list
3. Divide the countries list into two equal lists if it is even if not one more country for the first half.
3. ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. Unpack the first three countries and the rest as scandic countries.
'''

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print("Sorted ages:", ages)
min_age, max_age = ages[0], ages[-1]
print("Min age:", min_age)
print("Max age:", max_age)
ages.extend([min_age, max_age])
print("Extended ages:", ages)
median_index = len(ages) // 2
if len(ages) % 2 == 0:
    median_age = (ages[median_index - 1] + ages[median_index]) / 2
else:
    median_age = ages[median_index]
print("Median age:", median_age)
average = sum(ages) / len(ages)
print("Average age:", average)
range_age = max_age - min_age
print("Range of ages:", range_age)

countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("middle countries:", countries[len(countries)//2])
