def distribute_apples(total_weight):
    box_15kg = 15
    box_10kg = 10
    box_5kg = 5

    count_15kg = total_weight // box_15kg
    remaining_weight = total_weight % box_15kg

    count_10kg = total_weight // box_10kg
    remainining_weight = total_weight % box_10kg

    count_5kg = remaining_weight // box_5kg

    return count_15kg, count_10kg, count_5kg

total_weight = 460

count_15kg, count_10kg, count_5kg = distribute_apples(total_weight)

print(f"Boxes with 15kg: {count_15kg}")
print(f"Boxes with 10kg: {count_10kg}")
print(f"Boxes with 5kg: {count_5kg}")
