"""
Pyramid H Language - Core Algorithmic Implementation
Author: Fadwa (2026)
Description: A constructive framework to simulate finite numerical growth 
and measure prime symmetry bridges (n - d, n + d).
"""

import math

def is_prime(num: int) -> bool:
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

class PyramidH:
    def __init__(self):
        self.H = [1]
        self.apex = 1

    def grow_to(self, target_n: int):
        while self.apex < target_n:
            self.apex += 1
            self.H.append(self.apex)

    def find_bridges(self, n: int) -> list:
        bridges = []
        for d in range(0, n):
            p1 = n - d
            p2 = n + d
            if is_prime(p1) and is_prime(p2):
                bridges.append((d, p1, p2))
        return bridges

if __name__ == "__main__":
    pyramid = PyramidH()
    target = 10
    pyramid.grow_to(target)
    bridges_10 = pyramid.find_bridges(target)
    print(f"--- Pyramid H Simulation at Apex n = {target} ---")
    print(f"Total active bridges found: {len(bridges_10)}")
    for d, p1, p2 in bridges_10:
        print(f"  Bridge d = {d} -> ({p1}, {p2})")

    target_large = 1000
    bridges_large = pyramid.find_bridges(target_large)
    print(f"\n--- Simulation at Apex n = {target_large} ---")
    print(f"Total active bridges: {len(bridges_large)}")
    print(f"Smallest bridge d: {bridges_large[0][0]} -> ({bridges_large[0][1]}, {bridges_large[0][2]})")
    print(f"Largest bridge d:  {bridges_large[-1][0]} -> ({bridges_large[-1][1]}, {bridges_large[-1][2]})")
