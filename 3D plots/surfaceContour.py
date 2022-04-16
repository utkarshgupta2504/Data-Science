# %% [markdown]
# ### Surface Plots
# - A 3D plot that can be visualised on the 3 axes
# - The values can be got using `meshgrid`

# %%
from mpl_toolkits.mplot3d import Axes3D  # This is required for script
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("dark_background")

# %% [markdown]
# #### Creating data

# %%
a = np.arange(-1, 1, 0.02)

a, b = np.meshgrid(a, a)

# %% [markdown]
# #### Plotting

# %%
fig = plt.figure(figsize=(8, 8))
axes = plt.axes(projection="3d")
axes.plot_surface(a, b, a**2 + b**2, cmap="rainbow")
plt.show()

# %% [markdown]
# ### Contour Plot
# - If we cut the surface plot using parallel planes
# - Color the points on the same plane with same color

# %%
fig = plt.figure(figsize=(8, 8))
axes = plt.axes(projection="3d")
axes.contour(a, b, a**2 + b**2, cmap="rainbow")
plt.show()
