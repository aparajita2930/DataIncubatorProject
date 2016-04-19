import time
from datetime import datetime
import csv
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cross_validation import train_test_split
from sklearn.cross_validation import StratifiedShuffleSplit
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import StratifiedKFold
import matplotlib.pyplot as plt


print "Script start at ", datetime.now().isoformat()

X=np.load('F:/NYU/DataIncubator/Cancer/numpy_array.npy')
Y=X[:,:3] #patient_id cancer_type tissue_type
X=X[:,3:] #rpm

RS=np.random.RandomState(90)
perm=RS.permutation(678)

Y=Y[perm]
X=X[perm]

X_train, X_test, Y_train, Y_test = train_test_split(X, Y[:,1], test_size=0.25, random_state=30, stratify=Y[:,1])

num_comp = []
per_variance = []
for n in (0.99, 0.90, 0.75, 0.65, 0.5):
	p=PCA(n_components=n).fit(X_train)
	print(p.explained_variance_)
	print n*100, len(p.explained_variance_)
	num_comp.append(len(p.explained_variance_))
	per_variance.append(n*100)
	

	
plt.title('Number of Principal Components vs Expectational Variance')
plt.bar(per_variance, num_comp, width=5, color="blue")
plt.ylabel('Number of Principal Components')
plt.xlabel('% Variance')
plt.axis([45, 105, 0, 10])
plt.show()