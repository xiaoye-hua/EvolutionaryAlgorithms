# -*- coding: utf-8 -*-
# @File    : __init__.py.py
# @Author  : Hua Guo
# @Time    : 2021/9/18 上午9:49
# @Disc    :
import numpy as np


def nonuniform_mutation(population: np.ndarray, dist='cauchy') -> np.ndarray:
    """
    Non-normal mutation
        1. Gaussian distribution
        2. Cauchy distribution
    """
    if dist == "cauchy":
        sample_function = np.random.standard_cauchy
    elif dist == "gaussian":
        sample_function = np.random.normal
    else:
        print("Wrong dist paramters")
    mutation_pro = 0.3
    for f in range(0, len(population)):
        for i in range(0, len(population[f])):
            if np.random.uniform(0, 1) <= mutation_pro:
                noise = sample_function()
                population[f][i] = population[f][i] + noise
    return population