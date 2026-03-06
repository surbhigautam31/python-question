text = input("enter a string :")
vowels = "aeiouAEIOU"
vowels_count = 0
consonents_count=0

for ch in text:
    if ch in vowels:
        vowels_count += 1
    elif ch.isalpha():
        consonents_count += 1

print(f"Vowels: {vowels_count}")
print(f"Consonants: {consonents_count}")