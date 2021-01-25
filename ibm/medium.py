#221  maximal Square
def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or len(matrix)<1:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        side =0
        
        dp = [[0 for col in range(cols+1)]for row in range(rows+1)]
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j]=="1":
                    dp[i+1][j+1] = min(dp[i][j],dp[i][j+1],dp[i+1][j])+1
                    side = max(side,dp[i+1][j+1])
        print(dp)
        return side*side

#229. Majority Element II
def majorityElement(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    times= len(nums)/3
    print(times)
    temp = {}
    res = []
    if len(nums)==1:
        return [nums[0]]

    for i in nums:
        if i not in res:
            if not temp.get(i):
                temp[i]=1
                if temp[i]>times:
                    res.append(i)
            else:
                temp[i]+=1
                if temp[i]>times:
                    res.append(i)
    return res

#259. 3Sum Smaller
 def threeSumSmaller(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    result = 0
    nums.sort()
    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s < target:
                result += r - l
                l += 1
            else:
                r -= 1
    return result

# 287. Find the Duplicate Number
def findDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i+1]==nums[i]:
            return nums[i]        

## O(n)
def findDuplicate(self, nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

        
#443
def compress(self, chars):
        if not chars:
            return 0
        
        curr, count, ind = chars[0], 1, 1
        while ind < len(chars):
            if chars[ind] == curr:
                count += 1
                chars.pop(ind)
            
            elif chars[ind] != curr:
                if count != 1:
                    for i in str(count):
                        chars.insert(ind, i)
                        ind += 1

                curr,count = chars[ind], 1
                ind += 1
        
        if count > 1:
            for i in str(count):
                chars.append(i)
        
        return len(chars)
    
#my solution
def compress(self, chars):
    """
    :type chars: List[str]
    :rtype: int
    """
    ret = []
    i = 0
    j = 0
    while(j<len(chars)):
        if(chars[j]==chars[i]):
            j+=1
        else:
            print(i,j)
            if (j-i==1):
                ret.append(str(chars[i]))
            elif(j-i>1):
                ret.append(str(chars[i]))
                temp = list(str(j-i))
                for i in temp:
                    ret.append(i)
            i=j
            j +=1
        if j ==len(chars):
            if (j-i==1):
                ret.append(str(chars[i]))
            elif(j-i>1):
                ret.append(str(chars[i]))
                #print([x for x in uhello])
                temp = list(str(j-i))
                for i in temp:
                    ret.append(i)

    chars = ret
    print(chars)
    return len(chars)

#764. Largest Plus Sign

def orderOfLargestPlusSign(self, N, mines):
    banned = {tuple(mine) for mine in mines}
    dp = [[0] * N for _ in range(N)]
    ans = 0

    for r in range(N):
        count = 0
        for c in range(N):
            count = 0 if (r,c) in banned else count+1
            dp[r][c] = count

        count = 0
        for c in range(N-1, -1, -1):
            count = 0 if (r,c) in banned else count+1
            if count < dp[r][c]: dp[r][c] = count

    for c in range(N):
        count = 0
        for r in range(N):
            count = 0 if (r,c) in banned else count+1
            if count < dp[r][c]: dp[r][c] = count

        count = 0
        for r in range(N-1, -1, -1):
            count = 0 if (r, c) in banned else count+1
            if count < dp[r][c]: dp[r][c] = count
            if dp[r][c] > ans: ans = dp[r][c]

    return ans


#1010. Pairs of Songs With Total Durations Divisible by 60

def numPairsDivisibleBy60(self, time):
    """
    :type time: List[int]
    :rtype: int
    """
    #cannot use dict() for remainders[60-t%60]
    remainders = collections.defaultdict(int)

    ret = 0
    for t in time:
        if t % 60 == 0: # check if a%60==0 && b%60==0
            ret += remainders[0]
        else: # check if a%60+b%60==60
            ret += remainders[60-t%60]
        remainders[t % 60] += 1 # remember to update the remainders
    return ret


