


#import pywhatkit as KT

from PIL import Image # type: ignore

#palmeiras
imagem = Image.open("yourImage.png")


#medio: 
largura, altura = 40 , 26 

# largura, altura = 60 , 37 
# largura, altura = 200 , 90


#quadrado bom
# largura, altura = 300 , 140
#pequeno:
#largura, altura = 200 , 100 

imagem = imagem.resize((largura, altura))
imagem = imagem.convert("L")

# caracteres_ascii = [" ", ".", "-", "*", ":", "=", "+", "#", "%", "@"]
caracteres_ascii = [" ", "/", "*", ";", "=", "+", "#", "%", "@"]         ##    !@#$%¨&*(_+=´

pixels = imagem.load()
ascii_image = ""

for y in range(altura):
    for x in range(largura):
        pixel = pixels[x, y]
        ascii_char = caracteres_ascii[int((pixel/255)*(len(caracteres_ascii)-1))]
        ascii_image += ascii_char
    ascii_image += "\n"

print(ascii_image)
