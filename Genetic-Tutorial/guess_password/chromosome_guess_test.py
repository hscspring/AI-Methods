# coding:utf-8

import datetime
import unittest
import click
import chromosome_genetic

# @click.command()
# @click.option('--lens', help='Length of PassWord.')
class GuessPasswordTests(unittest.TestCase):

    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    
    def test_guess(self):
        target = "I LOVE YOU!"
        print(self.guess_pwd(target, 11))
    def guess_long(self, lens):
        target = "For I am fearfully and wonderfully made."
        print(self.guess_pwd(target, lens))

    def guess_pwd(self, target, lens):
        start_time = datetime.datetime.now()

        def fn_getfitness(genes):
            return get_fitness(genes, target)

        def fn_display(candidate):
            display(candidate, start_time)

        optimal_fitness = len(target)
        best = chromosome_genetic.get_best(fn_getfitness, lens, optimal_fitness, self.gene_set, fn_display)
        self.assertEqual(best.Genes, target)
        return best.Genes

def get_fitness(genes, target):
    # zip 是把两个列表组合在一起，这样返回的就是和目标值一样的字母数量
    result = sum(1 for expected, actual in zip(target, genes) if expected == actual)
    return result

def display(candidate, start_time):
    time_diff = datetime.datetime.now() - start_time
    if candidate.Fitness % 5 == 0:
        print("%s %s %s" % (candidate.Genes, candidate.Fitness, str(time_diff)))

if __name__ == '__main__':
    GuessPasswordTests().guess_long(40)
    print()
    unittest.main()
