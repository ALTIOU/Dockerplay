"""
LeetCode 15. 三数之和 (3Sum)

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，
使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

示例 1：
输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]

示例 2：
输入：nums = []
输出：[]

示例 3：
输入：nums = [0]
输出：[]
"""

def threeSum(nums):
    """
    三数之和解法 - 双指针法
    
    时间复杂度: O(n²)
    空间复杂度: O(1) 不考虑返回数组的空间
    
    Args:
        nums: List[int] - 输入的整数数组
        
    Returns:
        List[List[int]] - 所有和为0的不重复三元组
    """
    result = []
    n = len(nums)
    
    # 如果数组长度小于3，直接返回空结果
    if n < 3:
        return result
    
    # 对数组进行排序，这样可以使用双指针法
    nums.sort()
    
    # 遍历数组，固定第一个数
    for i in range(n - 2):
        # 跳过重复的第一个数
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # 使用双指针寻找另外两个数
        left = i + 1
        right = n - 1
        
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            
            if current_sum == 0:
                # 找到一个解
                result.append([nums[i], nums[left], nums[right]])
                
                # 跳过重复的left值
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                
                # 跳过重复的right值
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                # 移动指针继续寻找
                left += 1
                right -= 1
            elif current_sum < 0:
                # 和太小，移动左指针增大和
                left += 1
            else:
                # 和太大，移动右指针减小和
                right -= 1
    
    return result


def test_three_sum():
    """测试函数"""
    test_cases = [
        [-1, 0, 1, 2, -1, -4],  # 预期输出: [[-1,-1,2],[-1,0,1]]
        [],                     # 预期输出: []
        [0],                    # 预期输出: []
        [0, 0, 0],             # 预期输出: [[0,0,0]]
        [-2, 0, 1, 1, 2],      # 预期输出: [[-2,0,2],[-2,1,1]]
        [-1, 0, 1],            # 预期输出: [[-1,0,1]]
    ]
    
    for i, nums in enumerate(test_cases):
        result = threeSum(nums)
        print(f"测试用例 {i + 1}:")
        print(f"输入: {nums}")
        print(f"输出: {result}")
        print("-" * 40)


if __name__ == "__main__":
    test_three_sum()