import sys
import numpy as np
import dagger as dag
import matplotlib.pyplot as plt

ny,nx = 256,256
dy,dx = 200,200
Urate = 5e-4
dt = 50000
Kr = 1e-5
Ks = 2e-5
dep = 4
rshp = (ny,nx)
prec = np.full(rshp, 1.7, dtype = np.float32)
ts = dag.trackscape()
# Initialising the topography and its dimensions
ts.init_random(nx, ny,dx,dy,"4edges")

# FUnctions to set parameters as global homogeneous values (if not initialised, there is a default value)
ts.set_single_Kr(Kr)
ts.set_m(0.6)
ts.set_n(2)
ts.set_dt(dt)

ts.set_variable_precipitations(prec)


print("begin")

for i in range(20):
	ts.standalone_implicit_SPL()
	ts.block_uplift(Urate,dt)
	print(i)
print("end")

fig,ax = plt.subplots()

ax.imshow(ts.get_topo().reshape(rshp), cmap = "gist_earth")

plt.show()