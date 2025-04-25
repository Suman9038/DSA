def maxlen(arr: list[int], target_sum: int) -> int:
    m = {} 
    preSum = 0
    res = 0

    for i in range(len(arr)):
        preSum += arr[i]
        
        if preSum == target_sum:
            res = i + 1
        if preSum not in m:
            m[preSum] = i

        if (preSum - target_sum) in m:
            res = max(res, i - m[preSum - target_sum])

       

    return res


arr = [3,1,0,1,8,2,3,6]
print(maxlen(arr, 5))