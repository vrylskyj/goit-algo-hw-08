import heapq

def min_cost_to_connect_cables(cable_lengths):
    # Ініціалізуємо загальні витрати
    total_cost = 0
    
    # Перетворюємо список кабелів у пріоритетну чергу
    heapq.heapify(cable_lengths)
    
    # Повторюємо, доки в черзі є більше одного кабелю
    while len(cable_lengths) > 1:
        # Видаляємо два найкоротші кабелі з черги
        shortest1 = heapq.heappop(cable_lengths)
        shortest2 = heapq.heappop(cable_lengths)
        
        # Об'єднуємо їх та додаємо до загальних витрат
        total_cost += shortest1 + shortest2
        
        # Додаємо новий кабель (суму довжин двох попередніх) до черги
        heapq.heappush(cable_lengths, shortest1 + shortest2)
    
    # Повертаємо загальні витрати
    return total_cost

# Приклад використання
cables = [8, 4, 6, 12]
min_cost = min_cost_to_connect_cables(cables)
print("Мінімальні витрати на об'єднання кабелів:", min_cost)
