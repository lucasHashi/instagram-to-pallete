
class Cor(object):
    def __init__(self, rgb=[0,0,0]):
        self.rgb_r, self.rgb_g, self.rgb_b = rgb
    
    def set_rgb(self, rgb):
        self.r, self.rgb_g, self.rgb_b = rgb
    
    def get_rgb(self):
        return [self.rgb_r, self.rgb_g, self.rgb_b]
    
    def __str__(self):
        r = '00'+str(self.rgb_r) if(self.rgb_r < 10) else '0'+str(self.rgb_r) if(self.rgb_r < 100) else str(self.rgb_r)
        g = '00'+str(self.rgb_g) if(self.rgb_g < 10) else '0'+str(self.rgb_g) if(self.rgb_g < 100) else str(self.rgb_g)
        b = '00'+str(self.rgb_b) if(self.rgb_b < 10) else '0'+str(self.rgb_b) if(self.rgb_b < 100) else str(self.rgb_b)
        
        return '{}, {}, {}'.format(r, g, b)