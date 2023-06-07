import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def read_data(file):
    
    df = pd.read_csv(file)
    df = df[['Gender', '11']]
    df.columns = ['gender', 'last_minute']
    
    return df


def calculate_stats(df, label):
    
    df = df[df['gender'] == label]
    val_counts = df['last_minute'].value_counts(normalize=True)
    
    return val_counts


def generate_plot(df):

    df_F = df[df['gender'] == 'F']
    df_M = df[df['gender'] == 'M']
    
    plt.rcParams["figure.figsize"]=(20,4)
    colors=["#E66101","#FDB863","#EEEEEE","#B2ABD2","#5E3C99"]
    sns.set_palette(sns.color_palette(colors))
    response_order=["Strong Disagree","Disagree","Neither","Agree","Strong Agree"]
    
    fig,(ax1, ax2)=plt.subplots(ncols=2,sharex=True,sharey=True)
    sns.countplot(x='last_minute',data=df_F,order = response_order,ax=ax1)
    ax1.set_title('Females',fontsize=14)
    ax1.tick_params(axis='both', which='major', labelsize=12)
    ax1.set_ylabel('Percent of Respondents',fontsize=14)
    ax1.set_xlabel(None)
    sns.countplot(x='last_minute',data=df_M,order=response_order, ax=ax2)
    ax2.set_title('Males',fontsize=14)
    ax2.tick_params(axis='both', which='major', labelsize=12)
    ax2.set_ylabel(None)
    ax2.set_xlabel(None)
    fig.text(0.5,-0.01,'You tend to leave things to the last minute',fontsize=18,ha='center')
    
    return fig


