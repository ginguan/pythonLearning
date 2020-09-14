'''
One year IBM interview question 
'''



'''
259. 3Sum Smaller

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]

'''
#use pointer left right mid
def threeSumSmaller(self, nums, target):
    count = 0
    nums.sort()
    for i in range(len(nums)):
        j, k = i+1, len(nums)-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s < target:
                # if (i,j,k) works, then (i,j,k), (i,j,k-1),..., 
                # (i,j,j+1) all work, totally (k-j) triplets
                count += k-j
                j += 1
            else:
                k -= 1
    return count
'''
1355. Activity Participants


'''
'''
1. Two Sum

Given an array of integers nums and and integer target, return the indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1]
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

'''
def twoSum(self, nums: List[int], target: int) -> List[int]:
    lookup = {}
    for index, item in enumerate(nums):
        if(target - item) in lookup:
            return [lookup[target-item],index]
        else:
            lookup[item] = index
            
'''
157. Read N Characters Given Read4

Given a file and assume that you can only read the file using a given method read4, implement a method to read n characters.

 

Method read4:

The API read4 reads 4 consecutive characters from the file, then writes those characters into the buffer array buf.

The return value is the number of actual characters read.

Note that read4() has its own file pointer, much like FILE *fp in C.

Definition of read4:

    Parameter:  char[] buf4
    Returns:    int

Note: buf4[] is destination not source, the results from read4 will be copied to buf4[]

'''


'''
949. Largest Time for Given Digits

Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00, a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.

 

Example 1:

Input: [1,2,3,4]
Output: "23:41"
Example 2:

Input: [5,5,5,5]
Output: ""

A.length == 4
0 <= A[i] <= 9
'''
'''
itertools.permutations(A)

https://docs.python.org/3/library/itertools.html

'''
def largestTimeFromDigits(self, A):
    return max(["%d%d:%d%d" % t for t in itertools.permutations(A) if t[:2] < (2, 4) and t[2] < 6] or [""])
    
def largestTimeFromDigits(self, A: List[int]) -> str:
    output = ""
    if min(A) >2:
        return ""
    max_time = -1
    for h, i,j,k in itertools.permutations(A):
        hour = h*10 +i
        minute = j *10 +k
        if hour <24 and minute <60:
            max_time = max(max_time,hour*60 + minute)
    if max_time == -1:
        return ""
    else:
        return "{:02d}:{:02d}".format(max_time // 60, max_time % 60)
        #output = str(hour)+":"+str(minute) will get error for 00:00
        
'''
if permutation not avaliable
'''
def perm(a, k=0):
    if k == len(a):
        print(a)
    else:
        for i in range(k, len(a)):
            a[k], a[i] = a[i] ,a[k]
            perm(a, k+1)
            a[k], a[i] = a[i], a[k]

            
            
'''
20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''
def isValid(self, s: str) -> bool:
        while "{}" in s or "()" in s or "[]" in s:
            if '{}' in s:
                s=s.replace('{}','')
                print(s)
                print('{}')
            if '()' in s:
                s=s.replace('()','')
                print('()')
            if '[]' in s:
                s=s.replace('[]','')
                print('[]')
            #print(s.replace('a', ''))
        if s == "" :
            return True
        else:
            return False
        
        
'''
1151. Minimum Swaps to Group All 1's Together

Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array together in any place in the array.

 

Example 1:

Input: data = [1,0,1,0,1]
Output: 1
Explanation: 
There are 3 ways to group all 1's together:
[1,1,1,0,0] using 1 swap.
[0,1,1,1,0] using 2 swaps.
[0,0,1,1,1] using 1 swap.
The minimum is 1.
Example 2:

Input: data = [0,0,0,1,0]
Output: 0
Explanation: 
Since there is only one 1 in the array, no swaps needed.
Example 3:

Input: data = [1,0,1,0,1,0,0,1,1,0,1]
Output: 3
Explanation: 
One possible solution that uses 3 swaps is [0,0,0,0,0,1,1,1,1,1,1].
Example 4:

Input: data = [1,0,1,0,1,0,1,1,1,0,1,0,0,1,1,1,0,0,1,1,1,0,1,0,1,1,0,0,0,1,1,1,1,0,0,1]
Output: 8
'''
 def minSwaps(self, data: List[int]) -> int:
        numOf0 = data.count(0)
        numOf1 = data.count(1)
        
        count = 0;
        for i in range(numOf0):
            if (data[i]==1):
                count = count+1
        return count
            