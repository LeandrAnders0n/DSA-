#Question:Roman to Integer
#Approach: Use a Hash Table to map the roman numerals to its integer value
#Loop through the roman numeral and add or subtract the corresponding integer value, basis of the position of the
#roman numeral, ie where a smaller numeral before a larger numeral indicates subtraction, while otherwise, it indicates addition.
#The time complexity of the code is O(n)
#The space complexity of the code is O(1) 


def roman_to_integer(roman_number):
    roman_values={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    integer_value=0

    for i in range(0,len(roman_number)-1):
        if roman_values[roman_number[i]]<roman_values[roman_number[i]]:
            integer_value-=roman_values[roman_number[i]]
        else:
            integer_value+=roman_values[roman_number[i]]
    return integer_value+roman_values[roman_number[-1]]


print(roman_to_integer("LVIII"))
