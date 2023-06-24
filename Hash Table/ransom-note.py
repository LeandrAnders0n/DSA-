#Question:Ransom Note
#Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
# Each letter in magazine can only be used once in ransomNote.

#Appraoach:The code uses two dictionaries, ransomNoteFreq and magazineFreq, to store the frequency of each letter in the ransom note and magazine strings, respectively. It then iterates over each letter in the ransom note, subtracts its frequency from the corresponding letter in the magazine, and checks if the frequency becomes negative. If it does, it means there are not enough letters in the magazine to construct the ransom note, and it returns False. If the iteration completes without any negative frequencies, it means the ransom note can be constructed, and it returns True.


# Time Complexity: O(N + M), where N is the length of the ransom note string and M is the length of the magazine string
# Space Complexity: O(N)

def canConstruct(ransomNote, magazine):
    ransomNoteFreq={}
    magazineFreq={}

    for char in magazine:
        magazineFreq[char]=magazineFreq.get(char,0)+1

    for char in ransomNote:
        magazineFreq[char]=magazineFreq.get(char,0)-1

        if magazineFreq[char]<0:
            return False
    return True









ransomNote = "aa"
magazine = "aab"
# Expected Output: True
print(canConstruct(ransomNote, magazine))  

ransomNote = "aa"
magazine = "ab"
#Expected Output: False
print(canConstruct(ransomNote, magazine))  
