import gym 
import numpy as np

def load_frozen_lake(desc=None, map_name=None, is_slippery=False):

    if desc is None and map_name is None:
        #desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
        desc =[ ['S','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F']]
        map_name = '8x8'
        
    return gym.make('FrozenLake-v1', desc, map_name, is_slippery)

np.random.seed(0)
desc =[ ['S','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F'],
                ['F','F','F','F','F','F','F','F']]
env = load_frozen_lake()
print(env.desc)
print(env.P[0][0])
env = load_frozen_lake(is_slippery=True)
print(env.desc)
print(env.P[0][0])
desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
print(env.desc)
env = load_frozen_lake(map_name='4x4')
print(env.desc)
