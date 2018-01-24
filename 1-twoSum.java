/*
Brute Force: Time complexity O(n^2)
Space complexity O(1)
 */

public int[] twoSum(int[] nums, int target) {
    for (int i = 0; i < nums.length; i++) {
        for (int j = i + 1; j < nums.length; j++) {
            if (nums[j] == target - nums[i]) {
                    return new int[] { i, j };
            }
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}

/*
Two-pass Hash Table: Time complexity O(n)
Space complexity O(n)
 */

public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        map.put(nums[i], i);
    }
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement) && map.get(complement) != i) {
            return new int[] { i, map.get(complement) };
        }
    }
    throw new IllegalArgumentException("No two sum solution");
}

/*
One-pass Hash Table: Time complexity O(n)
Space complexity O(n)
 */

/*
先向map中添加元素再进行for循环检查是错误的，对于nums = [3, 3]; target = 6等类似情况会直接抛出异常，正确结果应为i = 0, j = 1
 */

public int[] twoSum(int[] nums, int target) {
    Map<Integer, Integer> map = new HashMap<>();
    for (int i = 0; i < nums.length; i++) {
        int complement = target - nums[i];
        if (map.containsKey(complement)) {
            return new int[] { map.get(complement), i };
        }
        map.put(nums[i], i);
    }
    throw new IllegalArgumentException("No two sum solution");
}


