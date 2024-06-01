import random
from collections import defaultdict
import numpy as np

def naive_shuffle(cards):
    for i in range(len(cards)):
        n = random.randint(0, len(cards) - 1)
        cards[i], cards[n] = cards[n], cards[i]

def fisher_yates_shuffle(cards):
    for i in range(len(cards)-1, 0, -1):
        n = random.randint(0, i)
        cards[i], cards[n] = cards[n], cards[i]

def simulate_shuffles(num_simulations, num_cards=4):
    naive_counts = defaultdict(int)
    fy_counts = defaultdict(int)
    card_set = list(range(1, num_cards+1))

    for _ in range(num_simulations):
        naive_cards = card_set[:]
        naive_shuffle(naive_cards)
        naive_counts[tuple(naive_cards)] += 1

        fy_cards = card_set[:]
        fisher_yates_shuffle(fy_cards)
        fy_counts[tuple(fy_cards)] += 1

    return naive_counts, fy_counts

def analyze_results(counts):
    values = np.array(list(counts.values()))
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev

def main():
    num_simulations = 1000000
    naive_counts, fy_counts = simulate_shuffles(num_simulations)
    naive_mean, naive_std = analyze_results(naive_counts)
    fy_mean, fy_std = analyze_results(fy_counts)
    print("Naive algorithm:")
    for key, value in sorted(naive_counts.items()):
        print(f"{key}: {value}")

    print("\nFisher–Yates shuffle:")
    for key, value in sorted(fy_counts.items()):
        print(f"{key}: {value}")
        
    print(f"Naive Shuffle: Mean = {naive_mean}, Std Dev = {naive_std}")
    print(f"Fisher-Yates Shuffle: Mean = {fy_mean}, Std Dev = {fy_std}")

    if fy_std < naive_std:
        print("Fisher-Yates shuffle is better: more uniform distribution.")
    else:
        print("Naive shuffle is better: more uniform distribution.")

if __name__ == "__main__":
    main()
