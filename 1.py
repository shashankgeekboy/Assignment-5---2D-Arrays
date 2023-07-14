def convert_1d_array_to_2d(original, m, n):
  if len(original) != m * n:
    return []

  converted_array = []
  for i in range(m):
    row = original[i * n:(i + 1) * n]
    converted_array.append(row)

  return converted_array


def main():
  original = [1, 2, 3, 4]
  m = 2
  n = 2

  converted_array = convert_1d_array_to_2d(original, m, n)
  print(converted_array)


if __name__ == "__main__":
  main()
