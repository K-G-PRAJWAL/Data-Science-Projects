import streamlit as st
import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Simple Iris Flower Prediciton Web App

An app that predicts the iris flower type.
""")

st.sidebar.header("Input flower parameters")

def user_input_features():
  sepal_length = st.sidebar.slider('sepal_length', 4.3, 7.9, 5.4)
  sepal_width = st.sidebar.slider('sepal_width', 2.0, 4.4, 3.4)
  petal_length = st.sidebar.slider('petal_length', 1.0, 6.9, 1.3)
  petal_width = st.sidebar.slider('petal_width', 0.1, 2.5, 0.2)
  data = {
    'sepal_length': sepal_length,
    'sepal_width': sepal_width,
    'petal_length': petal_length,
    'petal_width': petal_width
  }
  features = pd.DataFrame(data, index=[0])
  return features

df = user_input_features()

st.subheader("User Input parameters")
st.write(df)

iris = datasets.load_iris()
x = iris.data
y = iris.target

clf = RandomForestClassifier()
clf.fit(x, y)

prediction = clf.predict(df)
prediction_probability = clf.predict_proba(df)

st.subheader("Class labels and their index number")
st.write(iris.target_names)

st.subheader("Prediction")
st.write(iris.target_names[prediction])

st.subheader("Prediction Probability")
st.write(prediction_probability)