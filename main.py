# Imports necessários
import random
from deap import creator, base, tools, algorithms
MAX_WEIGHT = 30
print(f"peso maximo : {MAX_WEIGHT}\n")
def createItems(numItems):
    items = []
    for x in range(numItems):
        items.append({"weight": random.randint(1,10), "value": random.uniform(1, 100)})
    return items

# items = [{'weight': 10, 'value': 35.64110058808632},
# {'weight': 2, 'value': 54.69880643006783}, 
# {'weight': 9, 'value': 31.65301313515851} ,
# {'weight': 4, 'value': 16.24477511072319} ,
# {'weight': 7, 'value': 53.44643551529447} ,
# {'weight': 9, 'value': 79.28002328835994} ,
# {'weight': 5, 'value': 98.30979709437615} ,
# {'weight': 8, 'value': 36.13315327585151} ,
# {'weight': 7, 'value': 19.222853326291055},
# {'weight': 3, 'value': 61.84489311209864} ]

items = createItems(10)
print("items: ")
for item in items:
    print(item)

# Define o tipo fitness: Um objetivo com maximização
creator.create("FitnessMax", base.Fitness, weights=(1.0,))

# Define o tipo indivíduo: indivíduo do tipo list (array) com
# a fitness definida anteriormente.
creator.create("Individual", list, fitness=creator.FitnessMax)

# Toolbox para inicialização de componentes do algoritmo
toolbox = base.Toolbox()

# Atributo booleano criado de forma aleatório
toolbox.register("attr_bool",
                 random.random)

# Indivíduo (tipo Inidividual) criado a partir do atributo definido
# anteriormente. Ou seja, indivíduo do tipo booleano.
# São criados 100 indivíduos. initRepeat faz esse papel
toolbox.register("individual",
                 tools.initRepeat, creator.Individual, toolbox.attr_bool, n=10)

# Criação da população, do tipo lista composto
# por indivíduos (individual)
toolbox.register("population",
                 tools.initRepeat, list, toolbox.individual)



# Criação da função de fitness.
# A função recebe um indivíduo e retorna uma tupla
# que representa a avaliação do indivíduo


def evalOneMax(individual):
    value = 0
    weight = 0
    for index in range(len(individual)):
        if individual[index] > 0.5:
            value += items[index]['value']
            weight += items[index]['weight']
    if (weight > MAX_WEIGHT):
        return 100000000, 0
    return weight, value

def getItems(individual):
    _items = []
    for index in range(len(individual)):
        if individual[index] > 0.5:
            _items.append((index,items[index]))
    return _items

# registra a função de fitness
toolbox.register("evaluate", evalOneMax)

# registro dos operadores
toolbox.register("mate", tools.cxTwoPoint)  # crossover
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)  # mutação

# registro do método de seleção
toolbox.register("select", tools.selTournament, tournsize=3)

# tamanho da população
population = toolbox.population(n=300)


# iniciando o processo de evolução

NGEN = 40  # número de gerações
for gen in range(NGEN):

    # O módulo algorithms implementa vários algoritmos evolucionários
    # Na documentação tem a lista:
    # https://deap.readthedocs.io/en/master/api/algo.html
    # varAnd aplica operações de mutação e crossover
    # cxpb: probabilidade de crossover
    # mutpb: probabilidade de mutação
    offspring = algorithms.varAnd(population, toolbox, cxpb=0.5, mutpb=0.1)

    # avalia cada indivíduo
    fits = toolbox.map(toolbox.evaluate, offspring)

    # associa cada indivíduo ao seu valor de fitness
    for fit, ind in zip(fits, offspring):
        ind.fitness.values = [fit[1]]

    # aplica a seleção para gerar a nova população
    population = toolbox.select(offspring, k=len(population))

# retorna o k melhor indivíduos da última população
top10 = tools.selBest(population, k=10)

# Imprime o melhor
print(top10[0])


_items = getItems(top10[0])
print('items\n')
for item in _items:
    print(item)
print("")

_weights = list(map(lambda x: x[1]['weight'], _items))
_values = list(map(lambda x: x[1]['value'], _items))
print(f"peso: {sum(_weights)} - valor: {sum(_values)} ")
