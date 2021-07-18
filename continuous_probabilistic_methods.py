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
            print('------------------------------------------------------')
            print(f'For {i} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
            outliers_lower = df[df[i] < lower_bound]
            outliers_upper = df[df[i] > upper_bound]
            outliers = pd.concat([outliers_lower, outliers_upper], axis=0)
            print('')
            print(outliers,'\n')
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
            print('------------------------------------------------------------------------------')
            print(f'For {i} the lower bound is {lower_bound} and  upper bound is {upper_bound}')
            outliers_lower = df[df[i] < lower_bound]
            outliers_upper = df[df[i] > upper_bound]
            outliers = pd.concat([outliers_lower, outliers_upper], axis=0)
            print('')
            print(outliers,'\n')
            
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

# create a function
def sigma_outliers(df, sigma=2):
    '''
    This function takes in a dataframe and a sigma value and return outliers based off the parameters
    '''

    for i in df.columns:
        
        if df[i].dtypes != 'object':

            print(df[pd.Series(stats.zscore(df[i])).abs()>sigma].sort_values(by=i))
            print('----------------------------------------')



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