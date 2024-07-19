# -*- coding: utf-8 -*-
import random

from cu.edu.cujae.daf.context import Configuration
from cu.edu.cujae.daf.core import AlgorithmCreator
from cu.edu.cujae.daf.context.dataset.loader import AnnotatedFileLoader
from cu.edu.cujae.daf.randomize import Randomize
from cu.edu.cujae.daf.utils import IO

results = []

# Función Objetivo
def objetiveFunction(hyper, type, number, run, iter):  
    contentToWrite = "Trials = 50000\nSave Metrics = 1\nAtt Amplitude Factor = 2\nCrossover Probability = {}\nDominance Overlap Threshold = 0.5\nH = 13\nMax Ind Replace = 2\nMin Substitution Percent = 5\nMutation Probability = {}\nNeighborhood Crossover Probability = {}\nNumber of Objectives = 3\nRedundancy Overlap Threshold = 0.75\nT = 10".format(round(hyper[0], 2), round(hyper[1], 2), round(hyper[2], 2))
    IO.writeFile("{}".format("./hyperparameters"), contentToWrite)

    repetitions = 3
    partitions = 10

    dinos = AlgorithmCreator.classicDinos()
    config = Configuration.loadRawFile("./hyperparameters", '=')

    template = {"Elapsed Time": 0, "Weighted Relative Accuracy": 0.0}
    results.append("Dataset, Crossover Probability, Mutation Probability, Neighborhood Crossover Probability, Runtime, Weighted Relative Accuracy")
    
    datasetResults = template
    total_patterns = 0

    for rep in range(1, repetitions + 1):
        repetitionResults = template

        for part in range(1, partitions + 1):
            exp_path = "./results/{}_MH_{}/run{}/iter{}/rep{}_part{}".format(type, number, run, iter, rep, part)
            dataset = AnnotatedFileLoader.apply("./dataset/appendicitis/appendicitis-10-{}tra.dat".format(part), ",")

            seed = random.randint(0, 2**32 - 1)
            Randomize.setSeed(seed)
            dinos.setContext(dataset, config)
            dinos.run()

            metrics = dinos.runMetrics().last()
            total_patterns += metrics.externalPopSize()
            
            repetitionResults["Weighted Relative Accuracy"] = repetitionResults.get("Weighted Relative Accuracy", 0.0) + (metrics.metricsResult().apply("Weighted Relative Accuracy"))
            repetitionResults["Elapsed Time"] = repetitionResults.get("Elapsed Time", 0) + (metrics.elapsedTime() / 1000.0)

            print("Finished partition {} of repetition {} for appendicitis dataset with {} subgroups\n".format(part, rep, metrics.externalPopSize()))
            
            subgroups = dinos.retrieveSubgroups()
            subgroups_str = "\n".join(map(str, subgroups))
            IO.writeFile("{}_rules.csv".format(exp_path), subgroups_str)

            IO.writeFile("{}_cov.csv".format(exp_path), patternCoverage(dinos.retrieveCoverage()))

        for record in repetitionResults.items():
            accum = repetitionResults[record[0]] + record[1]
            repetitionResults[record[0]] = accum

        datasetResults.update(repetitionResults)
    
    values = {"Weighted Relative Accuracy": datasetResults.get("Weighted Relative Accuracy", 0.0) / float(total_patterns), 
              "Elapsed Time": datasetResults.get("Elapsed Time", 0.0) / float(total_patterns)}

    datasetPerformance("appendicitis", values, hyper)

    print("Finished appendicitis dataset with an average of {} subgroups".format(total_patterns / 30))
    IO.writeFile("./results/{}_MH_{}/run{}/iter{}/dataset_result.csv".format(type, number, run, iter), '\n'.join(results))

def patternCoverage(cov_data):
    srt = []
    list_element = list(cov_data)
    new = []
    size = len(list_element)
    
    for i in range(size):
        element = list_element[i]
        mtx = list(element._1())
        cov = list(element._2())
        new.append((mtx, cov))
    
    for (mtx, cov) in new:
        mtx_str = ','.join(map(str, mtx))
        cov_str = ','.join(map(str, cov))
        formatted_line = "{},{}\n".format(mtx_str, cov_str)
        srt.append(formatted_line)
    
    result_string = ''.join(srt)
    return result_string

def datasetPerformance(dataset_name, values, hyper):
    results.append("{}, {}, {}, {}, {}, {}".format(dataset_name, round(hyper[0], 2), round(hyper[1], 2), round(hyper[2], 2), values["Elapsed Time"], values["Weighted Relative Accuracy"]))
    print(results)


# Resultados de las ejecuciones
def allResults(type, number, run):
    results = []
    iterations = 1

    for iter in range(1, iterations + 1):
        exp_path = "./results/{}_MH_{}/run{}/iter{}".format(type, number, run, iter)
        reader = str(IO.readFile("{}/dataset_result.csv".format(exp_path)).last()).split(", ")

        results.append("Iteration, Dataset, Crossover Probability, Mutation Probability, Neighborhood Crossover Probability, Runtime, Weighted Relative Accuracy")
        results.append("{}, {}, {}, {}, {}, {}, {}".format(iter, reader[0], reader[1], reader[2], reader[3], reader[4], reader[5]))
        print(results)
        IO.writeFile("./results/{}_MH_{}/run{}/all_results.csv".format(type, number, run), '\n'.join(results))


# Ejemplo
objetiveFunction([0.25756756, 0.453634644, 0.647475678], "S", 1, 1, 1)
allResults("S", 1, 1)
            