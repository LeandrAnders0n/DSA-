#Question:Count Days Spent Together
# Alice and Bob are traveling to Rome for separate business meetings.
# You are given 4 strings arriveAlice, leaveAlice, arriveBob, and leaveBob. Alice will be in the city from the dates arriveAlice to leaveAlice (inclusive), while Bob will be in the city from the dates arriveBob to leaveBob (inclusive). Each will be a 5-character string in the format "MM-DD", corresponding to the month and day of the date.
# Return the total number of days that Alice and Bob are in Rome together.
# You can assume that all dates occur in the same calendar year, which is not a leap year. Note that the number of days per month can be represented as: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31].

#Approach:
# The code calculates the total number of days that Alice and Bob are in Rome together by finding the overlapping days between their respective arrival and departure dates. It uses Python's datetime module to convert the date strings to Python date objects for proper comparison.
# Time and Space Complexity: O(1)

from datetime import datetime

def countDaysTogether(arriveAlice, leaveAlice, arriveBob,leaveBob):
    start_Alice = datetime.strptime(arriveAlice, "%m-%d")
    end_Alice = datetime.strptime(leaveAlice, "%m-%d")
    start_Bob = datetime.strptime(arriveBob, "%m-%d")
    end_Bob = datetime.strptime(leaveBob, "%m-%d")
    # Find the overlapping days between their visits
    overlap_start = max(start_Alice, start_Bob)
    overlap_end = min(end_Alice, end_Bob)
    # Calculate the total number of days they are in Rome together
    total_days_together = max(0, (overlap_end - overlap_start).days + 1)
    return total_days_together

arriveAlice,leaveAlice,arriveBob, leaveBob  = "10-01","10-31","11-01","12-31"
print(countDaysTogether(arriveAlice,leaveAlice,arriveBob, leaveBob))
# Output: 0

arriveAlice,leaveAlice,arriveBob, leaveBob = "08-15","08-18", "08-16","08-19"
print(countDaysTogether(arriveAlice,leaveAlice,arriveBob, leaveBob))
# Output: 3