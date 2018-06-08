# https://www.datascience.com/blog/k-means-clustering

import numpy as np
from sklearn.cluster import KMeans
import pandas as pd

data = pd.read_csv('kmeans.csv')
print("Input data and shape")
print(data.shape)

### For the purposes of this example, we store feature data from our
### data in the `f1` and `f2` arrays. We combine this into
### a feature matrix `X` before entering it into the algorithm.
f1 = data['DistanceFeature'].values
f2 = data['SpeedingFeature'].values

X = np.array(list(zip(f1,f2)))
kmeans = KMeans(n_clusters=2)
kmeans = kmeans.fit(X)
labels = kmeans.predict(X)
centroids = kmeans.cluster_centers_

print("Final centroids")
print(centroids)
