import random
import matplotlib.pyplot as plt

def monte_carlo_simulation(num_rolls):
    # Створюємо словник для зберігання кількості з'явлень кожної суми
    sums_count = {i: 0 for i in range(2, 13)}

    # Кидаємо кубики num_rolls разів
    for _ in range(num_rolls):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        total = dice1 + dice2
        sums_count[total] += 1

    # Обчислюємо ймовірності кожної суми
    probabilities = {k: v / num_rolls for k, v in sums_count.items()}
    
    return probabilities

# Кількість кидків кубиків
num_rolls = 1000000

# Симуляція кидків кубиків
probabilities = monte_carlo_simulation(num_rolls)

# Вивід результату
print("Монте-Карло ймовірності:")
print("-" * 20)
for total, probability in probabilities.items():
    print(f"{total}\t{probability:.4%}")

# Аналітичні ймовірності
analytical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

print("\nАналітичні ймовірності:")
print("-" * 30)
for total, probability in analytical_probabilities.items():
    print(f"{total}\t{probability:.4%}")

# Побудова графіку для порівняння результатів
x = list(probabilities.keys())
monte_carlo_probs = [probabilities[key] for key in x]
analytical_probs = [analytical_probabilities[key] for key in x]

plt.figure(figsize=(10, 6))
plt.plot(x, monte_carlo_probs, label='Монте-Карло', marker='o')
plt.plot(x, analytical_probs, label='Аналітичні', marker='x')
plt.xlabel('Сума')
plt.ylabel('Ймовірність')
plt.title('Порівняння ймовірностей сум кидків кубиків')
plt.legend()
plt.grid(True)
plt.show()

