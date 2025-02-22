
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, auc

#------------------------------------------------------------------------------------

def create_subplots(
    plot_function, data, classes, num_rows, num_cols,
    title="", title_font_size=16, fig_size=(5, 5),
    share_x=False, share_y=False, **kwargs
) -> None:
    """
    Create a figure with a grid of subplots and apply a plotting function 
    to each subplot.

    Parameters:
        plot_function (function): The function applied to each subplot. 
            It should accept three parameters: the subplot axis, the DataFrame, and the class label.
        data (pandas.DataFrame): The DataFrame containing the data for plotting.
        classes (list): A list of class labels or identifiers.
        num_rows (int): The number of rows in the subplot grid.
        num_cols (int): The number of columns in the subplot grid.
        title (str, optional): The title for the entire figure. Defaults to "".
        title_font_size (int, optional): Font size for the figure title. Defaults to 16.
        fig_size (tuple, optional): Figure size (width, height) in inches. Defaults to (5, 5).
        share_x (bool, optional): Whether to share the x-axis across subplots. Defaults to False.
        share_y (bool, optional): Whether to share the y-axis across subplots. Defaults to False.
        **kwargs: Additional keyword arguments passed to `plot_function`.

    Raises:
        ValueError: If the number of classes exceeds the number of available subplots.

    Returns:
        None
    """
    total_subplots = num_rows * num_cols

    if len(classes) > total_subplots:
        raise ValueError("Number of classes exceeds the number of available subplots.")

    # Special case for a single subplot
    if total_subplots == 1:
        fig, ax = plt.subplots(figsize=fig_size)
        plot_function(ax, data, classes[0], **kwargs)
        ax.set_title(title)
        plt.show()
        return

    fig, axs = plt.subplots(
        nrows=num_rows, ncols=num_cols, figsize=fig_size,
        sharex=share_x, sharey=share_y
    )

    if title:
        fig.suptitle(title, fontsize=title_font_size)

    axs = axs.flatten()

    for i, cls in enumerate(classes):
        plot_function(axs[i], data, cls, **kwargs)

    # Remove any unused subplots
    for j in range(len(classes), total_subplots):
        fig.delaxes(axs[j])

    fig.tight_layout()
    plt.show()

def boxplot_function(ax, data, class_label,**kwargs):
    """
    Create a boxplot on the given subplot axis using the provided DataFrame.

    Parameters:
        ax (matplotlib.axes.Axes): The subplot axis to draw the boxplot.
        data (pandas.Series or pandas.DataFrame): The data for the boxplot.
        class_label (str): The label for the class corresponding to the data.
        **kwargs: Arbitrary keyword arguments to pass to seaborn.boxplot.

    Returns:
        None
    """
    sns.boxplot(data=data[class_label], ax=ax,**kwargs)
    ax.set_xlabel(class_label)

def histogram_function(ax, data, class_label,**kwargs):
    """
    Create a histogram on the given subplot axis using the provided DataFrame.

    Parameters:
        ax (matplotlib.axes.Axes): The subplot axis to draw the histogram.
        data (pandas.Series or pandas.DataFrame): The data for the histogram.
        class_label (str): The label for the class corresponding to the data.
        **kwargs: Arbitrary keyword arguments to pass to seaborn.histplot.

    Returns:
        None
    """
    sns.histplot(data=data[class_label], ax=ax,**kwargs)
    ax.set_xlabel(class_label)

def kdeplot_function(ax, data, class_label,**kwargs):
    """
    Create a KDE plot on the given subplot axis using the provided DataFrame.

    Parameters:
        ax (matplotlib.axes.Axes): The subplot axis to draw the KDE plot.
        data (pandas.Series or pandas.DataFrame): The data for the KDE plot.
        class_label (str): The label for the class corresponding to the data.
        **kwargs: Arbitrary keyword arguments to pass to seaborn.kdeplot.

    Returns:
        None
    """
    sns.kdeplot(data=data[class_label], ax=ax,**kwargs)
    ax.set_xlabel(class_label)

def plot_scatter_matrix(df, columns, hue=None, fig_size=(10, 10), **kwargs) -> None:
    """
    Plot a scatter matrix (pairplot) for specified columns of a DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list): A list of column names to include in the scatter matrix.
        hue (str, optional): Column name to use for color encoding in the scatter plot.
        fig_size (tuple, optional): The size of the figure (width, height) in inches.
                                    Default is (10, 8).
        **kwargs: Additional keyword arguments to pass to sns.pairplot().

    Returns:
        None
    """
    
    pairplot = sns.pairplot(df[columns], hue=hue, **kwargs)
    pairplot.fig.set_size_inches(*fig_size)
    plt.show()

def plot_correlation_matrix(df, columns, fig_size=(10, 8), **kwargs) -> None:
    """
    Plot the correlation matrix for specified columns of a DataFrame.

    Parameters:
        df (pandas.DataFrame): The DataFrame containing the data.
        columns (list): A list of column names to include in the correlation matrix.
        fig_size (tuple, optional): The size of the figure (width, height) in inches.
                                    Default is (10, 8).
        **kwargs: Additional keyword arguments to pass to sns.heatmap().

    Returns:
        None
    """
    correlation_matrix = df[columns].corr()

    cmap = kwargs.pop("cmap", "coolwarm")

    plt.figure(figsize=fig_size)
    sns.heatmap(
        correlation_matrix, 
        annot=True, 
        cmap=cmap, 
        fmt=".2f", 
        linewidths=0.5, 
        vmax=1, 
        vmin=-1, 
        **kwargs
    )
    
    plt.title("Correlation Matrix")
    plt.show()

def plot_feature_importance(model, feature_names, figsize=(10, 5)):
    """
    Generate a horizontal bar plot of feature importance for a trained Random Forest model.

    Parameters:
        model (sklearn.ensemble.RandomForestClassifier): Trained Random Forest model.
        feature_names (list): List of feature names corresponding to the model input.
        figsize (tuple, optional): Figure size for the plot. Default is (10, 5).

    Returns:
        None
    """
    importances = model.feature_importances_

    feature_importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
    feature_importance_df = feature_importance_df.sort_values(by='Importance', ascending=False)

    plt.figure(figsize=figsize)
    plt.barh(feature_importance_df['Feature'], feature_importance_df['Importance'])
    plt.xlabel("Importance")
    plt.ylabel("Features")
    plt.title("Feature Importance in Random Forest")
    plt.gca().invert_yaxis()
    plt.show()

def plot_auc_roc(model, X_test, y_test, figsize=(8, 6)):
    """
    Generate an AUC-ROC curve for a trained classifier.

    Parameters:
        model (sklearn classifier): Trained classifier with a `predict_proba` method.
        X_test (numpy.ndarray or pandas.DataFrame): Test set features.
        y_test (numpy.ndarray or pandas.Series): True labels for the test set.
        figsize (tuple, optional): Figure size for the plot. Default is (8, 6).

    Returns:
        None
    """
    y_probs = model.predict_proba(X_test)[:, 1]

    fpr, tpr, _ = roc_curve(y_test, y_probs)
    roc_auc = auc(fpr, tpr)

    plt.figure(figsize=figsize)
    plt.plot(fpr, tpr, color='blue', lw=2, label=f'AUC = {roc_auc:.4f}')
    plt.plot([0, 1], [0, 1], color='gray', linestyle='--', lw=2)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate')
    plt.title('ROC Curve')
    plt.legend(loc='lower right')
    plt.grid(True)
    plt.show()

#------------------------------------------------------------------------------------