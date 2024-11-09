import random
import heapq
from typing import List, Tuple

class Particle:
    def __init__(self, id: int, decay_time: float):
        self.id = id
        self.decay_time = decay_time
    
    def __lt__(self, other):
        return self.decay_time < other.decay_time

    def __eq__(self, other):
        return self.id == other.id and self.decay_time == other.decay_time

class ParticleHeap:
    def __init__(self):
        self.heap = []
        heapq.heapify(self.heap)
    
    def push(self, particle: Particle):
        heapq.heappush(self.heap,particle)
    
    def pop(self) -> Particle:
        return heapq.heappop(self.heap)

    def is_empty(self) -> bool:
        return len(self.heap) == 0

def generate_particles(n: int) -> List[Particle]:
    list_of_particles = []
    for x in range(n):
        new_particle = Particle(n, random.randint(1,10))
        list_of_particles.append(new_particle)
    return list_of_particles

def simulate_collision(particle: Particle) -> Tuple[bool, Particle]:
       
    if random.random() > 0.5:
        return (True, Particle(particle.id, particle.decay_time * 2))
    else:
        return (False, None)

def simulate_decay(particles: List[Particle]) -> List[Tuple[int, float]]:
    heap = ParticleHeap()
    for particle in particles:
        heap.push(particle)
    
    decay_events = []
    while not heap.is_empty():
        particle = heap.pop()
        decay_events.append((particle.id, particle.decay_time))
        
        collided, new_particle = simulate_collision(particle)
        if collided:
            heap.push(new_particle)
    
    return decay_events

