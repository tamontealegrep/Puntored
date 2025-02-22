
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler

#------------------------------------------------------------------------------------

def isolation_forest_clean(df, columns, contamination=0.05, return_outliers=False):
    """
    Cleans a DataFrame by detecting and removing outliers using Isolation Forest.

    Parameters:
        df (pandas.DataFrame): DataFrame to clean.
        columns (list): List of column names to use for outlier detection.
        contamination (float, optional): The proportion of outliers expected 
            in the data. Defaults to 0.05.
        return_outliers (bool, optional): Return the outliers Dataframe.
            Default False.

    Returns:
        pandas.DataFrame: A new DataFrame with outliers removed.
        pandas.DataFrame, optional: A DataFrame containing the rows identified as outliers
    """
    df = df.copy()
    scaler = StandardScaler()
    df[columns] = scaler.fit_transform(df[columns])

    model = IsolationForest(contamination=contamination)
    model.fit(df[columns])

    df['outlier'] = model.predict(df[columns])

    cleaned = df[df['outlier'] == 1].copy()
    outliers = df[df['outlier'] == -1].copy()

    cleaned.drop('outlier', axis=1, inplace=True)
    outliers.drop('outlier', axis=1, inplace=True)

    cleaned[columns] = scaler.inverse_transform(cleaned[columns])
    outliers[columns] = scaler.inverse_transform(outliers[columns])

    if return_outliers:
        return cleaned, outliers
    else:
        return cleaned
    
#------------------------------------------------------------------------------------