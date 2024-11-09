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
    
    def push(self, particle: Particle):
        # TODO: Implement using heapq function call
        pass
    
    def pop(self) -> Particle:
        # TODO: Implement using heapq functional call
        pass
    
    def is_empty(self) -> bool:
        # TODO: Implement
        pass

def generate_particles(n: int) -> List[Particle]:
    # TODO: Implement
    pass

def simulate_collision(particle: Particle) -> Tuple[bool, Particle]:
    # TODO: Implement where chance of collision is 50%
    # I.e., collision occurs if random.random() < 0.5
    pass

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