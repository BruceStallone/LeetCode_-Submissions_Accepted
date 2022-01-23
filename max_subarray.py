def maxSubArray(nums):
	currSum = maxSum = nums[0]
	for i in range(1,len(nums)):
	    currVal = nums[i]
	    currSum = max(currVal, currSum + currVal)
	    maxSum = max(currSum, maxSum)
	return maxSum