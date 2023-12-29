import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def plot_distribution(data, title):
    st.subheader(title)
    sns.set()
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data, kde=True, ax=ax)
    ax.set_title(title)
    st.pyplot(fig)

def generate_statistical_samples():
    st.sidebar.subheader("Statistical Distributions")
    distribution = st.sidebar.selectbox("Choose a distribution", ["Bernoulli", "Binomial", "Normal", "Poisson", "Uniform", "Exponential"])

    if distribution == "Bernoulli":
        p = st.sidebar.slider('Probability of Success', 0.0, 1.0, 0.5)
        data = np.random.binomial(1, p, 1000)
        plot_distribution(data, "Bernoulli Distribution")

    elif distribution == "Binomial":
        n = st.sidebar.slider('Number of Trials', 1, 100, 10)
        p = st.sidebar.slider('Probability of Success', 0.0, 1.0, 0.5)
        data = np.random.binomial(n, p, 1000)
        plot_distribution(data, "Binomial Distribution")

    elif distribution == "Normal":
        mu = st.sidebar.number_input('Mean', value=0.0)
        sigma = st.sidebar.number_input('Standard Deviation', value=1.0)
        data = np.random.normal(mu, sigma, 1000)
        plot_distribution(data, "Normal Distribution")

    elif distribution == "Poisson":
        lam = st.sidebar.slider('Rate', 0, 10, 2)
        data = np.random.poisson(lam, 1000)
        plot_distribution(data, "Poisson Distribution")

    elif distribution == "Uniform":
        a = st.sidebar.number_input('Lower Bound', value=0.0)
        b = st.sidebar.number_input('Upper Bound', value=1.0)
        data = np.random.uniform(a, b, 1000)
        plot_distribution(data, "Uniform Distribution")

    elif distribution == "Exponential":
        lam = st.sidebar.slider('Rate', 0.1, 2.0, 1.0)
        data = np.random.exponential(lam, 1000)
        plot_distribution(data, "Exponential Distribution")
        
def perform_statistics_laws():
    st.title("Statistical Distribution Generator")
    generate_statistical_samples()
