# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z
def a(x, y, z):
    left = not(x or y or z)
    right = ((not x) and (not y) and (not z))
    return (left == right)

for x in [True, False]:
    for y in [True, False]:
        for z in [True, False]:
            print(f" x = {x}, y = {y}, z = {z}, ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z = {a(x, y, z)}")