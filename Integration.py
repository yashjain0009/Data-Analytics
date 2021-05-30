import scipy.integrate as sci
import numpy as np
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt
def f(x):
    return np.sin(x)+0.5*x
a=0.5
b=9.5
x=np.linspace(0,10)
y=f(x)
fig,ax=plt.subplots()
plt.plot(x,y,'b',linewidth=2)
plt.ylim(ymin=0)
Ix=np.linspace(a,b)
Iy=f(Ix)
c=list(zip(Ix,Iy))
z=(b,0)
q=(a,0)
c.append(z)
c.insert(0,q)
poly=Polygon(c,edgecolor='0.5',facecolor='0.7')
plt.text(0.75 * (a + b), 1.5, r"$\int_a^b f(x)dx$",horizontalalignment='center', fontsize=20)
plt.figtext(0.92, 0.075, '$x$')
plt.figtext(0.075, 0.9, '$f(x)$')
ax.set_xticks((a, b))
ax.set_xticklabels(('$a$', '$b$'))
ax.set_yticks([f(a), f(b)])
ax.add_patch(poly)
plt.show()
