package leetcode

func twoSum(nums []int, target int) []int {
	for i := 0; i < len(nums); i++ {
		for j := i + 1; j < len(nums); j++ {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
		}
	}
	return []int{}
}

func twoSum2(nums []int, target int) []int {
	m := make(map[int]int)
	for i, num := range nums {
		m[num] = i
	}

	for i, num := range nums {
		comp := target - num
		if j, ok := m[comp]; ok && j != i {
			return []int{i, j}
		}
	}

	return []int{}
}
