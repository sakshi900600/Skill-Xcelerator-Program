# n = 3
# rows = []

# for i in range(n):
#     # Create left side: from 'e' to 'e' - i
#     left = [chr(ord('a') + n - 1 - j) for j in range(i + 1)]
#     full = left + left[-2::-1]  # mirror without center
#     line = '-'.join(full)
    
#     dash_padding = '-' * (2 * (n - i - 1))
#     rows.append(dash_padding + line + dash_padding)

# # Mirror the top part to form bottom (excluding middle)
# rows += rows[-2::-1]

# # Print the pattern
# for row in rows:
#     print(row)




print(ord('a'))  # 97
print(ord('c'))  # 99
