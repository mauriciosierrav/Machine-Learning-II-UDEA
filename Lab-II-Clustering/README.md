## Workshop Solution

1. ***Spectral Clustering Method:***

    **a.** It is generally useful when the data have a nonlinear structure or when the clusters have complex shapes. It is particularly useful when the data have an underlying graph structure, where each data point can be considered a node in a graph and the similarity between data points can be expressed as edge weights. 
    ####
    **b.** It is based on graph theory and linear algebra. It involves the following steps: Affinity matrix construction: given a set of data points, an affinity matrix is constructed that encodes the similarities between pairs of data points. The affinity matrix can be constructed using various measures, such as the Gaussian similarity function or the k-nearest neighbor graph. Calculation of the Laplacian matrix: The Laplacian matrix is derived from the affinity matrix and is used to capture the underlying structure of the data. Finding the eigenvectors and eigenvalues of the Laplacian matrix: These eigenvectors represent the principal directions of the data, and the eigenvalues represent the variance of the data in these directions. Clustering the data: In spectral clustering, the data points are projected onto the eigenvectors corresponding to the smallest eigenvalues and clustered in this lower dimensional space.
    ####
    **c.** El algoritmo se puede describir de la siguiente manera:

   1. **Entrada:** Una matriz de similitud S, el número de clusters k
   2. Calcular la matriz Laplaciana L
      - Calcular la matriz de similitud S
      - Calcular la matriz diagonal de grado D
      - Calcular la matriz Laplaciana L = D - S
   3. Calcular los vectores propios de L
      - Calcular los primeros k vectores propios de L
      - Ordenarlos como columnas de una matriz X
   4. Agrupar las filas de X usando k-means
      - Aplicar k-means a las filas de X para obtener k clusters
   5. Asignar cada punto de datos a su centro de cluster más cercano
   6. **Salida** de los clusters
   ####
   **d.** Yes, spectral clustering has some relationships with PCA, t-SNE and SVD.

   1. **PCA (Principal Component Analysis)** is a technique used to transform data into a new coordinate system by finding the directions of maximum variance in the data. Similarly, in spectral clustering, we find a new coordinate system to transform the data. Instead of using the directions of maximum variance, we use the eigenvectors of the Laplacian matrix.
   2. **t-SNE (t-SNE (t-Stochastic Neighbor Embedded Distribution)** is a nonlinear dimensionality reduction technique that finds a lower dimensional representation of high dimensionality data such that similarities between pairs of data are preserved. Spectral clustering can also be used for dimensionality reduction, but is generally used for clustering rather than visualization.
   3. **SVD (Singular Value Decomposition)** is a matrix decomposition technique that decomposes a matrix into three matrices. Spectral clustering uses the eigenvalue decomposition of the Laplacian matrix, which is a similar concept. However, the Laplacian matrix is a specific type of matrix used in graph theory, while SVD can be applied to any type of matrix.
####
2. **DBSCAN Method:**

   **a.** DBSCAN can be particularly useful in the following cases: Data with unknown or arbitrary shapes: It can cluster data points with arbitrary shapes and sizes, which makes it particularly useful when the structure of the data is not known in advance. Data sets with high dimensionality: It can handle data sets with high dimensionality, as it does not rely on distance metrics that become unreliable in high dimensionality spaces. Datasets with noise and outliers: It can handle datasets with noise and outliers effectively, as it can identify and discard them as noise points. Spatial data: It is particularly effective in clustering spatial data. Large datasets: It is a scalable algorithm that can handle large datasets efficiently, making it particularly useful in big data applications.

   Applications requiring real-time processing: It is a fast algorithm that can be used in real-time applications.
   ####
   **b.** The mathematical foundations of DBSCAN include: Density: The density of a point is defined as the number of points within a specified ε (epsilon) distance from that point. Center points: A point is considered a center point if there are at least MinPts (minimum points) within a distance ε from that point. Edge points: A point is considered an edge point if it is within a distance ε of a center point, but has less than MinPts points within a distance ε of itself. Noise points: A point is considered a noise point if it is neither a center point nor an edge point.
   ####
   **c.** There is no direct relationship between DBSCAN and Spectral Clustering. Both are clustering algorithms that can be used for different types of data and have their own strengths and weaknesses, they are fundamentally different in their approach and mathematical foundations. However, both algorithms are part of the family of density-based clustering methods, meaning that they rely on the concept of density to group similar data points.
####
3. **Elbow Method:**

   It is used to estimate the optimal number of clusters in a data set for clustering algorithms. The method involves plotting the variance (or other measures of clustering quality) as a function of the number of clusters and selecting the value at which the rate of decrease decreases sharply, creating an "elbow" in the curve. This method seeks to identify the point at which adding more clusters does not significantly improve clustering quality, and therefore select the optimal number of clusters.
   ####
   The method has some limitations that may affect its ability to assess clustering quality accurately. One of the main problems is that the optimal number of clusters can be subjective and context dependent. In addition, the shape of the curve can also be influenced by noise in the data, which can lead to misinterpretation. Another limitation is that it only considers one measure of clustering quality, and other measures may be more relevant or informative for a particular data set. Finally, the method assumes that clusters are spherical, of equal size and evenly spaced, which may not be true for all data sets.
####
4. Both ***KMeans*** module and the ***KMedoids*** module were implemented in version 0.0.2 of the _unsupervised_ Python package. This can be installed  using  `pip install dimensionality_reductions_jmsv`. 

   In this [repository](https://github.com/mauriciosierrav/dimensionality-reduction-jmsv.git) you can see the implementation.
####
5. Click [here](workshop_solution/Punto5.ipynb) to go to the solution of point 5
####
6. Click [here](workshop_solution/Punto6.ipynb) to go to the solution of point 6
