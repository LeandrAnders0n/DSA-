#Question: Can Place Flowers
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

#Approach:
# Add leading and trailing zeros to the flowerbed to simplify boundary checks, then iterate through the modified array to plant flowers in empty plots that meet the criteria. If we are successfully able to plant all required flowers, returns True; otherwise, return False.

# Time complexity: O(N)
# Space complexity: O(1)

def can_place_flowers(flowerbed,n):
    flowerbed=[0]+flowerbed+[0]
    for i in range(1,len(flowerbed)-1):
        if flowerbed[i]==0 and flowerbed[i-1]==0 and flowerbed[i+1]==0:
            n-=1
            flowerbed[i]=1
    return True if n<=0 else False

flowerbed = [1,0,0,0,1] 
n = 1
# Output: true
print(can_place_flowers(flowerbed,n))
flowerbed = [1,0,0,0,1] 
n = 2
# Output: false
print(can_place_flowers(flowerbed,n))
