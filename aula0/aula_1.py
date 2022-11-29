import pandas as pd
import seaborn as sns

notas = pd.read_csv(
    'D:\\Programming\\Python\\DataScience\\Alura\\aula0\\ml-latest-small\\ratings.csv')

notas.columns = ['userId', 'filme', 'nota', 'momento']

sns.boxplot(notas.nota)
