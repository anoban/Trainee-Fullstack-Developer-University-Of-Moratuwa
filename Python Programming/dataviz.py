import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np
import pandas as pd

# data visualizations for univariate data 
# best options are bar plots, histograms, pie charts & box plots

# bivariate data visualizations show the relationship between two variables
# best options include scatter plots, violin plots, subplots

# multivariate data visualizations reveal relationships between more than two variables
# these can be 3d plots, tree maps or pair plots

np.random.seed(2022-5-12)
nums = np.random.randint(0,100,1000)
covariate = np.sqrt(np.power(nums,3))
plt.plot(nums, covariate, color = "yellow", markersize = 5, linestyle = "none", marker = "o", markeredgecolor = "black")
plt.show()

plt.hist(nums, bins = np.arange(0,100,11), color = "blue")
plt.show()

# seaborn has built-in themes to style plots
# an intro to seaborn plots
# replots - relational plots: scatter plot & line plots
# displots - dustribution plots: histplot, kdeplot, rugplot & ecdfplot
# catplots - categorical plots: stripplot, swarmplot, boxplot, violinplot, pointplot & barplot

penguins = pd.read_csv("D:/Data Analysis with R Programming/Week 1/penguins.csv")
penguins.columns
plt.plot(penguins[penguins.species == "Adelie"].flipper_length_mm, penguins[penguins.species == "Adelie"].body_mass_g, color = "blue", marker = "o", linestyle = "none")
plt.plot(penguins[penguins.species == "Gentoo"].flipper_length_mm, penguins[penguins.species == "Gentoo"].body_mass_g, color = "orange", marker = "o", linestyle = "none")
plt.plot(penguins[penguins.species == "Chinstrap"].flipper_length_mm, penguins[penguins.species == "Chinstrap"].body_mass_g, color = "red", marker = "o", linestyle = "none")
plt.show()

plt.plot(penguins.flipper_length_mm, penguins.body_mass_g, color = penguins.species, marker = "o", linestyle = "none")
plt.show()
# wont work here :(

sb.set_theme()
sb.jointplot(data = penguins, y = "flipper_length_mm", x = "body_mass_g", hue = "species")
plt.show()