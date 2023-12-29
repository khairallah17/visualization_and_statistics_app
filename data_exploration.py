# data_exploration.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mplcursors

def perform_data_exploration():
    st.header("Data Exploration")

    # File upload section
    data_file = st.file_uploader("Upload Data File", type=["csv", "txt", "xlsx", "xls", "html"])

    if data_file is not None:
        try:
            if data_file.type == 'application/vnd.ms-excel':
                df = pd.read_excel(data_file)
            else:
                df = pd.read_csv(data_file)

            # Display DataFrame
            st.write("### Uploaded DataFrame:")
            st.write(df)

            # Sidebar controls
            st.sidebar.subheader("Data Options")

            # Display DataFrame columns
            if st.sidebar.checkbox("Show Columns"):
                st.write("### DataFrame Columns:")
                st.write(df.columns.tolist())

            # Display specific line using df.loc
            if st.sidebar.checkbox("Show Specific Line"):
                line_number = st.sidebar.slider("Enter specific line number:", 0, len(df) - 1, 0)

                st.write("### Loc (Specific Line) Result:")
                st.write(df.loc[line_number])

            # Display specific range using df.loc
            if st.sidebar.checkbox("Show Specific Range"):
                start_line = st.sidebar.slider("Enter start line for range:", 0, len(df) - 1, 0)
                end_line = st.sidebar.slider("Enter end line for range:", start_line, len(df) - 1, len(df) - 1)

                st.write("### Loc (Specific Range) Result:")
                st.write(df.loc[start_line:end_line])

            # Select specific columns
            if st.sidebar.checkbox("Select Columns by Name"):
                selected_columns = st.sidebar.multiselect("Select column(s) by name:", df.columns.tolist())
                st.write("### Selected Columns:")
                st.write(df[selected_columns])

            # Display length of DataFrame
            if st.sidebar.checkbox("Show Length of DataFrame"):
                st.write("### Length of DataFrame:")
                st.write(f"**Length of DataFrame:** {len(df)}")

            # Group by specific column and display mean
            if st.sidebar.checkbox("Group by and Display Mean"):
                groupby_column = st.sidebar.selectbox("Select column for grouping:", df.columns.tolist())
                grouped_df = df.groupby(groupby_column)[[groupby_column]].mean()
                st.write("### Grouped DataFrame (Mean):")
                st.write(grouped_df)

            # Line Plot based on user input
            if st.sidebar.checkbox("Line Plot"):
                x_column_line = st.sidebar.selectbox("Select x-axis column for Line Plot:", df.columns.tolist())
                y_columns_line = st.sidebar.multiselect("Select y-axis column(s) for Line Plot:", df.columns.tolist())
                st.write("### Line Plot:")
                line_plot(df, x_column_line, y_columns_line)

            # Scatter Plot based on user input
            if st.sidebar.checkbox("Scatter Plot"):
                x_column_scatter = st.sidebar.selectbox("Select x-axis column for Scatter Plot:", df.columns.tolist())
                y_column_scatter = st.sidebar.selectbox("Select y-axis column for Scatter Plot:", df.columns.tolist())
                st.write("### Scatter Plot:")
                scatter_plot(df, x_column_scatter, y_column_scatter)

            # Boxplot based on user input
            if st.sidebar.checkbox("Boxplot"):
                x_column_boxplot = st.sidebar.selectbox("Select x-axis column for Boxplot:", df.columns.tolist())
                y_column_boxplot = st.sidebar.selectbox("Select y-axis column for Boxplot:", df.columns.tolist())
                st.write("### Boxplot:")
                boxplot(df, x_column_boxplot, y_column_boxplot)

            # Histogram based on user input
            if st.sidebar.checkbox("Histogram"):
                x_column_hist = st.sidebar.selectbox("Select column for Histogram:", df.columns.tolist())
                st.write("### Histogram:")
                histogram(df, x_column_hist)

            # KDE Plot based on user input
            if st.sidebar.checkbox("KDE Plot"):
                x_column_kde = st.sidebar.selectbox("Select column for KDE Plot:", df.columns.tolist())
                st.write("### KDE Plot:")
                kde_plot(df, x_column_kde)

            # Violin Plot based on user input
            if st.sidebar.checkbox("Violin Plot"):
                x_column_violin = st.sidebar.selectbox("Select x-axis column for Violin Plot:", df.columns.tolist())
                y_column_violin = st.sidebar.selectbox("Select y-axis column for Violin Plot:", df.columns.tolist())
                st.write("### Violin Plot:")
                violin_plot(df, x_column_violin, y_column_violin)

            # Bar Plot based on user input
            if st.sidebar.checkbox("Bar Plot"):
                x_column_bar = st.sidebar.selectbox("Select x-axis column for Bar Plot:", df.columns.tolist())
                y_column_bar = st.sidebar.selectbox("Select y-axis column for Bar Plot:", df.columns.tolist())
                st.write("### Bar Plot:")
                bar_plot(df, x_column_bar, y_column_bar)

            # Pie Chart based on user input
            if st.sidebar.checkbox("Pie Chart"):
                pie_column = st.sidebar.selectbox("Select column for Pie Chart:", df.columns.tolist())
                st.write("### Pie Chart:")
                pie_chart(df, pie_column)

        except Exception as e:
            st.error(f"An error occurred: {e}")

def line_plot(data, x_column, y_columns):
    st.subheader("Line Plot")

    # Set Seaborn style
    sns.set()

    # Create a line plot with hover
    fig, ax = plt.subplots(figsize=(10, 6))
    for y_column in y_columns:
        sns.lineplot(x=data[x_column], y=data[y_column], marker='o', label=f'{y_column}', ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel="Values")  # You can customize the y-axis label
    ax.set_title(f'Line Plot: {", ".join(y_columns)} vs {x_column}')

    # Show legend
    ax.legend()

    # Display details on hover
    hover = st.sidebar.checkbox("Display Details on Hover")
    if hover:
        tooltips = [(col, f"@{col}") for col in [x_column] + y_columns]
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text('\n'.join([f"{label}: {sel.artist.get_array()[sel.index]:.2f}" for label, sel in zip(*sel.target)])), target=ax, tooltips=tooltips)

    # Show the plot
    st.pyplot(fig)

def scatter_plot(data, x_column, y_column):
    st.subheader("Scatter Plot")

    # Set Seaborn style
    sns.set()

    # Create a scatter plot with hover
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=data[x_column], y=data[y_column], marker='o', ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel=y_column)
    ax.set_title(f'Scatter Plot: {y_column} vs {x_column}')

    # Display details on hover
    hover = st.sidebar.checkbox("Display Details on Hover")
    if hover:
        tooltips = [(col, f"@{col}") for col in [x_column, y_column]]
        mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text('\n'.join([f"{label}: {sel.artist.get_array()[sel.index]:.2f}" for label, sel in zip(*sel.target)])), target=ax, tooltips=tooltips)

    # Show the plot
    st.pyplot(fig)

def boxplot(data, x_column, y_column):
    st.subheader("Boxplot")

    # Set Seaborn style
    sns.set()

    # Create a boxplot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(x=data[x_column], y=data[y_column], ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel=y_column)
    ax.set_title(f'Boxplot: {y_column} vs {x_column}')

    # Show the plot
    st.pyplot(fig)

def histogram(data, x_column):
    st.subheader("Histogram")

    # Set Seaborn style
    sns.set()

    # Create a histogram
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data[x_column], bins=30, kde=True, ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel="Frequency")
    ax.set_title(f'Histogram: {x_column}')

    # Show the plot
    st.pyplot(fig)

def kde_plot(data, x_column):
    st.subheader("KDE Plot")

    # Set Seaborn style
    sns.set()

    # Create a KDE plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data[x_column], fill=True, ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel="Density")
    ax.set_title(f'KDE Plot: {x_column}')

    # Show the plot
    st.pyplot(fig)

def violin_plot(data, x_column, y_column):
    st.subheader("Violin Plot")

    # Set Seaborn style
    sns.set()

    # Create a violin plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(x=data[x_column], y=data[y_column], ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel=y_column)
    ax.set_title(f'Violin Plot: {y_column} vs {x_column}')

    # Show the plot
    st.pyplot(fig)

def bar_plot(data, x_column, y_column):
    st.subheader("Bar Plot")

    # Set Seaborn style
    sns.set()

    # Create a bar plot
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=data[x_column], y=data[y_column], ax=ax)

    # Add labels and title
    ax.set(xlabel=x_column, ylabel=y_column)
    ax.set_title(f'Bar Plot: {y_column} vs {x_column}')

    # Show the plot
    st.pyplot(fig)

def pie_chart(data, column):
    st.subheader("Pie Chart")

    # Set Seaborn style
    sns.set()

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 8))
    data[column].value_counts().plot.pie(autopct='%1.1f%%', startangle=90, ax=ax)

    # Add title
    ax.set_title(f"Pie Chart: {column}")

    # Show the plot
    st.pyplot(fig)

if __name__ == "__main__":
    perform_data_exploration()
