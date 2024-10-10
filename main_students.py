import pandas as pd

def main(query):
    df = pd.read_csv('./IMDB_top_1000.csv')
    print(df.head())
    # TODO: Completar esta función para realizar búsquedas semánticas con base en el código del archivo test.ipynb



if __name__ == '__main__':
    query = input('ingresa el termino de busqueda: ')
    main(query)