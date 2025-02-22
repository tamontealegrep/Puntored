
import pandas as pd

#------------------------------------------------------------------------------------

def data_types_table(df):
    """
    Generate a table with the data types of each column in the DataFrame.

    Parameters:
        df (pandas.DataFrame): DataFrame to check data types.

    Returns:
        pandas.DataFrame: A table with column names and their corresponding 
            data types. Sorted by data type.
    """

    data_types = df.dtypes.to_frame("Data Type")
    data_types.index.name = "Column Name" 

    return data_types

def missing_values_table(df, message=False):
    """
    Generate a table with the number and percentage of missing values for each 
    column in the DataFrame.

    Parameters:
        df (pandas.DataFrame): DataFrame to check for missing values.
        message (bool, optional): If True, prints a summary message. Default is False.

    Returns:
        pandas.DataFrame: A table with columns for the number of missing values, 
                the percentage of missing values, and the data type of each column.
    """
    
    missing_values = df.isnull().sum()
    missing_percent = (missing_values / len(df) * 100).round(2)

    missing_table = pd.DataFrame({
        "Missing Values": missing_values,
        "% of Total Values": missing_percent,
    })
    
    missing_table = missing_table.sort_values(by="% of Total Values", ascending=False)

    if message:
        num_columns = missing_table[missing_table["Missing Values"] > 0].shape[0]
        print(
            f"Your selected DataFrame has {df.shape[1]} columns and {df.shape[0]} rows.\n"
            f"There are {num_columns} columns that have missing values."
        )

    return missing_table

def describe_dataframe(df, columns):
    """
    Compute summary statistics, skewness, and kurtosis for the specified 
    columns in a DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list): A list of column names to compute statistics for.

    Returns:
        pandas.DataFrame: A DataFrame with summary statistics, including count, mean, 
                standard deviation, percentiles (1%, 5%, 25%, 50%, 75%, 95%, 99%), 
                iqf, min, max, skewness, and kurtosis.
    """
    
    sub_df = df[columns]
    
    stats = {
        col: [
            sub_df[col].count(),
            sub_df[col].mean(),
            sub_df[col].std(),
            sub_df[col].min(),
            sub_df[col].quantile(0.01),
            sub_df[col].quantile(0.05),
            sub_df[col].quantile(0.25),
            sub_df[col].median(),
            sub_df[col].quantile(0.75),
            sub_df[col].quantile(0.95),
            sub_df[col].quantile(0.99),
            sub_df[col].max(),
            sub_df[col].quantile(0.75) - sub_df[col].quantile(0.25),
            sub_df[col].skew(),
            sub_df[col].kurt()
        ]
        for col in sub_df.columns
    }

    stats_df = pd.DataFrame.from_dict(
        stats, 
        orient="index",
        columns=[
            "count", "mean", "std", "min", "1%", "5%", "25%", "50%", "75%", 
            "95%", "99%", "max", "iqf", "skewness", "kurtosis"
        ]
    )

    stats_df = stats_df.transpose()
    stats_df.index.name = "statistic"
    
    return stats_df

#------------------------------------------------------------------------------------