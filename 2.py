def staircase_rows(n):
  rows = 0
  while n > 0:
    rows += 1
    n -= rows

  return rows


def main():
  n = 5

  rows = staircase_rows(n)
  print(rows)


if __name__ == "__main__":
  main()
