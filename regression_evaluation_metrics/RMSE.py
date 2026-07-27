from sklearn.metrics import mean_squared_error
import numpy as np

real_scores=[90,60,80,100]
pred_scores=[85,70,70,95]
Mse=mean_squared_error(real_scores,pred_scores)
print(np.sqrt(Mse))