text_combined = "UONCSVAIHGEPAAHIGIRLBIECSTECSWPNITETIENOIEEFDOWECXTRSRXSTTARTLODYFSOVNEOECOHENIODAARQNAELAFSGNOPTE"
columns_new = 14

transposed_text_new = [''.join(text_combined[i::columns_new]) for i in range(columns_new)]
formatted_text_new = '\n'.join(transposed_text_new)
print(formatted_text_new)

vowels = "AEIOU"
ideal_proportion = 7*0.4
proportions_diff = []
total_proportion = 0
x = 0
for col in transposed_text_new:
    vowel_count = sum(1 for char in col if char.upper() in vowels)
    proportion = vowel_count 
    diff = abs(proportion - ideal_proportion)
    proportions_diff.append((proportion, diff))
    total_proportion += proportion
    x += diff

for item in proportions_diff:
    print(f"{item[0]}, Difference: {item[1]:.2f}")

average_proportion = total_proportion / 98
print(average_proportion)
print(x / 14)

new_order_corrected = [5, 2, 6, 7, 1, 4, 3]
reordered_corrected = [''.join(line[i - 1] for i in new_order_corrected) for line in transposed_text_new]
reordered_corrected_formatted = '\n'.join(reordered_corrected)
print(reordered_corrected_formatted)
