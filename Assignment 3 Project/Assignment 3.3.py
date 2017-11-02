import numpy as np
import sklearn.metrics as sk
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import difflib as df
import xlrd

doc = xlrd.open_workbook('Data/classprobs.xls').sheet_by_index(0)
true_class = doc.col_values(0)
pred1 = doc.col_values(1)
pred2 = doc.col_values(2)

FP1, TP1, thresh1 = sk.roc_curve(true_class, pred1)
FP2, TP2, thresh2 = sk.roc_curve(true_class, pred2)

plt.plot(FP1, TP1, 'r--', FP2, TP2, 'g--')
plt.plot([0, 1], [0, 1], c='purple')
red_patch = mpatches.Patch(color='red', label='Predicition 1')
green_patch = mpatches.Patch(color='green', label='Prediction 2')
purple_patch = mpatches.Patch(color='purple', label='Lucky guess')
plt.legend(handles=[red_patch,green_patch,purple_patch])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC diagram')
plt.show()

AUC1 = sk.roc_auc_score(true_class,pred1)
AUC2 = sk.roc_auc_score(true_class,pred2)
print AUC1
print AUC2

pred1_class = []
pred2_class = []

for i in range(0,np.size(pred1)):
    if pred1[i] < 0.5:
        pred1_class.append(0.0)
    else:
        pred1_class.append(1.0)

for i in range(0,np.size(pred2)):
    if pred2[i] < 0.5:
        pred2_class.append(0.0)
    else:
        pred2_class.append(1.0)

truth_rate1 = df.SequenceMatcher(None,true_class,pred1_class).ratio()
truth_rate2 = df.SequenceMatcher(None,true_class,pred2_class).ratio()

print truth_rate1
print truth_rate2

matrix_1 = sk.confusion_matrix(true_class,pred1_class)
matrix_2 = sk.confusion_matrix(true_class,pred2_class)
print matrix_1
print matrix_2




