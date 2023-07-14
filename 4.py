def find_distinct_numbers(nums1, nums2):
  distinct_numbers = []
  seen = set()

  for num in nums1:
    if num not in seen:
      distinct_numbers.append(num)
      seen.add(num)

  for num in nums2:
    if num in seen:
      seen.remove(num)

  return distinct_numbers


def main():
  nums1 = [1, 2, 3]
  nums2 = [2, 4, 6]

  distinct_numbers = find_distinct_numbers(nums1, nums2)
  print(distinct_numbers)


if __name__ == "__main__":
  main()
