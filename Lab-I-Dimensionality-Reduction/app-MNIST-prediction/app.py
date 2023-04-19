import streamlit as st
import pickle
import numpy as np
from PIL import Image


#Load pickle files
with open('log_regr_PCA.pkl', 'rb') as lr1:
    log_regr_PCA = pickle.load(lr1)

with open('log_regr_SVD.pkl', 'rb') as lr2:
    log_regr_SVD = pickle.load(lr2)

with open('dr_PCA.pkl', 'rb') as dr1:
    dr_PCA = pickle.load(dr1)

with open('dr_SVD.pkl', 'rb') as dr2:
    dr_SVD = pickle.load(dr2)


def main():
    #titles
    st.title('MNIST digit classifier')
    st.sidebar.header('User Input Parameters')

    #select favorite model
    option = ['Logistic Regression PCA', 'Logistic Regression SVD']
    model = st.sidebar.selectbox('Which model you like to use?', option)

    # load image
    file = st.file_uploader("Upload any MNIST image", type=["jpg", "jpeg", "png"])
    if file is not None:
        image = Image.open(file).convert("L")
        st.image(image, width=100)

    # RUN button
    if st.button('RUN'):
        if model == 'Logistic Regression PCA':
            img_arr = np.array(image).flatten().reshape(1,-1)
            img_arr_ = dr_PCA.transform(img_arr)
            predict = log_regr_PCA.predict(img_arr_)
            st.success(f'Your image MNIST is a: {predict} using a Logistic Regresion model with PCA')
        elif model == 'Logistic Regression SVD':
            img_arr = np.array(image).flatten().reshape(1,-1)
            img_arr_ = dr_SVD.transform(img_arr)
            predict = log_regr_SVD.predict(img_arr_)
            st.success(f'Your image MNIST is a: {predict} using a Logistic Regresion model with SVD')
        else:
            st.success(f'Select some model')

if __name__ == '__main__':
    main()
