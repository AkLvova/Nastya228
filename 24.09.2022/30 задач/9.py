a = int(input())
b = int(input())

print("YES" if not (a and b) or not (a % b and b % a) else "NO")
