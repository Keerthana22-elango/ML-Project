import re

def classify_text(text):

    # Remove spaces
    cleaned = text.strip()

    # Features
    length = len(cleaned)
    digits = sum(c.isdigit() for c in cleaned)
    letters = sum(c.isalpha() for c in cleaned)
    uppercase = sum(c.isupper() for c in cleaned)
    symbols = sum(not c.isalnum() for c in cleaned)

    digit_ratio = digits / length if length else 0
    symbol_ratio = symbols / length if length else 0
    uppercase_ratio = uppercase / length if length else 0

    # Rule 1: High digit + uppercase → Encrypted
    if digit_ratio > 0.4 and uppercase_ratio > 0.4:
        return 1, "Encrypted", "High mix of digits & uppercase (Hex-like pattern)."

    # Rule 2: Many symbols → Encrypted
    if symbol_ratio > 0.3:
        return 1, "Encrypted", "High percentage of symbols (random-like pattern)."

    # Rule 3: Long + random digits → Encrypted
    if length > 20 and digit_ratio > 0.3:
        return 1, "Encrypted", "Long text with random digits → looks encrypted."

    # Otherwise Not Encrypted
    return 0, "Not Encrypted", "Text looks natural with low randomness."


# -------- Main Program --------
text = input("Enter text: ")

label_num, label_text, reason = classify_text(text)

print("\n===== RESULT =====")
print("Input Text:", text)
print("Prediction Label (0/1):", label_num)
print("Prediction:", label_text)
print("Reason:", reason)
