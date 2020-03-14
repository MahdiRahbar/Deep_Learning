#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 12:59:10 2020

@author: mahdi
"""
from deap import base, creator, tools, algorithms
from scipy.stats import bernoulli
from bitstring import BitArray
import model
# population_size = 10  # Too big
# num_generations = 15  # Takes for ever to run


class EA:

    def __init__(self, population_size, num_generations, gene_length, window_size_gen):
        self.population_size = population_size
        self.num_generations = num_generations
        self.gene_length = gene_length
        self.window_size_gen = window_size_gen
        self.unit_number_gen = self.gene_length - self.window_size_gen
        self.split_point = self.window_size_gen - 1
    SPLIT_POINT = self.split_point

    def evo_algorithm(self):
        # As we are trying to minimize the RMSE score, that's why using -1.0. |
        # In case, when you want to maximize accuracy for instance, use 1.0
        creator.create('FitnessMax', base.Fitness, weights=(1.0,))
        creator.create('Individual', list, fitness=creator.FitnessMax)

        toolbox = base.Toolbox()
        toolbox.register('binary', bernoulli.rvs, 0.5)
        toolbox.register('individual', tools.initRepeat, creator.Individual, toolbox.binary, n=gene_length)
        toolbox.register('population', tools.initRepeat, list, toolbox.individual)

        toolbox.register('mate', tools.cxOrdered)
        toolbox.register('mutate', tools.mutShuffleIndexes, indpb=0.6)
        toolbox.register('select', tools.selRoulette)
        toolbox.register('evaluate', deep_model)

        start_time = time.time()
        population = toolbox.population(n=population_size)
        r = algorithms.eaSimple(population, toolbox, cxpb=0.4, mutpb=0.1, ngen=num_generations, verbose=False)

        print('Finished in %.2f s' % (time.time() - start_time))

        best_individuals = tools.selBest(population, k=1)
        best_window_size = None
        best_num_units = None

        print(BitArray(best_individuals[0][0:6]).uint)

        for bi in best_individuals:
            window_size_bits = BitArray(bi[0:6])
            num_units_bits = BitArray(bi[6:])
            best_window_size = window_size_bits.uint
            best_num_units = num_units_bits.uint
            print('\nWindow Size: ', best_window_size, ', Num of Units: ', best_num_units)

        return best_window_size, best_num_units