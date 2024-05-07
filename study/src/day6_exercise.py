
'''
1. Create an empty tuple
2. Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
3. Join brothers and sisters tuples and assign it to siblings
4. How many siblings do you have?
5. Modify the siblings tuple and add the name of your father and mother and assign it to family_members

6. Unpack siblings and parents from family_members
7. Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
8. Change the about food_stuff_tp tuple to a food_stuff_lt list
9. Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list.
10. Slice out the first three items and the last three items from food_staff_lt list
11. Delete the food_staff_tp tuple completely
12. Check if an item exists in tuple:
    - Check if 'Estonia' is a nordic country
    - Check if 'Iceland' is a nordic country
    
    nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
'''
# 1.
# empty_tuple = ()
empty_tuple = tuple()
# 2.
sisters = ('Emily', 'Sophia', 'Chloe')
brothers = ('Alex', 'Brian', 'Daniel')
siblings = sisters + brothers
# 4. 
print(len(siblings))
# 5.
family_members = siblings + ('David', 'Emma')
# 6.
siblings, parents = family_members[:3], family_members[3:]
# 7.
fruits = ('apple', 'banana', 'orange')
vegetables = ('carrot', 'broccoli', 'cucumber')
animal_products = ('milk', 'eggs', 'cheese')
food_stuff_tp = fruits + vegetables + animal_products
# 8.
food_stuff_lt = list(food_stuff_tp)
# 9.
print(food_stuff_lt[len(food_stuff_lt)//2])
# 10.
print(food_stuff_lt[:3])
print(food_stuff_lt[-3:])
# 11.
del food_stuff_tp
# 12.
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Norway' in nordic_countries:
    print(1)
    
