# coding:utf-8

import random
import statistics
import time

class Chromosome:
    Genes = None
    Fitness = None

    def __init__(self, genes, fitness):
        self.Genes = genes
        self.Fitness = fitness

class Benchmark:
    pass


def _generate_parent(length, gene_set, get_fitness):
    genes = []
    while len(genes) < length:
        # 与目标长度的距离
        sample_size = min(length - len(genes), len(gene_set))
        # 扩展至目标长度
        genes.extend(random.sample(gene_set, sample_size))
    genes = ''.join(genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

def _mutate(parent, gene_set, get_fitness):
    # This fixes the problem with randint() which includes the endpoint;
    # in Python this is usually not what you want.
    # randrange 不包括 endpoint，也就是左边是闭区间，右边是开区间
    index = random.randrange(0, len(parent.Genes))
    # 可以写成继承
    child_genes = list(parent.Genes)
    new_gene, alternate = random.sample(gene_set, 2)
    # 尽量保证每一次的突变有 “变化”
    # 可以改成如果相等重新生成，不过测试了一下，会出现和 parent 一样的情况，现在这种不会
    child_genes[index] = alternate if new_gene == child_genes[index] else new_gene
    genes = ''.join(child_genes)
    fitness = get_fitness(genes)
    return Chromosome(genes, fitness)

def get_best(get_fitness, target_len, optimal_fitness, gene_set, display):
    random.seed()
    best_parent = _generate_parent(target_len, gene_set, get_fitness)
    display(best_parent)

    # 如果一下就生成 目标值，直接返回
    if best_parent.Fitness >= optimal_fitness:
        return best_parent

    n = 0
    while 1:
        # 关键在 ”突变“
        child = _mutate(best_parent, gene_set, get_fitness)
        n += 1
        if best_parent.Fitness >= child.Fitness:
            continue
        display(child)
        if child.Fitness >= optimal_fitness:
            print("Has spent %s steps." % n)
            return child
        best_parent = child
