import random
import json
import os

# Configuration
NUM_PROBLEMS = 10
COEFF_RANGE = (-10, 10)  # inclusive range for a, b, c
STATS_FILE = "practice_stats.json"

def generate_quadratic():
    """Generate coefficients a, b, c for ax^2 + bx + c = 0, ensuring a != 0."""
    a = random.randint(*COEFF_RANGE)
    while a == 0:
        a = random.randint(*COEFF_RANGE)
    b = random.randint(*COEFF_RANGE)
    c = random.randint(*COEFF_RANGE)
    return a, b, c

def discriminant(a, b, c):
    return b*b - 4*a*c

def roots(a, b, c):
    d = discriminant(a, b, c)
    if d < 0:
        # complex roots
        real = -b / (2*a)
        imag = (abs(d) ** 0.5) / (2*a)
        return f"{real:.2f} + {imag:.2f}i", f"{real:.2f} - {imag:.2f}i"
    elif d == 0:
        r = -b / (2*a)
        return f"{r:.2f}", f"{r:.2f}"
    else:
        sqrt_d = d ** 0.5
        r1 = (-b + sqrt_d) / (2*a)
        r2 = (-b - sqrt_d) / (2*a)
        return f"{r1:.2f}", f"{r2:.2f}"

def load_stats():
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, 'r') as f:
            return json.load(f)
    return {"total_sessions": 0, "total_problems": 0, "correct_answers": 0}

def save_stats(stats):
    with open(STATS_FILE, 'w') as f:
        json.dump(stats, f, indent=2)

def main():
    print("Quadratic Practice - Enter roots as comma-separated values (e.g., 2, -3) or 'complex' for complex roots.")
    print("Type 'exit' to quit.\n")
    
    stats = load_stats()
    session_correct = 0
    
    for i in range(1, NUM_PROBLEMS + 1):
        a, b, c = generate_quadratic()
        r1, r2 = roots(a, b, c)
        # Determine expected answer string
        if "complex" in r1 or "complex" in r2:
            expected = "complex"
        else:
            # sort roots for consistent comparison
            r1_val = float(r1)
            r2_val = float(r2)
            expected = f"{min(r1_val, r2_val):.2f}, {max(r1_val, r2_val):.2f}"
        
        print(f"Problem {i}: {a}x^2 + ({b})x + ({c}) = 0")
        user_input = input("Your answer: ").strip()
        
        if user_input.lower() == "exit":
            break
        
        # Normalize user input: remove spaces, lower case
        normalized = user_input.replace(" ", "").lower()
        if normalized == expected.replace(" ", "").lower():
            print("Correct! 🎯\n")
            session_correct += 1
        else:
            print(f"Incorrect. Expected: {expected}\n")
    
    print(f"Session complete. You solved {session_correct} out of {i} correctly.")
    stats["total_sessions"] += 1
    stats["total_problems"] += i
    stats["correct_answers"] += session_correct
    save_stats(stats)
    print(f"Overall stats: {stats['correct_answers']}/{stats['total_problems']} correct across {stats['total_sessions']} sessions.")

if __name__ == "__main__":
    main()