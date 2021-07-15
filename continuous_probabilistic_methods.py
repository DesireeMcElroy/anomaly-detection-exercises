import pandas as pd
import numpy as np


# -------------------------------------------------------------------------------------

def get_lower_and_upper_bounds(df, k=1.5):
    '''
    calculates the lower and upper bound to locate outliers and displays them
    note: recommended k be 1.5
    '''
    for i in df.columns:
        if df[i].dtypes != 'object':
            quartile1, quartile3 = np.percentile(df[i], [25,75])
            IQR_value = quartile3 - quartile1
            lower_bound = (quartile1 - (k * IQR_value))
            upper_bound = (quartile3 + (k * IQR_value))
            print(f'For {i} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
    else:
        print('')

# -------------------------------------------------------------------------------------

def visualize_get_lower_and_upper_bounds(df, k=1.5):
    '''
    calculates the lower and upper bound to locate outliers and displays them
    note: recommended k be 1.5
    '''
    for i in df.columns:
        if df[i].dtypes != 'object':
            quartile1, quartile3 = np.percentile(df[i], [25,75])
            IQR_value = quartile3 - quartile1
            lower_bound = (quartile1 - (k * IQR_value))
            upper_bound = (quartile3 + (k * IQR_value))
            print(f'For {i} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
            
            # get those visualizations going
            plt.figure(figsize=(16,4))
            plt.subplot(1, 2, 1)
            sns.histplot(data = df, x = df[i], kde=True)
            plt.title(i)
            plt.subplot(1, 2, 2)
            sns.boxplot(x=df[i], data=df, whis=k)
            plt.title(i)
            plt.show()
    else:
        print('')

# -------------------------------------------------------------------------------------

def get_low_and_up_bounds_df(df, k=1.5):
    '''
    This function takes in a pandas dataframe, list of columns, and k value, and will print out upper and lower bounds for each column.
    It takes in a default argument of the col_list being all numeric columns, and the k value=1.5
    '''
    col_list=list(df.select_dtypes(include=['int', 'float'], exclude='O'))
    for col in col_list:
        # Find the lower and upper quartiles
        q_25, q_75 = df[col].quantile([0.25, 0.75])
        # Find the Inner Quartile Range
        q_iqr = q_75 - q_25
        # Find the Upper Bound
        q_upper = q_75 + (k * q_iqr)
        # Find the Lower Bound
        q_lower = q_25 - (k * q_iqr)
        # Identify outliers
        outliers_lower = df[df[col] < q_lower]
        outliers_upper = df[df[col] > q_upper]
        outliers_all = pd.concat([outliers_lower, outliers_upper], axis=0)
        print('')
        print(col)
        print(f'K: {k}')
        print(f'Lower Fence: {q_lower}')
        print(f'Upper Fence: {q_upper}')
        print('')
        print(f'Lower Outliers in {col}')
        print('')
        print(outliers_lower)
        print('')
        print(f'Upper Outliers in {col}')
        print('')
        print(outliers_upper)
        print('')
        print(f'All Outliers in {col}')
        print('')
        print(outliers_all)
        plt.figure(figsize=(16,4))
        plt.subplot(1, 2, 1)
        sns.histplot(data = df, x = col, kde=True)
        plt.title(col)
        plt.subplot(1, 2, 2)
        sns.boxplot(x=col, data=df)
        plt.title(col)
        plt.show()
        print('-------------------------------------------------------------------')


# -------------------------------------------------------------------------------------


def distplot(df, column):
    '''
    This functions takes in a dataframe and the columns to plot. It then weeds out any string columns and plots the
    distribution of numerical columns
    '''
    for i in column:
        if df[i].dtypes != 'object':
            sns.distplot(df[i])
            plt.xticks(fontsize= 12)
            plt.yticks(fontsize=12)
            plt.ylabel("Count", fontsize= 13, fontweight="bold")
            plt.xlabel(i, fontsize=13, fontweight="bold")
            plt.title('Distribution of '+i)
            plt.show()
    
    else:
        print('')

# -------------------------------------------------------------------------------------


def hist(df):
    '''
    This function takes in a dataframe and columns and creates a histogram with each column
    '''
    for col in df.columns:
        plt.hist(df[col])
        plt.title(f"{col} distribution")
        plt.show()




# -------------------------------------------------------------------------------------

# my original remove outliers function
def remove_outliers(df, k=1.5):
    '''
    calculates the lower and upper bound to locate outliers in variables and then removes them.
    note: recommended k be 1.5 and entered as integer
    '''
    for i in df.columns:
        if df[i].dtypes != 'object':
            quartile1, quartile3 = np.percentile(df[i], [25,75])
            IQR_value = quartile3 - quartile1
            lower_bound = (quartile1 - (k * IQR_value))
            upper_bound = (quartile3 + (k * IQR_value))
            print(f'For {i} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
    
            df = df[(df[i] <= upper_bound) & (df[i] >= lower_bound)]
            print('-----------------')
            print('Dataframe now has ', df.shape[0], 'rows and ', df.shape[1], 'columns')

    else:
        print('')

    return df