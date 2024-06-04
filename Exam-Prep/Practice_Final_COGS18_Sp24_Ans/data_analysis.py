import pandas as pd
import matplotlib.pyplot as plt

def generate_plot(counts):
    """Plots counts by gender.
    
    Parameters
    ----------
    counts : tuple
        Counts to be plotted
        
    Returns
    -------
    fig : matplotlib.figure.Figure
        Plot to be generated
    """ 
    
    plt.rcParams["figure.figsize"] = (10,4)
    fig = plt.figure()

    # generate bar plot for female and male counts
    # customizing bar color, y-axis label and title
    plt.bar(x=("female", "male"), 
            height = counts,
            color = ["#c6656c", "#36525e"])
    plt.ylabel('Count')
    plt.title('Number of females vs male centenarians (1900-1999)')
    
    return fig

def read_data(file):
    """Reads dataset in, filters to only include those deceased whose birth year 
    is between 1900 and 1999 (inclusive).
    
    Parameters
    ----------
    file : path to file
       dataset to be read in
        
    Returns
    -------
    df : pandas.DataFrame
        Filtered dataset
    """     
    
    df = pd.read_csv(file)

    # filter to include only the data we're interested in
    df = df[df['still_alive'] == 'deceased']
    df['birth_year'] = df['birth_date'].str.extract('(^\d\d\d\d)').astype(int)
    df = df[df['birth_year'].between(1900,1999)]

    return df

def calculate_stats(df):
    """Calculates the number of males and females in the dataset.
    
    Parameters
    ----------
    df : pandas.DataFrame
       Dataset to calculate gender breakdown from; requires 'gender' column
        
    Returns
    -------
    num_female : int
        number of females in df
    num_male : int
         number of males in df
    """       
    
    gender_counts = df['gender'].value_counts()  

    # Extract the count, defaulting to 0 if not found
    num_female = gender_counts.get('female', 0)  
    num_male = gender_counts.get('male', 0)  
    
    return num_female, num_male