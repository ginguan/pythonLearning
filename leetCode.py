'''
359. Logger Rate Limiter
Qs: 
Logger Rate Limiter

Design a logger system that receive stream of messages along with its timestamps, each message should be printed if and only if it is not printed in the last 10 seconds.
过去十秒都都没有print 过或者 是新的message
Given a message and a timestamp (in seconds granularity), return true if the message should be printed in the given timestamp, otherwise returns false.

It is possible that several messages arrive roughly at the same time.
solution:
https://leetcode.com/articles/logger-rate-limiter/
'''
#solution :
'''
Algo explaination:

- We initialize a hashtable/dictionary to keep the messages along with the timestamp.

- At the arrival of a new message, the message is eligible to be printed with either of the two conditions as follows:

    case 1). we have never seen the message before.

    case 2). we have seen the message before, and it was printed more than 10 seconds ago.

- In both of the above cases, we would then update the entry that is associated with the message in the hashtable, with the latest timestamp.
'''
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_dict = {}
        #using hashtable/dictionary to store message
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        if message not in self._msg_dict:
            # case 1). add the message to printl, never seen the msg
            self._msg_dict[message] = timestamp
            return True

        if timestamp - self._msg_dict[message] >= 10: #not printed in last 10s
            # case 2). update the timestamp of the message
            self._msg_dict[message] = timestamp
            return True
        else:
            return False

'''
I/O
    Logger logger = new Logger();

    // logging string "foo" at timestamp 1
    logger.shouldPrintMessage(1, "foo"); returns true; 

    // logging string "bar" at timestamp 2
    logger.shouldPrintMessage(2,"bar"); returns true;

    // logging string "foo" at timestamp 3
    logger.shouldPrintMessage(3,"foo"); returns false;
'''

'''
520. Detect Capital
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
'''
import re
#using library easily implement using format

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return re.fullmatch(r"[A-Z]*|.[a-z]*", word

'''
705. Design HashSet

https://leetcode.com/articles/design-hashset/
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

    All values will be in the range of [0, 1000000].
    The number of operations will be in the range of [1, 10000].
    Please do not use the built-in HashSet library.

ex.
MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

'''

class MyHashSet(object):

#add, remove, contains method in Hash set
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.keyRange = 769
        self.bucketArray = [Bucket() for i in range(self.keyRange)]

    def _hash(self, key):
        return key % self.keyRange

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].insert(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        bucketIndex = self._hash(key)
        self.bucketArray[bucketIndex].delete(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        bucketIndex = self._hash(key)
        return self.bucketArray[bucketIndex].exists(key)

#set node
class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.next = nextNode
#set bucket --> node lise
class Bucket:
    def __init__(self):
        # a pseudo head
        self.head = Node(0)

    def insert(self, newValue):
        # if not existed, add the new element to the head.
        if not self.exists(newValue):
            newNode = Node(newValue, self.head.next)
            # set the new head.
            self.head.next = newNode

    def delete(self, value):
        prev = self.head
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # remove the current node
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next

    def exists(self, value):
        curr = self.head.next
        while curr is not None:
            if curr.value == value:
                # value existed already, do nothing
                return True
            curr = curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

'''
125. Valid Palindrome

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        #using pointer
        i,  j =0, len(s)-1
        while i <j:
            '''
            isalnum()
            True if all characters in the string are alphanumeric
            '''
            while i <j and not s[i].isalnum():
                i +=1
            while i <j and not s[j].isalnum():
                j -=1
            
            if i<j and s[i].lower() != s[j].lower():
                return False
            
            i += 1
            j -=1
            
        return True
                            
                            
'''
342. Power of Four

Given an integer (signed 32 bits), write a function to check whether it is a power of 4.


'''
 def isPowerOfTwo(self, n):
    if n == 0:
        return False
    while n % 4 == 0:
        n /= 4
    return n == 1
                            
def isPowerOfFour(self, num: int) -> bool:
    return num > 0 and num & (num - 1) == 0 and num % 3 == 1
                            
'''
211. Add and Search Word - Data structure design

Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

You may assume that all words are consist of lowercase letters a-z.
'''
                            
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}
        

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie
        
        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node['$'] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """
        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == '.':
                        for x in node:
                            if x != '$' and search_in_node(word[i + 1:], node[x]):
                                return True
                    # if no nodes lead to answer
                    # or the current character != '.'
                    return False
                # if the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return '$' in node
            
        return search_in_node(word, self.trie)
                            
'''
442. Find All Duplicates in an Array
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.
'''
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        checked=[]
        result = []
        for i in nums:
            if i in checked:
                result.append(i)
            checked.append(i)
        return result

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        checked=set()
        result = []
        for i in nums:
            if i in checked:
                result.append(i)
            checked.add(i)
        return result
                            
class Solution(object):
    def findDuplicates(self, nums):
        ans = []
        for num in nums:
            if nums[abs(num)-1] < 0:
                ans.append(abs(num))
            else:
                nums[abs(num)-1] *= -1
        return ans
                            
from collections import Counter
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        nums2 = Counter(nums)
        return set(i for i in nums2 if nums2[i]>1)
                            
                            
'''
144. Binary Tree Preorder Traversal
https://leetcode.com/explore/learn/card/data-structure-tree/134/traverse-a-tree/928/

Pre-order traversal is to visit the root first. Then traverse the left subtree. Finally, traverse the right subtree.

In-order traversal is to traverse the left subtree first. Then visit the root. Finally, traverse the right subtree.

Post-order traversal is to traverse the left subtree first. Then traverse the right subtree. Finally, visit the root.
'''
class TreeNode(object):
""" Definition of a binary tree node."""
def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

def preorderTraversal(self, root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """
    if root is None:
        return []

    stack, output = [root, ], []

    while stack:
        root = stack.pop()
        if root is not None:
            output.append(root.val)
            if root.right is not None:
                stack.append(root.right)
            if root.left is not None:
                stack.append(root.left)

    return output
                            
'''inorder traversal'''
def inorderTraversal(self, root):
    if not root:
        return []
    return self.inorderTraversal(root.left)+ [root.val] + self.inorderTraversal(root.right) 

'''postorder'''
def postorderTraversal(self, root: TreeNode) -> List[int]:
    #left->right->root
    if not root:
        return []
    return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val]                     
'''
270. Closest Binary Search Tree Value
Given a non-empty binary search tree and a target value, find the value in the BST that is closest to the target.

Note:

Given target value is a floating point.
You are guaranteed to have only one unique value in the BST that is closest to the target.
Example:

Input: root = [4,2,5,1,3], target = 3.714286

    4
   / \
  2   5
 / \
1   3

Output: 4

'''
                            # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#import sys

class Solution:

    def closestValue(self, root: TreeNode, target: float) -> int:
        diff = abs(target -root.val) 
        result = root.val
        #closest = min(root.val, closest, key = lambda x: abs(target - x))
        #root = root.left if target < root.val else root.right
        while root:
            if abs(target -root.val) < diff:
                result = root.val
                diff = abs(target -root.val) 
            root = root.left if target < root.val else root.right
        return result

'''
437. Path Sum III
You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

Example:

root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11

'''
def pathSum(self, root: TreeNode, sum: int) -> int:
    def preorder(node: TreeNode, curr_sum) -> None:
        nonlocal count
        if not node:
            return 

        # current prefix sum
        curr_sum += node.val

        # here is the sum we're looking for
        if curr_sum == k:
            count += 1

        # number of times the curr_sum − k has occurred already, 
        # determines the number of times a path with sum k 
        # has occurred up to the current node
        count += h[curr_sum - k]

        # add the current sum into hashmap
        # to use it during the child nodes processing
        h[curr_sum] += 1

        # process left subtree
        preorder(node.left, curr_sum)
        # process right subtree
        preorder(node.right, curr_sum)

        # remove the current sum from the hashmap
        # in order not to use it during 
        # the parallel subtree processing
        h[curr_sum] -= 1

    count, k = 0, sum
    h = defaultdict(int)
    preorder(root, 0)
        return count
                            
'''
994. Rotting Oranges

In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
'''
                            
def orangesRotting(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """

    def getNeighbor(x, y, v):
        neighbors = []
        if x > 0 and grid[x-1][y] == v:
            neighbors.append((x-1,y))
        if x < len(grid)-1 and grid[x+1][y] == v:
            neighbors.append((x+1,y))
        if y > 0 and grid[x][y-1] == v:
            neighbors.append((x,y-1))
        if y < len(grid[0])-1 and grid[x][y+1] == v:
            neighbors.append((x,y+1))
        return neighbors

    fresh_count, minutes, rottens = 0, 0, []
    for r in xrange(len(grid)):
        for c in xrange(len(grid[r])):
            if grid[r][c] == 1:
                fresh_count += 1
                neighbor_rotten = getNeighbor(r, c, 2)
                if len(neighbor_rotten) > 0:
                    rottens.append((r,c))
                    grid[r][c] = 3 # previously fresh, not rotten

    if fresh_count == 0:
        return 0

    while len(rottens) > 0:
        minutes += 1
        fresh_count -= len(rottens)
        next_rottens = []
        for x, y in rottens:
            for u, v in getNeighbor(x,y,1):
                next_rottens.append((u, v))
                grid[u][v] = 3
        rottens = next_rottens

    return -1 if fresh_count > 0 else minutes
                            
                            
'''
171. Excel Sheet Column Number

Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
Example 1:

Input: "A"
Output: 1
Example 2:

Input: "AB"
Output: 28
Example 3:

Input: "ZY"
Output: 701
'''
                            
def titleToNumber(self, s: str) -> int:
    '''
    Scanning AZZC from right to left while accumulating results:

    First, ask the question, what the value of 'C' is:
    'C' = 3 x 260 = 3 x 1 = 3
    result = 0 + 3 = 3
    Then, ask the question, what the value of 'Z*' is:
    'Z*' = 26 x 261 = 26 x 26 = 676
    result = 3 + 676 = 679
    Then, ask the question, what the value of 'Z**' is:
    'Z**' = 26 x 262 = 26 x 676 = 17576
    result = 679 + 17576 = 18255
    Finally, ask the question, what the value of 'A***' is:
    'A***' = 1 x 263 = 1 x 17576 = 17576
result = 18255 + 17576 = 35831
    '''
    #ord() returns an integer for Unicode character
    result = 0
    n  = len(s)
    for i in range(n):
        result += (ord(s[i])+1- ord('A')) * pow(26,n-i-1)
    return result
                            
'''
274. H-Index

H-Index

Solution
Given an array of citations (each citation is a non-negative integer) of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia: "A scientist has index h if h of his/her N papers have at least h citations each, and the other N − h papers have no more than h citations each."

Example:

Input: citations = [3,0,6,1,5]
Output: 3 
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had 
             received 3, 0, 6, 1, 5 citations respectively. 
             Since the researcher has 3 papers with at least 3 citations each and the remaining 
             two with no more than 3 citations each, her h-index is 3.
Note: If there are several possible values for h, the maximum one is taken as the h-index.
'''
                            
def hIndex(arr):

  if not arr:
      return 0
  n = len(arr)
  arr.sort(reverse=True)
  i = 0
  while i<n and arr[i]>i:
      i+=1
  return i
                            
'''
119. Pascal's Triangle II

Given an integer rowIndex, return the rowIndexth row of the Pascal's triangle.

Notice that the row index starts from 0.
'''
def getRow(self, rowIndex: int) -> List[int]:
    triangle = [[1],[1,1]]
    for i in range(2, rowIndex+1):
        temp = [None]*(i+1)
        temp[0] =1
        temp[i] = 1
        for j in range(1,i):
            temp[j] = triangle[i-1][j]+triangle[i-1][j-1]
        triangle.append(temp)
    return triangle[rowIndex]
                            
                        
'''
Question 1 :
Imagine that an employment tree represents the formal employee hierarchy at Amazon. Manager nodes have
chid nodes for each employee that reports to them; each of these employees can, in turn, have child nodes
representing their respective reportees. Each node in the tree contains an integer representing the number of
months the employee has spent at the company. Team tenure is computed as the average tenure of the manager
and all the company employees working below the manager. The oldest team has the highest team tenure.

Write an algorithm to find the manager of the team with the highest tenure. An employee must have child nodes
to be a manager.

Input
The input to the function/method consists of an argument -
president, a node representing the root node of the employee hierarchy.

Output
Return the node which has the oldest team.

Note
There will be at least one child node in the tree and there will be no ties.

Example

Input
   President =
	             20
          12            18
             
      11   2   3      15   8

Output = 18
Explanation :
There are three managers in this tree with the following team tenures :
12 => (11+2+3+12)/4 = 7
18 => (18+15+8)/3 = 13.67
20 => (12+11+2+3+18+15+8+20)/8 = 11.125
'''
                            
'''
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Example 3:

Input: s = "bb"
Output: 2
 

Constraints:

1 <= s.length <= 2000
s consits of lower-case and/or upper-case English letters only.


'''
def longestPalindrome(self, s: str) -> int:
    if len(s) ==1:
        return 1
    counter = 0
    temp = []
    exist = False
    for i in s:
        if not i in temp and s.count(i)>1:
            temp.append(i)
            counter += (s.count(i)//2)*2
        if s.count(i)%2 !=0:
            exist = True
    if exist == True:
        counter +=1
    return counter
                            
'''
484. Find Permutation

By now, you are given a secret signature consisting of character 'D' and 'I'. 'D' represents a decreasing relationship between two numbers, 'I' represents an increasing relationship between two numbers. And our secret signature was constructed by a special integer array, which contains uniquely all the different number from 1 to n (n is the length of the secret signature plus 1). For example, the secret signature "DI" can be constructed by array [2,1,3] or [3,1,2], but won't be constructed by array [3,2,4] or [2,1,3,4], which are both illegal constructing special string that can't represent the "DI" secret signature.

On the other hand, now your job is to find the lexicographically smallest permutation of [1, 2, ... n] could refer to the given secret signature in the input.

Example 1:
Input: "I"
Output: [1,2]
Explanation: [1,2] is the only legal initial spectial string can construct secret signature "I", where the number 1 and 2 construct an increasing relationship.
Example 2:
Input: "DI"
Output: [2,1,3]
Explanation: Both [2,1,3] and [3,1,2] can construct the secret signature "DI", 
but since we want to find the one with the smallest lexicographical permutation, you need to output [2,1,3]
Note:

The input string will only contain the character 'D' and 'I'.
The length of input string is a positive integer and will not exceed 10,000

'''
                            
def findPermutation(self, s: str) -> List[int]:
        result = [1]
        i = 2
        dcount = 0
        for c in s:
            if c == 'I':
                result.append(i)
                dcount = 0
            elif c == 'D':
                result.insert(len(result) - (dcount + 1), i)
                dcount += 1
            else:
                raise ValueError("invalid character in string") #also check if if only contains D and I
            i += 1
        return result

'''
435. Non-overlapping Intervals

Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
Example 3:

Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Note:

You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
'''
def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    end, cnt = float('-inf'), 0
    for s, e in sorted(intervals, key=lambda x: x[1]):
        #omg super easy idea
        if s >= end: 
            end = e
        else: 
            cnt += 1
    return cnt
                            
'''
123. Best Time to Buy and Sell Stock III

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

 

Example 1:

Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
Example 4:

Input: prices = [1]
Output: 0
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 105
'''
                            
                            
'''
208. Implement Trie (Prefix Tree)
'''