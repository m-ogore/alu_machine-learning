import numpy as np
load_frozen_lake = __import__('0-load_env').load_frozen_lake
def q_init(env):
    
    return np.zeros((env.observation_space.n,env.action_space.n))
