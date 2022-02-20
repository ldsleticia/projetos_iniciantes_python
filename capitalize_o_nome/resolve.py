def solve(s):
    if (
        s.startswith("0")
        or s.startswith("1")
        or s.startswith("2")
        or s.startswith("3")
        or s.startswith("4")
        or s.startswith("5")
        or s.startswith("6")
        or s.startswith("7")
        or s.startswith("8")
        or s.startswith("9")
    ):
        return s
    else:
        return s.title()

print(solve("amanda more"))
print(solve("123b"))