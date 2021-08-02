from tables import array


class Tables:
    def load(self, data: array):
        n = self.verifica_a_maior_combinacao(data)
        s = self.cria_delimitador(n)
        table = self.loadtables(data, n, s)
        print(table)

    def loadtables(self, data, config, delimitator):
        rows = ''
        for i in data:
            row = ''
            for j, val in enumerate(i, start=0):

                pass_width = config[j] - len(i[j])
                
                row = "{}{}".format(row, self.cria_atrributo(val ,pass_width))
            
            rows = "{}|{}\n{}\n".format(rows, row, delimitator)

        return"{}\n{}".format(delimitator, rows)
    
    def cria_delimitador(self, n):
        s = ''
        for _ in range(sum(n)):
            s = "{}-".format(s)
        return "+---{}--+".format(s)

    def cria_atrributo(self, value, n_spaces):
        return " {}{} |".format(value,"".join([' '] * n_spaces))

    def verifica_a_maior_combinacao(self, data):
        arr_num = [0] * len(data[0])
        for i in data:
            for j, val in enumerate(i, start=0):
                val_len = len(val)
                if (len(val) > arr_num[j]):
                    arr_num[j] = val_len
        return arr_num
