import random

class Schedule:
    def __init__(self):
        self._subjects = ['Toan', 'Ly', 'Anh', 'Van', 'Sinh', 'Su']
        self._rooms = ['Phong A', 'Phong B', 'Phong C', 'Phong D', 'Phong E', 'Phong F']
        self._days = ['Thu Hai', 'Thu Ba', 'Thu Tu', 'Thu Nam', 'Thu Sau', 'Thu Bay']

    @property
    def subjects(self):
        return self._subjects
    @property
    def rooms(self):
        return self._rooms
    @property
    def days(self):
        return self._days

    def create_individual(self):
        schedule = {}
        for day in self.days:
            num_classes = random.randint(1, 6)
            daily_schedule = []
            for _ in range(num_classes):
                subject = random.choice(self.subjects)
                time_slot = random.randint(1, 6)
                room = random.choice(self.rooms)
                daily_schedule.append((subject, time_slot, room))
            schedule[day] = daily_schedule
        return schedule

    def initialize_population(self, size):
        return [self.create_individual() for _ in range(size)]

    def evaluate_schedule(self, schedule):
        conflicts = 10

        for day, daily_classes in schedule.items():
            times = {}
            subject_count = {}
            for subject, time_slot, room in daily_classes:
                # Kiểm tra xung đột thời gian
                if time_slot in times:
                    conflicts -= 5
                else:
                    times[time_slot] = True

                subject_count[subject] = subject_count.get(subject, 0) + 1
                # Kiểm tra số lần xuất hiện của môn học
                for subject, count in subject_count.items():
                    if count > 3:
                        conflicts -= 5


            num_classes = len(daily_classes)
            if num_classes == 1 or num_classes == 6:
                conflicts -= 5
            elif 4 >= num_classes >= 2:
                conflicts += 5

        fitness = conflicts
        return fitness


schedule_system = Schedule()
population_size = 100
population = schedule_system.initialize_population(population_size)

# In ra các cá thể
for i, individual in enumerate(population):
    print(f"Cá thể {i + 1}: {individual}")

# Đánh giá độ thích nghi cho từng cá thể
fitness_scores = {i: schedule_system.evaluate_schedule(individual) for i, individual in enumerate(population)}

# In ra độ thích nghi
for i, score in fitness_scores.items():
    print(f"Cá thể {i + 1}: Độ thích nghi = {score}")

# Chọn cá thể tốt nhất
best_individual_index = max(fitness_scores, key=fitness_scores.get)
best_individual = population[best_individual_index]

print("Cá thể tốt nhất:", best_individual)