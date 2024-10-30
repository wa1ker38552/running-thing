import random
from linkedlist import LinkedList
import time

names = 'alice bob charlie david eva frank grace hannah ian jack kelly leo mia nina owen paul quinn rita sam tina uma victor wendy xander yara zoe aaron brianna chris daniel emily fona george holly isla james kylie liam mason nora oliver piper'.split()
names = [i.capitalize() for i in names]
schools = ['los altos high school', 'los gatos high school', 'mountain view high school']
divisions = ['varsity', 'junior varsity']

database = {}

# bubble sort by dictionary key
def sort_data(data, key):
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data[j][key] > data[j + 1][key]:
                data[j], data[j + 1] = data[j + 1], data[j]
    return data

# for inheritance 
class Runner():
    def __init__(self, name, age, team, division):
        self.name = name
        self.age = age
        self.team = team
        self.id = str(abs(hash(f'{name}{age}{team}')))
        self.division = division
        self.time_distributions = []

    def generate_time_distributions(self, amount, time_range=[1800, 3600]):
        data = []
        for i in range(amount):
            data.append({
                'x': (time.time()-random.randint(0, 86400*30))*1000, # generate data for the past month, x1000 to conver to millisecond time for js
                'y': random.randint(time_range[0], time_range[1])
            })
        data = sort_data(data, 'x')
        self.time_distributions = data

    def generate_time(self, time_range=[1800, 3600]):
        return random.randint(time_range[0], time_range[1])

class VarsityRunner(Runner):
    def __init__(self, name, age, team, ranking, division):
        super().__init__(name, age, team, division)
        self.ranking = ranking

    def __str__(self):
        return f'{self.name} {self.age} {self.team} {self.ranking}'
    
    def to_hash_map(self):
        return {
            'name': self.name,
            'age': self.age,
            'team': self.team,
            'ranking': self.ranking,
            'division': self.division,
            'id': self.id,
            'time_distributions': self.time_distributions
        }

class JuniorVarsityRunner(Runner):
    def __init__(self, name, age, team, division):
        super().__init__(name, age, team, division)

    def __str__(self):
        return f'{self.name} {self.age} {self.team}'
    
    def to_hash_map(self):
        return {
            'name': self.name,
            'age': self.age,
            'team': self.team,
            'division': self.division,
            'id': self.id,
            'time_distributions': self.time_distributions
        }


def generate_runner_data(amount):
    data = LinkedList() # linked list
    for i in range(amount):
        name = random.choice(names)
        age = random.randint(14, 18)
        team = random.choice(schools)
        division = random.choice(divisions)

        if division == 'varsity':
            ranking = random.randint(1, 5)
            runner = VarsityRunner(name, age, team, ranking, division)
        else:
            runner = JuniorVarsityRunner(name, age, team, division)
        data.append(runner)
    return data

def generate_single_runner():
    name = random.choice(names)
    age = random.randint(14, 18)
    team = random.choice(schools)
    division = random.choice(divisions)

    if division == 'varsity':
        ranking = random.randint(1, 5)
        runner = VarsityRunner(name, age, team, ranking, division)
    else:
        runner = JuniorVarsityRunner(name, age, team, division)
    return runner