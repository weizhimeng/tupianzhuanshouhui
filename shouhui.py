from PIL import Image
import numpy as np

a = np.asarray(Image.open('./images.jpeg').convert('L')).astype('float')

depth = 10.
#分别取梯度值
grad = np.gradient(a)
grad_x,grad_y = grad
grad_x = grad_x * depth/100.
grad_y = grad_y * depth/100.
A = np.sqrt(grad_x ** 2 + grad_y ** 2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
#光源俯视角度
vec_e1 = np.pi/2.2
#光源方位角度
vec_az = np.pi/4
#光源对x,y,z轴的影响
dx = np.cos(vec_e1)*np.cos(vec_az)
dy = np.cos(vec_e1)*np.sin(vec_az)
dz = np.sin(vec_e1)

b = 255*(dx * uni_x + dy * uni_y + dz * uni_z)
b = b.clip(0,255)

im = Image.fromarray(b.astype('uint8'))
im.save('./images1.jpeg')