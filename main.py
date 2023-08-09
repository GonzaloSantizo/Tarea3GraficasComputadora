import shaders
from gl import Renderer, V2, color

width = 1000
height = 1000

rend = Renderer(width,height)

rend.vertexShader = shaders.vertexShader
rend.fragmentShader = shaders.fragmentShader
#rend.glCamMatrix(translate=(1,2,0))
rend.glLookAt(camPos=(-5,-5,-5),eyePos=(0,0,-3))
#distancia de camera x,y,z
#distancia de camara x,y,y

# Modelo 1
rend.glLoadModel(filename="model.obj",textureName="model.bmp",translate=(0,0,-5),rotate=(0,0,0),scale=(1,1,1))

rend.glRender()
rend.glFinish("output.bmp")