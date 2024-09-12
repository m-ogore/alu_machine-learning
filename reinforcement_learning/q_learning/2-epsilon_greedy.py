import numpy as np
def epsilon_greedy(Q, state, epsilon):
    
    p = np.random.uniform(0, 1)

    if p < epsilon:
        action = np.argmax(Q[state])
    else:
        action = np.random.randint(Q[state])

    return action
load_frozen_lake = __import__('0-load_env').load_frozen_lake
q_init = __import__('1-q_init').q_init

desc = [['S', 'F', 'F'], ['F', 'H', 'H'], ['F', 'F', 'G']]
env = load_frozen_lake(desc=desc)
Q = q_init(env)
Q[7] = np.array([0.5, 0.7, 1, -1])
np.random.seed(0)
print(epsilon_greedy(Q, 7, 0.5))
np.random.seed(1)
print(epsilon_greedy(Q, 7, 0.5))