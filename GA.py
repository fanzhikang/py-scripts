import numpy as np

DNA_SIZE = 10
POP_SIZE = 100
CROSS_RATE = 0.8
MUTATION_RATE = 0.03
N_GENARATIONS = 200
X_BOUND = [0,5]

def F(x):
    return np.sin(10*x)*x + np.cos(2*x)*x

def get_fitness(pred):
    return pred + 1e-3 - np.min(pred)

def translateDNA(pop):
    return pop.dot(2**np.arange(DNA_SIZE)[::-1])/float(2**DNA_SIZE-1)*X_BOUND[1]

def select(pop, fitness):
    idx = np.random.choice(np.arange(POP_SIZE),size=POP_SIZE, replace=True,
    p=fitness/fitness.sum())
    return pop[idx]

def crossover(parent, pop):
    if np.random.rand()<CROSS_RATE:
        i = np.random.randint(0,POP_SIZE,size=1)
        cross_points = np.random.randint(0,2,DNA_SIZE).astype(np.bool)
        parent[cross_points] = pop[i,cross_points]
    return parent

def mutate(child):
    for point in range(DNA_SIZE):
        if np.random.rand()<MUTATION_RATE:
            child[point]=1 if child[point]==0 else 0
    return child

pop = np.random.randint(2,size=(POP_SIZE,DNA_SIZE))

for _ in range(N_GENARATIONS):
    F_values = F(translateDNA(pop))

    fitness = get_fitness(F_values)
    print('Most fitted DNA: ',pop[np.argmax(fitness),:])
    pop = select(pop, fitness)
    pop_copy = pop.copy()
    for parent in pop:
        child =crossover(parent,pop_copy)
        child = mutate(child)
        parent[:] = child

