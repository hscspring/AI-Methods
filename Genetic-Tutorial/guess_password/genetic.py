# coding:utf-8

import random

def _generate_parent(length, gene_set):
    genes = []
    while len(genes) < length:
        # 与目标长度的距离
        sample_size = min(length - len(genes), len(gene_set))
        # 扩展至目标长度
        genes.extend(random.sample(gene_set, sample_size))
    return ''.join(genes)

def _mutate(parent, gene_set):
    # This fixes the problem with randint() which includes the endpoint;
    # in Python this is usually not what you want.
    # randrange 不包括 endpoint，也就是左边是闭区间，右边是开区间
    index = random.randrange(0, len(parent))
    # 可以写成继承
    child_genes = list(parent)
    new_gene, alternate = random.sample(gene_set, 2)
    # 尽量保证每一次的突变有 “变化”
    # 可以改成如果相等重新生成，不过测试了一下，会出现和 parent 一样的情况，现在这种不会
    child_genes[index] = alternate if new_gene == child_genes[index] else new_gene
    return ''.join(child_genes)

def get_best(get_fitness, target_len, optimal_fitness, gene_set, display):
    random.seed()
    best_parent = _generate_parent(target_len, gene_set)
    best_fitness = get_fitness(best_parent)
    display(best_parent)

    # 如果一下就生成 目标值，直接返回
    if best_fitness >= optimal_fitness:
        return best_parent

    n = 0
    while 1:
        # 关键在 ”突变“
        child = _mutate(best_parent, gene_set)
        child_fitness = get_fitness(child)
        n += 1
        if best_fitness >= child_fitness:
            continue
        display(child)
        if child_fitness >= optimal_fitness:
            print("Has spent %s steps." % n)
            return child
            break
        best_fitness = child_fitness
        best_parent = child
