import pandas as pd 
df = pd.read_csv('/_queries/1SCARED.csv')
df_reorder = df[['Title', 'Authors', 'Journal/Book', 'Publication Year', 'DOI', 'PMID', 'Citation', 'First Author', 'Create Date', 'PMCID', 'NIHMS ID']]
df_reorder.to_csv('/sample_reorder.csv')