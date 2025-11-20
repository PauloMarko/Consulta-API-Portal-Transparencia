import pandas as pd


class LeitorCSV:
    def __init__(self, csv_file):
        self.csv_file = csv_file

    def ler(self):
        # with open(self.csv_file, mode='r', encoding='utf-8') as csvfile:
        #     tabela = csv.reader(csvfile, delimiter=',')
        #     for linha in tabela:
        #         cpf = linha[0]
        #         self.lista_cpfs.append(cpf)
        # return self.lista_cpfs

        df = pd.read_csv(self.csv_file)
        lista_cpfs = df['cpfs'].tolist()

        return lista_cpfs


if __name__ == "__main__":
    leitor = LeitorCSV("cpfs.csv")
    print(leitor.ler())
