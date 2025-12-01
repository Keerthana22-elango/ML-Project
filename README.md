# Text Encryption Classifier (Rule-Based ML Logic)

This project classifies any given text as **Encrypted** or **Not Encrypted** based on simple features such as:
- Digit percentage
- Uppercase percentage
- Symbol percentage
- Text length
- Randomness patterns

The project uses lightweight rule-based logic that imitates ML-style feature importance.  
It outputs:
- Numerical label: **1 = Encrypted**, **0 = Not Encrypted**
- Human-readable label
- Brief feature importance / reason for classification

---

## 🔧 How It Works

The script checks:
- If text contains high digits + uppercase (hex-like pattern)
- If there are many symbols
- If text is long and random
- Otherwise, it is treated as natural language

Based on these simple features, the classifier gives a prediction.

---

## ▶️ How to Run

1. Install Python 3  
2. Run the classifier:
3. Enter any text  
4. You will get:
   - Prediction Label (0/1)  
   - Prediction Text (Encrypted / Not Encrypted)  
   - Feature Importance  
   - Drone Communication Explanation  

---

## 🔍 Example

Input:
A7C39F29D1F0B9231A

Output:
Prediction Label: 1
Prediction: Encrypted
Reason: High digit and uppercase ratio → hex-like encrypted pattern.

