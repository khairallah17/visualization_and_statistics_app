import streamlit as st
import numpy as np
import scipy.stats as stats

# Fonction pour saisir les données de l'utilisateur
def get_user_input_data():
    st.subheader("Enter Data")
    data1 = st.text_area("Enter data for Sample 1 (separate values with commas):", '1,2,3,4,5')
    data2 = st.text_area("Enter data for Sample 2 (separate values with commas):", '2,3,4,5,6')

    # Convertir les chaînes saisies en listes de nombres
    data1 = [float(i) for i in data1.split(',')]
    data2 = [float(i) for i in data2.split(',')]
    
    return np.array(data1), np.array(data2)

# Fonction pour effectuer un t-test
def perform_t_test(data1, data2):
    st.subheader("T-Test Result")
    
    # Exécution du t-test
    t_stat, p_val = stats.ttest_ind(data1, data2)

    st.write("T-statistic:", t_stat)
    st.write("P-value:", p_val)

# Fonction pour effectuer un z-test
def perform_z_test(data1, data2):
    st.subheader("Z-Test Result")
    
    # Calcul de la moyenne et de l'écart-type
    mean1, mean2 = np.mean(data1), np.mean(data2)
    std1, std2 = np.std(data1, ddof=1), np.std(data2, ddof=1)

    # Taille des échantillons
    n1, n2 = len(data1), len(data2)

    # Exécution du z-test
    z_stat = (mean1 - mean2) / np.sqrt(std1**2/n1 + std2**2/n2)
    p_val = stats.norm.sf(abs(z_stat)) * 2

    st.write("Z-statistic:", z_stat)
    st.write("P-value:", p_val)

# Fonction principale de l'application
def perform_tests():
    st.title("Statistical Tests with User Data")

    data1, data2 = get_user_input_data()

    # Choix du test à effectuer
    test_choice = st.sidebar.selectbox("Choose a test", ["T-Test", "Z-Test"])

    if test_choice == "T-Test":
        perform_t_test(data1, data2)
    elif test_choice == "Z-Test":
        perform_z_test(data1, data2)
