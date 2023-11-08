# Bitwise AND (&)
a = 5  # Binary: 0101
b = 3  # Binary: 0011

result_and = a & b  # Result: 0001 (1 in decimal)
print("Bitwise AND:", result_and)

# Bitwise OR (|)
result_or = a | b  # Result: 0111 (7 in decimal)
print("Bitwise OR:", result_or)

# Bitwise XOR (^)
result_xor = a ^ b  # Result: 0110 (6 in decimal)
print("Bitwise XOR:", result_xor)

# Bitwise NOT (~)
result_not_a = ~a  # Result: 11111010 (Two's complement representation)
print("Bitwise NOT of 'a':", bin(result_not_a))

# Left Shift (<<)
result_left_shift = a << 2  # Result: 010100 (20 in decimal)
print("Left Shift by 2:", result_left_shift)

# Right Shift (>>)
result_right_shift = a >> 1  # Result: 0010 (2 in decimal)
print("Right Shift by 1:", result_right_shift)


print(bin(a))