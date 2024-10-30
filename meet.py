from linkedlist import LinkedList
import random
import time
from runner import generate_single_runner

class Meet:
    def __init__(self, name, participants, schools, t):
        self.name = name
        self.participants = participants
        self.schools = schools
        self.time = t
        self.id = str(abs(hash(f'{name}{str(participants)}{str(schools)}{t}')))

    def to_hash_map(self):
        participants = []
        for p in self.participants:
            par = p.to_hash_map()
            par['time'] = p.generate_time()
            participants.append(par)
        participants = sorted(participants, key=lambda x: x['time'])
        
        return {
            'name': self.name,
            'time': self.time,
            'schools': self.schools,
            'id': self.id,
            'participants': participants
        }

