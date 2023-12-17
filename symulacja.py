import random
import numpy as np

SIMULATION_TIME = 1000000
STATIC_TANKING_TIME = 60

class car:
    def __init__(self, _ID, _created_in, _time_to_tank):
        self.ID = _ID
        self.waiting_time = 0
        self.time_to_tank = _time_to_tank
        self.tanking_time = 0
        self.tanked = False
        self.created_in = _created_in
    def __str__(self):
        return f"ID={self.ID}, Created in={self.created_in}, Waiting time={self.waiting_time}"
    
def random_exponential(lambda_param, sample=1):
    return np.random.exponential(scale = lambda_param, size=sample)

def random_normal(average, deviation, sample=1):
    return np.random.normal(loc=average, scale=deviation, size=sample)

def random_uniform(low, high, num_samples=1):
    return np.random.uniform(low, high, size=num_samples)

def lcg(x, a, b, m):
    while True:
        x = (a * x + b) % m
        yield x

def random_uniform_sample(n, interval, seed=0):
    #GLIBC
    a, b, m = 1103515245, 12345, 2 ** 32 -1
    bsdrand = lcg(seed, a, b, m)

    lower, upper = interval[0], interval[1]
    sample = []

    for i in range(n):
        observation = (upper - lower) * (next(bsdrand) / (m)) + lower
        sample.append(round(observation))

    return sample

def random_exponential_sample(n, lambd, seed=0):
    a, c, m = 1103515245, 12345, 2 ** 32 -1
    bsdrand = lcg(seed, a, c, m)

    sample = []

    for i in range(n):
        # Generuj wartości z rozkładu eksponenty
        u = next(bsdrand) / (m)
        observation = -np.log(1 - u) / lambd
        sample.append(observation)

    return sample

def random_normal_sample(n, mean, std_dev, seed=0):
    a, c, m = 1103515245, 12345, 2 ** 32 -1
    bsdrand = lcg(seed, a, c, m)

    sample = []

    for i in range(n):
        # Generuj dwie wartości z rozkładu jednostajnego
        u1 = next(bsdrand) / (m)
        u2 = next(bsdrand) / (m)

        # Transformacja Boxa-Mullera
        z0 = np.sqrt(-2 * np.log(u1)) * np.cos(2 * np.pi * u2)
        observation = mean + std_dev * z0

        sample.append(observation)

    return sample


second = 0
distributor_A = []
distributor_A_buffer = []
car_id = 0
add_new_car = 0
cars_done = []
next_car_iter = 0
can_next_car = True
next_car_time = 0
car_times = random_exponential(120, int(1000000/2))

# print(len(cars_done))

#zmienna losowa z rozkładu wykładniczego -> nowe auto -> szansa na przyjechanie auta (1/119)^k-1 * 1/120
#Metoda odwrotnej dystrybuanty
#Zrobić własny generator
#pierwszy -> rozkład
#drugi -> pierwszy + rozklad

# tab_temp = 0
# for n in range(1000000):
#     tab_temp += int(random_exponential(120, 1))

# print(tab_temp/1000000)


while(second != SIMULATION_TIME):

    if(second == next_car_time):
        # Static time
        distributor_A_buffer.append(car(car_id, second,  STATIC_TANKING_TIME))
        # Uniform time
        # distributor_A_buffer.append(car(car_id, second,  int(random_uniform(0, 120)[0])))
        # Exponential time
        # distributor_A_buffer.append(car(car_id, second,  int(random_exponential(60, 1)[0])))
        # Normal time
        # distributor_A_buffer.append(car(car_id, second,  int(random_normal(60, 20)[0])))
        car_id += 1
        can_next_car = True

    if len(distributor_A) == 0:
        if len(distributor_A_buffer) != 0:
            distributor_A.append(distributor_A_buffer.pop(0))
    else: 
        distributor_A[0].tanking_time += 1

    # Static time
    if len(distributor_A) != 0:
        if distributor_A[0].tanking_time == STATIC_TANKING_TIME:
            cars_done.append(distributor_A.pop(0))

    # Exponential distribution
    # if len(distributor_A) != 0:
    #     if distributor_A[0].time_to_tank == distributor_A[0].tanking_time:
    #         cars_done.append(distributor_A.pop(0))

    # normal distribution
    # if len(distributor_A) != 0:
    #     if random_normal(60, 1) <= 58:
    #         cars_done.append(distributor_A.pop(0))


    for waiting_car in distributor_A_buffer:
        waiting_car.waiting_time += 1

    if(can_next_car == True):
        if(int(car_times[next_car_iter] >= 1)):
            next_car_time += int(car_times[next_car_iter]) + 1
            next_car_iter += 1
            can_next_car = False
        else:
            next_car_time += 1
            next_car_iter += 1
            can_next_car = False

    second += 1

    

average_waiting_time = 0

for car_final in cars_done:
    average_waiting_time += car_final.waiting_time
    print(car_final)

print(float(average_waiting_time-1)/float(len(cars_done)))

# rus = random_exponential_sample(10000, 1/60, 4)
# rus = random_uniform_sample(1000, (0,120), 4)
rus = random_normal_sample(1000, 60, 20, 1)

average_estimator = 0
for i in rus:
    print(int(i))
    average_estimator += int(i)
print(average_estimator/10000)