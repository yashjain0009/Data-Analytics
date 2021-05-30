import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sktime.datasets import load_airline
from sktime.forecasting.model_selection import temporal_train_test_split
from sktime.performance_metrics.forecasting import smape_loss
from sktime.utils.plotting.forecasting import plot_ys

y=load_airline()
fig,ax=plot_ys(y)
ax.set(xlabel="Time",ylabel="Number")
plt.show()