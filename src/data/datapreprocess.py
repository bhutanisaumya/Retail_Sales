import pandas as pd
import seaborn as sns
import warnings
from datetime import datetime
from scipy.stats import skew
from sklearn.preprocessing import PowerTransformer
from sklearn.impute import SimpleImputer

class DataProcessor:
    def __init__(self):
        pass

    def explore_data(self, df):
        # Display basic data exploration for a given DataFrame
        print("First 5 rows:")
        print(df.head())

        print("\nLast 5 rows:")
        print(df.tail())

        print("\nDescriptive statistics:")
        print(df.describe())

        print("\nInfo:")
        print(df.info())

        print("\nShape:")
        print(df.shape)

    def melt_sales_data(self, sales_data, id_vars=['store_id', 'cat_id', 'item_id'], variable_name='Day', value_name='Sales'):
        # Select columns having days as d_num
        dept_sales = sales_data.columns[6:]
        
        # Melt the DataFrame
        melted_sales_data = pd.melt(sales_data, id_vars=id_vars, value_vars=dept_sales,
                                    var_name=variable_name, value_name=value_name)
        
        return melted_sales_data

    def dataset_duration(self, df):
        # Convert the 'date' column to datetime format
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate the difference between the maximum and minimum dates in days
        total_days = (df['date'].max() - df['date'].min()).days
        
        # Calculate the number of years by dividing days by 365.25 (accounting for leap years)
        total_years = total_days / 365.25
        
        # Print the duration in days and years
        print(total_days, 'days')
        print(total_years, 'years')
        
        # Return the duration as a tuple (days, years)
        return total_days, total_years

def main():
    # Set up warnings
    warnings.filterwarnings('ignore')
    
    # Initialize the DataProcessor class
    data_processor = DataProcessor()

    # Process and explore the data (you need to load the data first)
    # data_processor.explore_data(train_data)
    # Create an instance of the DataProcessor class


    # Call the dataset_duration method on the instance
    total_days, total_years = data_processor.dataset_duration(self)


if __name__ == "__main__":
    main()
