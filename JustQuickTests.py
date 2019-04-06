from DriverCode import crossover_coefficients

# def crossover_coefficients(first_coefficient, second_coefficient):
#     if first_coefficient > 0:
#         first_parent_coefficient_binary = bin(first_coefficient)[2:]
#     else:
#         first_parent_coefficient_binary = bin(first_coefficient)[3:]
#
#     if second_coefficient > 0:
#         second_parent_coefficient_binary = bin(second_coefficient)[2:]
#     else:
#         second_parent_coefficient_binary = bin(second_coefficient)[3:]
#
#     # print("Coefficients " + str(first_coefficient) + " " + str(second_coefficient))
#     if len(first_parent_coefficient_binary) <= len(second_parent_coefficient_binary):
#         len_ = len(first_parent_coefficient_binary)
#         child_coefficient_binary = list(second_parent_coefficient_binary)
#     else:
#         len_ = len(second_parent_coefficient_binary)
#         child_coefficient_binary = list(first_parent_coefficient_binary)
#
#     for i in range(len_):
#         if first_parent_coefficient_binary[i] == second_parent_coefficient_binary[i]:
#             child_coefficient_binary[i] = first_parent_coefficient_binary[i]
#         else:
#             child_coefficient_binary[i] = str(random.randint(0, 1))
#
#     if len(child_coefficient_binary):
#         return int(''.join(child_coefficient_binary), 2)
#     return 0

val = 10123
bin_val = bin(val)
bin_val = '-' + bin_val
print(int(bin_val, 2))

