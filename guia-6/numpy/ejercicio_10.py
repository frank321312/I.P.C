import numpy as np

def metros_a_cubrir(cant_metro):
    return np.linspace(0, cant_metro, num=cant_metro)

print(metros_a_cubrir(5))