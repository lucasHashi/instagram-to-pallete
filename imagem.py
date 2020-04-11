from colorthief import ColorThief

class Imagem(object):
    def __init__(self, caminho):
        self.caminho = caminho
        self.gerar_paleta()
    
    def gerar_paleta(self):
        furta_cor = ColorThief(self.caminho)
        
        # Pegar cor dominante
        self.cor_dominante = furta_cor.get_color(quality=1)
        # Pegar paleta de 5 cores, em qualidade 5 (vem como padrao 10)
        self.paleta = furta_cor.get_palette(color_count=5, quality=5)
    
    def __str__(self):
        imagem_str = 'Cor dominante:\n'
        imagem_str += str(self.cor_dominante)+'\nPaleta RGB:\n'

        paleta_str = str(self.paleta)

        imagem_str += paleta_str
        return imagem_str