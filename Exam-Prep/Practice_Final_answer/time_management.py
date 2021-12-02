import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_data(file):
    """Reads CSV file in, extracts gender and last minute column, renames columns

    Parameters
    ----------
    file : CSV
        path to CSV file to be read in

    Returns
    -------
    df : DataFrame
        pandas DataFrame with two columns: gender and last_minute
    """
    
    df = pd.read_csv(file)
    df = df[['Gender', '11']] # '11' is column that contains last_minute data
    df.columns = ['gender', 'last_minute']
    
    return df

def calculate_stats(df, label):
    """Calculates breakdown of last_minute within gender

    Parameters
    ----------
    df : DataFrame
        dataframe on which to calculate breakdown of last_minute
    label : str
        gender label ('M' or 'F')

    Returns
    -------
    val_counts : value_counts
        value_counts object with proportion of responses in last_minute

    """
    df = df[df['gender'] == label]
    # normalize to produce proportions rather than counts
    val_counts = df['last_minute'].value_counts(normalize=True)  
    
    return val_counts

def generate_plot(df):
    """generate barplots that summarize last_minute for each gender

    Parameters
    ----------
    df : DataFrame
        pandas Dataframe containing data to be summarized

    Returns
    -------
    fig : plt.Figure
        matplotlib figure containing summary of last_minute across genders

    """
    df_F = df[df['gender'] == 'F']
    df_M = df[df['gender'] == 'M']

    # specify parameters for use in figure
    plt.rcParams["figure.figsize"]=(20,4)
    colors=["#E66101","#FDB863","#EEEEEE","#B2ABD2","#5E3C99"]
    sns.set_palette(sns.color_palette(colors))
    
    response_order=["Strong Disagree","Disagree","Neither","Agree","Strong Agree"]
    
    # generate figure; allowing space for 2 plots 
    fig,(ax1, ax2)=plt.subplots(ncols=2,sharex=True,sharey=True)
    # female plot
    sns.countplot(x='last_minute',data=df_F,order = response_order,ax=ax1)
    ax1.set_title('Females',fontsize=14)
    ax1.tick_params(axis='both', which='major', labelsize=12)
    ax1.set_ylabel('Percent of Respondents',fontsize=14)
    ax1.set_xlabel(None)
    # male plot
    sns.countplot(x='last_minute',data=df_M,order=response_order, ax=ax2)
    ax2.set_title('Males',fontsize=14)
    ax2.tick_params(axis='both', which='major', labelsize=12)
    ax2.set_ylabel(None)
    ax2.set_xlabel(None)
    fig.text(0.5,-0.01,'You tend to leave things to the last minute',fontsize=18,ha='center')
    
    return fig