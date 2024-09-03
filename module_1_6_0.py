# ДЗ Средний балл
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
print({name: sum(grade) / len(grade) for name, grade in zip(sorted(students), grades)} )
# sum(grade) Вычисляет сумму оценок студента
# len(grade) Определяет количество оценок студента
# sum(grade) / len(grade) Вычисляет среднюю оценку студента
# sorted(students) Сортирует имена студентов в алфавитном порядке
# zip(sorted(students), grades Создаёт пары (имя, оценки)
