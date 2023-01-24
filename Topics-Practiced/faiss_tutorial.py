import numpy as np 
import faiss  # this will import the faiss library

dimension = 128    # dimensions of each vector                         
n = 200    # number of vectors                   
np.random.seed(1)             
db_vectors = np.random.random((n, dimension)).astype('float32')

nlist = 5  # number of clusters
quantiser = faiss.IndexFlatL2(dimension) 
index = faiss.IndexIVFFlat(quantiser, dimension, nlist, faiss.METRIC_L2)
print(index.is_trained)   # False
index.train(db_vectors)  # train on the database vectors
print(index.ntotal)   # 0
index.add(db_vectors)   # add the vectors and update the index
print(index.is_trained)  # True
print(index.ntotal)   # 200

# print(dir(faiss))
# [print(method) for method in dir(faiss) if method.startswith('__') is False]