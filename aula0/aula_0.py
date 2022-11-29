import pandas as pd

notas = pd.read_csv(
    'D:\\Programming\\Python\\DataScience\\Alura\\aula0\\ml-latest-small\\ratings.csv')

print(notas.shape)

notas.columns = ['ID', 'Filme', 'Nota', 'Momento']
print(notas.columns)

print(notas['Nota'].unique())

print(notas['Nota'].value_counts())

print(notas['Nota'].mean())
