def distance_value(arr1, arr2, d):
  distance = 0
  for num in arr1:
    flag = False
    for other_num in arr2:
      if abs(num - other_num) <= d:
        flag = True
        break
    if not flag:
      distance += 1

  return distance


def main():
  arr1 = [4, 5, 8]
  arr2 = [10, 9, 1, 8]
  d = 2

  distance = distance_value(arr1, arr2, d)
  print(distance)


if __name__ == "__main__":
  main()
