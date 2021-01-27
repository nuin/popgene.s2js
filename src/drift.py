# Paulo Nuin Jan 2021

import os
import sys
import click
import json
import random
import logging
import coloredlogs
from collections import defaultdict

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
coloredlogs.install(level='DEBUG')

def calculate_frequency(population):
    """

    :param population:
    :return:
    """

    pass



@click.command()
@click.option('-p', '--pop-size', 'pop_size', default=100, help='Population size')
@click.option('-f', '--freq-A', 'freq_A', default=0.5, help='Initial A frequency')
@click.option('-n', '--n-generations', 'number_generations', default=100, help='Number of generations')
@click.option('-np','--n-populations', 'number_populations', default=10, help='Number of populations')
def create_generations(pop_size, number_generations, freq_A, number_populations):

    click.echo('Number of populations %d' % number_populations)
    click.echo('Population size %d' % pop_size)
    click.echo('Number of generations %d' % number_generations)
    click.echo('Initial frequency %f' % freq_A)

    # logger.info('Number of populations', number_populations)

    generations = []
    populations = []
    pop_json = {}
    scale = list(range(number_generations + 1))
    for n in range(1, number_populations + 1):
        frequency = []
        frequency.append(freq_A)
        logger.info('Generating population ' + str(n))
        for g in range(1, number_generations + 1):
            logger.info('Population ' + str(n) + ' - Randomzing generation ' + str(g))
            individuals = []
            genes = ''
            for p in range(pop_size):
                gene1 = random.uniform(0, 1)
                gene2 = random.uniform(0, 1)
                if gene1 <= frequency[g - 1]:
                    gene1 = 'A'
                else:
                    gene1 = 'a'
                if gene2 <= frequency[g - 1]:
                    gene2 = 'A'
                else:
                    gene2 = 'a'
                individuals.append(gene1 + gene2)
                genes += gene1 + gene2
            frequency.append(genes.count('A')/(pop_size*2))
        populations.append(frequency)

    for i, pop in enumerate(populations):
        pop_json['pop_' + str(i)] = pop

    # pop_json['scale'] = scale
    drift_output = open('drift.json', 'w')
    json.dump(pop_json, drift_output)
    drift_output.close()


if __name__ == '__main__':

    create_generations()