import base64

# Let's think about the order differently.
# The program does: input -> [transform1] -> [transform2] -> [transform3] -> compare with expected_val
# Possible orders to try:
# 1. input -> base64 -> rot3 -> reverse -> expected_val
# 2. input -> reverse -> rot3 -> base64 -> expected_val  
# 3. input -> rot3 -> reverse -> base64 -> expected_val
# 4. input -> reverse -> base64 -> rot3 -> expected_val
# 5. input -> rot3 -> base64 -> reverse -> expected_val
# 6. input -> base64 -> reverse -> rot3 -> expected_val

expected_val = 'fSFwdTBpdnE0dXdfM29zMXV3X3UwdzRnMW80eXtqZG9p'

def rot3(s):
    result = []
    for c in s:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base + 3) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

def unrot3(s):
    result = []
    for c in s:
        if c.isalpha():
            base = ord('A') if c.isupper() else ord('a')
            result.append(chr((ord(c) - base - 3) % 26 + base))
        else:
            result.append(c)
    return ''.join(result)

# Try order 1: input -> base64 -> rot3 -> reverse
# Reverse: expected -> un-reverse -> un-rot3 -> un-base64
r1 = expected_val[::-1]
r2 = unrot3(r1)
print('Order1 after un-reverse then un-rot3:', r2)
try:
    r3 = base64.b64decode(r2 + '==').decode()
    print('Order1 FLAG:', r3)
except Exception as e:
    print('Order1 error:', e)

print()

# Try order 5: input -> rot3 -> base64 -> reverse
# Reverse: expected -> un-reverse -> un-base64 -> un-rot3
r1 = expected_val[::-1]
print('Order5 un-reverse:', r1)
try:
    r2 = base64.b64decode(r1 + '==').decode()
    print('Order5 after un-base64:', r2)
    r3 = unrot3(r2)
    print('Order5 FLAG:', r3)
except Exception as e:
    print('Order5 error:', e)

print()

# Try order 6: input -> base64 -> reverse -> rot3
# Reverse: expected -> un-rot3 -> un-reverse -> un-base64
r1 = unrot3(expected_val)
print('Order6 un-rot3:', r1)
r2 = r1[::-1]
print('Order6 un-reverse:', r2)
try:
    r3 = base64.b64decode(r2 + '==').decode()
    print('Order6 FLAG:', r3)
except Exception as e:
    print('Order6 error:', e)
