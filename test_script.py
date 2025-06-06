import pandas as pd

# Sample DataFrame creation
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8],
    'C': [9, 10, 11, 12]
}
df = pd.DataFrame(data)

# Function to calculate the sum of a specific column
def calculate_column_sum(dataframe, column_name):
    """
    Calculate the sum of a specified column in a DataFrame.

    Parameters:
    dataframe (pd.DataFrame): The DataFrame to operate on.
    column_name (str): The name of the column to sum.

    Returns:
    int or float: The sum of the specified column.
    """
    if column_name in dataframe.columns:
        return dataframe[column_name].sum()
    else:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
# Example usage
try:
    column_sum = calculate_column_sum(df, 'B')
    print(f"The sum of column 'B' is: {column_sum}")
except ValueError as e:
    print(e)
    
