# -*- coding: utf-8 -*-
"""avaliador notas

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1xxuq6Tokhi3lObdDj-SXOujrKUh2kebZ
"""

notas = [85,65,98,62,56,75,62,85,95,92,72,92,62,42,89,97,83,95,72]
media = 70


while True:
  try:
    novas_notas = input("digite as novas notas separadas por vírgula: ")
    novas_notas = [int(nota) for nota in novas_notas.split(",")]
    notas.extend(novas_notas)
    break
  except ValueError:
    print(f"erro!, certifique-se de digitar apenas números separados por vírgula.")



alunos_aprovados = []
alunos_reprovados = []

for nota in notas:
  if nota >= media:
    alunos_aprovados.append(nota)
  else:
    alunos_reprovados.append(nota)



print(f"Notas: {notas}")
print(f"Media: {media}")
print(f"Alunos aprovados: {alunos_aprovados}")
print(f"Alunos reprovados: {alunos_reprovados}")
print(f"Quantidade de alunos aprovados: {len(alunos_aprovados)} ")
print(f"Quantidade de alunos reprovados: {len(alunos_reprovados)} ")

