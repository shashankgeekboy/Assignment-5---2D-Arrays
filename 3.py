def squares_of_sorted_numbers(nums):
  squared_nums = []
  for num in nums:
    squared_nums.append(num * num)

  squared_nums.sort()

  return squared_nums


def main():
  nums = [-4, -1, 0, 3, 10]

  squared_nums = squares_of_sorted_numbers(nums)
  print(squared_nums)


if __name__ == "__main__":
  main()
