def find_minimum_element(nums):
  low = 0
  high = len(nums) - 1

  while low < high:
    mid = (low + high) // 2

    if nums[mid] > nums[high]:
      low = mid + 1
    else:
      high = mid

  return nums[low]


def main():
  nums = [3, 4, 5, 1, 2]

  minimum_element = find_minimum_element(nums)
  print(minimum_element)


if __name__ == "__main__":
  main()
