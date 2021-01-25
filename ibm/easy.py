#20. Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

def isValid(self, s: str) -> bool:
    match = {"}":"{" , "]":"[" , ")":"("}
    stack = []
    isEmpty = lambda x : x == []
    for i in s:

        if i == "[" or i == "{"  or i == "(":
            stack.append(i)
        else:
            if  isEmpty(stack):
                return False
            if stack[-1] == match[i] :
                stack.pop()
            else:
                return False
    return isEmpty(stack)

#21 Merge Two Sorted Lists

def mergeTwoLists(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    if not l1 or not l2:
        return l2 or l1

    if l1.val < l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
    


#169. Majority Element
def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:
            return nums[0]
        maxi= 0
        result = 0
        res = {}
        for i in nums:
            if res.get(i):
                res[i]+=1
                if res[i]>=maxi:
                    maxi = res[i]
                    result =i
            else:
                res[i]=1
        return result

#268. Missing Number

##Gauss' Formula 
def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    return (n*(n+1)/2) - sum(nums)

## hashset solution 
def missingNumber(self, nums):
    num_set = set(nums)
    n = len(nums) + 1
    for number in range(n):
        if number not in num_set:
            return number
    
#788 Rotated Digits

def rotatedDigits(self, N):
    count = 0
    for d in range(1, N+1):
        d = str(d)
        if '3' in d or '4' in d or '7' in d:
            continue
        if '2' in d or '5' in d or '6' in d or '9' in d:
            count+=1
    return count


#1518. Water Bottles

def numWaterBottles(self, numBottles, numExchange):
    """
    :type numBottles: int
    :type numExchange: int
    :rtype: int
    """
    empty = numBottles
    result = numBottles 
    while True:
        if empty//numExchange >0:
            result += empty//numExchange
            empty= empty % numExchange +empty//numExchange
        else: 
            return result

        
