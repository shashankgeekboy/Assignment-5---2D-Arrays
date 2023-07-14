def undouble(changed):
  seen = set()
  original = []

  for num in changed:
    if num in seen:
      original.append(num // 2)
    else:
      seen.add(2 * num)

  if len(original) * 2 == len(changed):
    return original
  else:
    return []


def main():
  changed = [1, 3, 4, 2, 6, 8]

  original = undouble(changed)
  print(original)


if __name__ == "__main__":
  main()
