# Question: Ancestral Names
# In some cultures, children are named after ancestors and there is a number following which represents how many ancestors have shared that name. They are often shown as Roman Numerals.
# In Roman numerals, a value is not repeated more than three times. At that point, a smaller value precedes a larger value to indicate subtraction. For example, the letter I represents the number 1, and represents 5. Reason through the formation of 1 to 10 below, and see how it is applied in the following lines.
# •I represents 1,'V' represent 5, 'X' represents 10 and'L' represents 50
# • XX XXX XL and L are 20. 30. 40 and 50.
# Given a list of strings comprised of a name and a Roman numeral, sort the list first by name, then by decimal value of the Roman numeral.
# For example, If you are given the names [Steven XL Steven XVI, David IX, Mary XV, Mary XIII, Mary XX] the result of the sort is [David IX, Mary XIII, Mary XV, Mary XX, Steven XVI, Steven XL]. The result with Roman numerals is the expected return value. Written with the numbers in decimal, they are [David 9, Mary 13, Mary 15, Mary 20, Steven 16, Steven 40]

# Approach:
# Function `ancestral_names` takes a list of names and Roman numerals, and sorts it first by name and then by the decimal value of the Roman numeral using a custom sorting function. Also, include a function `roman_to_decimal` for the Roman numeral to decimal conversion. The custom sorting function `custom_sort` splits each input string into name and Roman numeral parts, sorts by name, and then by the decimal value of the Roman numeral.

# Time Complexity: The time complexity is O(N * M * log(N)) where N is the number of names, and M is the average length of the Roman numerals in characters due to sorting.
# Space Complexity: O(N)

# Function to convert a Roman numeral to its decimal value
def roman_to_decimal(roman):
    roman_dict={'I':1,'V':5,'X':10,'L':50}
    decimal=0
    prev_value=0

    for numeral in reversed(roman):
        value=roman_dict[numeral]

        if value<prev_value:
            decimal-=value
        else:
            decimal+=value
        prev_value=value
    return decimal

# Custom sorting function
def custom_sort(name_roman):
    # Split the input string into name and Roman numeral
    name,roman=name_roman.split()
    return (name,roman_to_decimal(roman))
# Function to sort the list of names and Roman numerals
def ancestral_names(names):
    # Sort the list first by name, then by decimal value of the Roman numeral
    sorted_names=sorted(names,key=custom_sort)
    return sorted_names

names= ["Steven XL", "Steven XVI", "David IX", "Mary XV", "Mary XIII", "Mary XX"]
# Output:[David IX, Mary XIII, Mary XV, Mary XX, Steven XVI, Steven XL]
print(ancestral_names(names))
