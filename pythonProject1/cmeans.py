import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from scipy.spatial import distance
from sklearn.decomposition import PCA
import random
import warnings
warnings.filterwarnings('ignore')

class Fuzzy_C_Means:
    def __init__(self, data, clusters, fuzzifier, error_tolerance, iterations):
        self.z = data
        self.c = clusters
        self.m = fuzzifier
        self.e = error_tolerance
        self.l = iterations

    def compute_distance(self, x, V):
        return distance.cdist(x.T, V, 'euclidean').T

    def update_partition_matrix(self, dist, m):
        exp_dist = dist ** (2.0 / m - 1)
        return exp_dist / np.sum(exp_dist, axis=0, keepdims=1)

    def compute_clusters(self, x, U, m):
        exp_U = np.power(U, m)
        p1 = exp_U.dot(x.T)
        p2 = np.sum(exp_U, axis=1)
        p2 = np.reshape(p2, (-1, self.c))
        return np.divide(p1, p2.T)

    def cmeans(self):
        Datapoints, Features = self.z.shape

        x = self.z.T

        V = np.empty((self.l, self.c, Features))
        V[0] = np.array(x[:, np.random.choice(x.shape[1], size=self.c)].T)
        U = np.zeros((self.l, self.c, Datapoints))

        i = 0
        while True:
            distance = self.compute_distance(x, V[i])
            U[i] = self.update_partition_matrix(distance, self.m)
            V[i + 1] = self.compute_clusters(x, U[i], self.m)

            if np.linalg.norm(U[i + 1] - U[i]) < self.e:
                break

            i += 1

        return V[i], U[i]