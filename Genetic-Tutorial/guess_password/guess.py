# coding:utf-8

import click
import datetime
import genetic

@click.command()
def run():
    target = "I LOVE YOU!"
    print(guess_pwd(target))

def guess_pwd(target):
    gene_set = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!."
    start_time = datetime.datetime.now()

    def fn_getfitness(genes):
        return get_fitness(genes, target)

    def fn_display(genes):
        display(genes, target, start_time)

    optimal_fitness = len(target)
    return genetic.get_best(fn_getfitness, len(target), optimal_fitness, gene_set, fn_display)

def get_fitness(genes, target):
    # zip 是把两个列表组合在一起，这样返回的就是和目标值一样的字母数量
    return sum(1 for expected, actual in zip(target, genes) if expected == actual)

def display(genes, target, start_time):
    time_diff = datetime.datetime.now() - start_time
    fitness = get_fitness(genes, target)
    if fitness % 5 == 0:
        print("%s %s %s" % (genes, fitness, str(time_diff)))

if __name__ == '__main__':
    run()

