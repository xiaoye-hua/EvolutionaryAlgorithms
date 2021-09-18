# -*- coding: utf-8 -*-
# @File    : test_Mutation.py
# @Author  : Hua Guo
# @Time    : 2021/9/18 上午10:33
# @Disc    :
import numpy as np
import copy
from unittest import TestCase

from src.Mutation import nonuniform_mutation


class TestMutation(TestCase):
    def setUp(self) -> None:
        self.pop = np.random.random([100, 265])

    def test_nonunifrom_mutation(self):
        res = nonuniform_mutation(copy.deepcopy(self.pop))
        print(res.shape)
        # self.assertTrue(res.any() != self.pop.any())