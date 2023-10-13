import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_data(df):
    # Convert 'date' column to datetime data type if needed
    df['date'] = pd.to_datetime(df['date'])

    # Extract the year from the 'date' column
    df['Year'] = df['date'].dt.year

    # Group the data by year and calculate the sum of sales for each year
    sales_by_year = df.groupby('Year')['Sales'].sum().reset_index()

    # Create a bar plot to visualize sales by year
    plt.figure(figsize=(12, 6))
    sns.barplot(x='Year', y='Sales', data=sales_by_year)
    plt.title('Sales by Year')
    plt.xlabel('Year')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Line plot to visualize sales over time
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='date', y='Sales', data=df)
    plt.title('Retail Sales Over Time')
    plt.xlabel('Date')
    plt.ylabel('Sales')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()





