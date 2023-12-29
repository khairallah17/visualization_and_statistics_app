import streamlit as st
from data_exploration import perform_data_exploration
from statistics_laws import perform_statistics_laws

def main():
    st.title("Statistics Final Project")

    # Navigation bar
    menu = ["Home","Data Exploration", "statistics laws"]
    choice = st.sidebar.selectbox("Navigation", menu)

    # Page content based on the selected choice
    if choice == "Home":
        st.write("Welcome to Home App!")

    elif choice == "Data Exploration":
        perform_data_exploration()
        
    elif choice == "statistics laws":
        perform_statistics_laws()
    

# Run the Streamlit app
if __name__ == "__main__":
    main()
