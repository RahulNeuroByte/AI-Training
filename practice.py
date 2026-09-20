# 6. REMOVING ELEMENTS
# ============================================================

numbers = [10, 20, 30, 40, 50]

# ------------------------------------------------------------
# remove()
# Removes first occurrence of VALUE
# ------------------------------------------------------------

numbers.remove(30)

print("After remove:", numbers)


# ------------------------------------------------------------
# pop()
# Removes element using INDEX
# Also returns removed element
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

removed = numbers.pop(2)

print("Removed:", removed)
print("After pop:", numbers)


# pop() without index removes last element

last = numbers.pop()

print("Last removed:", last)
print("After pop:", numbers)


# ------------------------------------------------------------
# del
# Deletes element using index
# ------------------------------------------------------------

numbers = [10, 20, 30, 40, 50]

del numbers[1]

print("After del:", numbers)


# Delete multiple elements

numbers = [10, 20, 30, 40, 50]

del numbers[1:4]

print("After deleting range:", numbers)


# ------------------------------------------------------------
# clear()
# Removes ALL elements
# ------------------------------------------------------------

numbers = [10, 20, 30]

numbers.clear()

print("After clear:", numbers)
