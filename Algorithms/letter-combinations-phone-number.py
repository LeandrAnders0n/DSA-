#Question:Letter Combinations of a Phone Number
#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#Approach: Backtracking
#Use backtracking to find all possible letter combinations from a given phone number's digits. Recursively explore and construct combinations, appending them to the final list "res." 

# Time Complexity and Space Complexity: O(2^n)

def letter_combinations(digits):
    if not digits:
        return []
    
    phone_dict={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    res=[]
    def backtrack(combination,next_digits):
        if not next_digits:
            res.append(combination)
            return
        
        for letter in phone_dict[next_digits[0]]:
            backtrack(combination+letter,next_digits[1:])
    
    backtrack("",digits)
    return res

digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(letter_combinations(digits))

digits = "2"
# Output: ["a","b","c"]
print(letter_combinations(digits))