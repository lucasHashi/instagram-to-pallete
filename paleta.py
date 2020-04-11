import cor

class Paleta(object):
    def __init__(self, cores = [cor.Cor, cor.Cor, cor.Cor, cor.Cor, cor.Cor]):
        self.cores = cores

    def __str__(self):
        paleta_str = [ str(cor) for cor in self.cores ]
        return str(paleta_str).replace("', '", "'\n'")
    
    def get_paleta(self):
        return self.cores
    
    def set_paleta(self, cores):
        self.cores = cores