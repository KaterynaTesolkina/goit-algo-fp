# Task 7 Monte Carlo Simulation of Dice Rolls

## Опис
Цей проект імітує велику кількість кидків двох гральних кубиків, обчислює суми чисел, які випадають на кубиках, та визначає ймовірність кожної можливої суми. 
Для визначення ймовірностей використовується метод Монте-Карло. Отримані результати порівнюються з аналітичними ймовірностями, які можна обчислити теоретично.

## Аналітичні ймовірності
Теоретичні ймовірності для сум, які можуть випасти при киданні двох гральних кубиків, наведені в таблиці:

| Сума | Ймовірність |
|------|-------------|
| 2    | 2.78% (1/36)|
| 3    | 5.56% (2/36)|
| 4    | 8.33% (3/36)|
| 5    | 11.11% (4/36)|
| 6    | 13.89% (5/36)|
| 7    | 16.67% (6/36)|
| 8    | 13.89% (5/36)|
| 9    | 11.11% (4/36)|
| 10   | 8.33% (3/36)|
| 11   | 5.56% (2/36)|
| 12   | 2.78% (1/36)|

## Результати Монте-Карло
Після виконання симуляції 1,000,000 кидків двох кубиків було отримано наступні ймовірності для кожної суми:

| Сума | Ймовірність (Монте-Карло) |
|------|----------------------------|
| 2    | 2.78%                     |
| 3    | 5.56%                     |
| 4    | 8.35%                     |
| 5    | 11.12%                    |
| 6    | 13.90%                    |
| 7    | 16.65%                    |
| 8    | 13.88%                    |
| 9    | 11.11%                    |
| 10   | 8.34%                     |
| 11   | 5.56%                     |
| 12   | 2.75%                     |

## Висновки
Результати, отримані методом Монте-Карло, дуже близькі до теоретичних аналітичних ймовірностей. Невеликі відхилення можна пояснити випадковими варіаціями, 
притаманними методу Монте-Карло, особливо при великій кількості симуляцій.

Графік, побудований для порівняння ймовірностей, також підтверджує, що результати симуляції збігаються з теоретичними значеннями.

Ці результати демонструють правильність розрахунків і підтверджують, що метод Монте-Карло можна ефективно використовувати для оцінки ймовірностей у випадкових процесах.