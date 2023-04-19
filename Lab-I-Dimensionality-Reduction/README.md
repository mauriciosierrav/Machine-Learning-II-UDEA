## Workshop Solution
1. Click [here](workshop_solution/Punto1.ipynb) to go to the solution of point 1
####
2. Click [here](workshop_solution/Punto2.ipynb) to go to the solution of point 2
####
3. The _unsupervised_ Python package was published in **PyPI** and can be installed  using  `pip install dimensionality_reductions_jmsv`. 

   In this [repository](https://github.com/mauriciosierrav/dimensionality-reduction-jmsv.git) you can see the implementation.
####
4. Click [here](workshop_solution/Punto4.ipynb) to go to the solution of point 4
####
5. Click [here](workshop_solution/Punto5.ipynb) to go to the solution of point 5
####
6. Click [here](workshop_solution/Punto6.ipynb) to go to the solution of point 6
####
7. Click [here](workshop_solution/Punto7.ipynb) to go to the solution of point 7
####
8. Click [here](workshop_solution/Punto8.ipynb) to go to the solution of point 8
####
9. **What are the underlying mathematical principles behind UMAP? What is it useful for?**

    UMAP (Uniform Manifold Approximation and Projection) is a nonlinear dimensionality reduction technique. It is based on mathematical principles such as differential geometry, algebraic topology and information theory. 

    UMAP has several applications, some examples are: finding a low-dimensional geometric representation of high-dimensional data while maintaining the global and local structure of the data; visualization of high-dimensional data; identification of groups or clusters in the data; feature selection and exploration of the underlying structure of the data.

    UMAP is closely related to t-SNE as both are nonlinear dimensionality reduction techniques used to visualize high-dimensional data in a low-dimensional space; however UMAP offers some advantages: higher speed, better preservation of global structure and more understandable parameters, which makes UMAP a more effective tool for high-dimensional data visualization.
####
10. **What are the underlying mathematical principles behind LDA? What is it useful for?**

    LDA (Linear Discriminant Analysis) is a dimensionality reduction and classification technique. It is based on several underlying mathematical principles, such as probability theory and statistics, linear algebra and mathematical optimization.
   
    LDA has several applications, some examples are: projecting data into a lower dimensional space that maximizes the separation between classes, finding a set of linear discriminants that maximize the relationship between the between-class variance and the within-class variance; feature selection; exploring the underlying structure of the data; dimensionality reduction; and improving the efficiency of image processing.

    LDA is closely related to PCA as both are linear dimensionality reduction techniques used to find the most important features in the data; however LDA offers some advantages: it is a simple and computationally efficient algorithm; it can work well even when the number of features is much larger than the number of training samples; it can handle multicollinearity (correlation between features) in the data.
####
11. https://dimensionality-reduction-for-mnist-prediction.streamlit.app/
    
    Click [here](app-MNIST-prediction/app.py) to see the implementation.
    
    In this [directory](app-MNIST-prediction/MNIST_example) you can find MNIST images to test the performance of the model in the web app
