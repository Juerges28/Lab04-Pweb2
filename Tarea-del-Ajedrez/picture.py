from colors import *
class Picture:
  def __init__(self, img):
    self.img = img

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    return Picture(self.img[::-1])

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    horizontal = []
    for row in self.img:
        horizontal.append(row[::-1])
    return Picture(horizontal)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []
    for row in self.img:
      negative_row = [self._invColor(pixel) for pixel in row]
      negative.append(negative_row)
    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    return Picture(None)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p bajo la figura actual """
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
    new_img = self.img + p.img
    return Picture(new_img)
  
  def insert(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual hacia abajo
        la cantidad de veces que indique el valor de n """
    return Picture(None)
  
          
