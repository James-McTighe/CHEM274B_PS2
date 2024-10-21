import unittest
# from gradescope_utils.autograder_utils.decorators import weight, number
from particle_simulator import Particle, ParticleHeap, generate_particles, simulate_collision, simulate_decay

class TestParticleSimulator(unittest.TestCase):
    # @weight(1)
    # @number("5.1")
    def test_particle_comparison(self):
        p1 = Particle(1, 10)
        p2 = Particle(2, 20)
        self.assertTrue(p1 < p2)
        self.assertFalse(p1 == p2)

    # @weight(1)
    # @number("5.2")
    def test_particle_heap(self):
        heap = ParticleHeap()
        particles = [Particle(i, i*10) for i in range(5, 0, -1)]
        for p in particles:
            heap.push(p)
        
        self.assertFalse(heap.is_empty())
        popped = heap.pop()
        self.assertEqual(popped.id, 1)

    # @weight(1)
    # @number("5.3")
    def test_generate_particles(self):
        n = 10
        particles = generate_particles(n)
        self.assertEqual(len(particles), n)
        self.assertTrue(all(isinstance(p, Particle) for p in particles))

    # @weight(1)
    # @number("5.4")
    def test_simulate_collision(self):
        particle = Particle(1, 10)
        collided, new_particle = simulate_collision(particle)
        if collided:
            self.assertIsNotNone(new_particle)
            self.assertEqual(new_particle.id, particle.id)
            self.assertGreater(new_particle.decay_time, particle.decay_time)
        else:
            self.assertIsNone(new_particle)

    # @weight(1)
    # @number("5.5")
    def test_simulate_decay(self):
        particles = generate_particles(5)
        decay_events = simulate_decay(particles)
        self.assertGreaterEqual(len(decay_events), 5)
        self.assertTrue(all(isinstance(event, tuple) for event in decay_events))
        self.assertTrue(all(len(event) == 2 for event in decay_events))