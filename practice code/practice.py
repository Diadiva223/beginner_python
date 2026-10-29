alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

text = input("Enter a test")
shift_amount = int(input("Enter shift amount"))

shifted_position = alphabet.index(text) + shift_amount
shifted_position %= len(alphabet)
output_text = alphabet[shifted_position]

print(output_text)