# -*- coding: utf-8 -*-
"""ts.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RLVYFIGrCKaaJ41Cr81XSLkFft03CXxV
"""

#TS
import random
import math

# Biblioteca para geração de graficos para facilitar visualizão
import matplotlib.pyplot as plt

MAX_NUMERO_DE_ITERACOES_TABU = 4000
MEMORIA_MAXIMA = 10
memoria = []

def executar_tabu_search():

  # É gerada uma solução inicial aleatoria
  solucao_atual = gerar_solucao_aleatoria_n_rainhas()

  # É calculado o fitness da solução incial
  melhor_fitness = fitness_n_rainhas(solucao_atual)

  # É definido um criterio de parada
  numero_de_iteracoes = MAX_NUMERO_DE_ITERACOES_TABU

  # print('Fitness Inicial: ', melhor_fitness)

  # --- Inicio da execução do algoritimo ---

  # Criterio de parada
  for i in range(0, numero_de_iteracoes):

    # Uma nova solução é gerada
    nova_solucao = mudar_solucao_n_rainhas(solucao_atual)

    solucao_ja_testada = True
    while solucao_ja_testada:
      for k in memoria:
        for z in range(0, NUMERO_DE_RAINHAS):
          if k[z].x == nova_solucao[z].x:
            solucao_ja_testada = True
            break
      else:
        solucao_ja_testada = False
      if solucao_ja_testada:
        nova_solucao = realizar_mudanca_na_solucao(solucao_atual)
 
    if len(memoria) == MEMORIA_MAXIMA:
      memoria.pop(0)
    memoria.append(copy.deepcopy(nova_solucao))

    # A nova solução é comparada com a anterior
    if fitness_n_rainhas(nova_solucao) <= fitness_n_rainhas(solucao_atual):
      # Caso ela seja melhor a anterior é substituida pela nova
      solucao_atual.clear()
      for j in range(0, NUMERO_DE_RAINHAS):
        solucao_atual.append(nova_solucao[j])
      # e o melhor fitness é atualizado
      melhor_fitness = fitness_n_rainhas(solucao_atual)

  return melhor_fitness