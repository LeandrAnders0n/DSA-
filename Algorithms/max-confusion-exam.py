#Question:Maximize the Confusion of an Exam
#A teacher is writing a test with n true/false questions, with 'T' denoting true and 'F' denoting false. He wants to confuse the students by maximizing the number of consecutive questions with the same answer (multiple trues or multiple falses in a row).
# You are given a string answerKey, where answerKey[i] is the original answer to the ith question. In addition, you are given an integer k, the maximum number of times you may perform the following operation:
# Change the answer key for any question to 'T' or 'F' (i.e., set answerKey[i] to 'T' or 'F')
# Return the maximum number of consecutive 'T's or 'F's in the answer key after performing the operation at most k times.

#Approach: Sliding Window

def max_confusion(answerKey,k):
    # Store the count in the current sliding window
    count = {"T": 0, "F": 0}
    # Max count
    max_result = 0
    # Left Pointer
    left = 0
    # Temporary max count
    result = 0
    for right in range(len(answerKey)):
        # Increment dictionary count
        count[answerKey[right]] += 1
        # If count of both 'T' and 'F' is more than 'K', ove the left pointer and decrement the left pointer's value
        while count["T"] > k and count["F"] > k:
            count[answerKey[left]] -= 1
            left += 1
        # Sum of 'T' and 'F' values
        result = count["T"] + count["F"]
        # Max count of all values
        max_result = max(max_result, result)
    return max_result


answerKey = "TTFTTFTT"
k = 1
# Output: 5
print(max_confusion(answerKey,k))

answerKey = "TTFF"
k = 2
# Output: 4
print(max_confusion(answerKey,k))

answerKey = "TFFT"
k = 1
# Output: 3
print(max_confusion(answerKey,k))