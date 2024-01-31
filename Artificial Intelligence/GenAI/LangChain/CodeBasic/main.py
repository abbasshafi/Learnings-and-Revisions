from langchain_community.document_loaders import TextLoader

loader = TextLoader("nvda_news_1.txt")
data = loader.load()


data[0].metadata

from langchain_community.document_loaders.csv_loader import CSVLoader
loader= CSVLoader('movies.csv',source_column='title')
data=loader.load()
len(data)

data[0].metadata

from langchain_community.document_loaders import UnstructuredURLLoader