func twoSum(nums []int, target int) []int {
    seen := make(map[int]int)
	// val : idx
	for i, n := range nums {
		diff := target - n
		if j, ok := seen[diff]; ok {
			return []int{j, i}
		}
		seen[n] = i
	}

	return []int{}
}
