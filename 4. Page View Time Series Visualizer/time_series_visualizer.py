import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=True)
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
mask = (df['value'] >= df['value'].quantile(0.025)) \
    & (df['value'] <= df['value'].quantile(0.975))

df = df.loc[mask]


def draw_line_plot():
    fig = df.plot(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019',
              xlabel='Date', ylabel='Page Views', figsize=(20,8)).get_figure()

    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = None
    df_bar = df.resample('M').mean()
    df_bar['Year'] = df_bar.index.year
    df_bar['Month'] = df_bar.index.month

    df_bar = df_bar.pivot_table(index='Year', columns='Month', values='value',)
    #month_name is needed, but after pivoting, the order is changed so 
    df_bar.rename(columns={1:'January',2:'February',3:'March',4:'April',5:'May',
                            6:'June',7:'July',8:'August',9:'September',10:'October',
                            11:'November',12:'December'}, inplace=True)
    # Draw bar plot

    fig, ax = plt.subplots(figsize=(12, 8))
    df_bar.plot.bar(ax=ax)

    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    fig.savefig('bar_plot.png')

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]
    months = {
        'Jan': 0,
        'Feb': 1,
        'Mar': 2,
        'Apr': 3,
        'May': 4,
        'Jun': 5,
        'Jul': 6,
        'Aug': 7,
        'Sep': 8,
        'Oct': 9,
        'Nov': 10,
        'Dec': 11,
    }
    df_box.sort_values('month', key = lambda x : x.apply (lambda x : months[x]), inplace=True)
    fig, ax = plt.subplots(1, 2, figsize=(20, 10))
    
    sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1])
    ax[0].set_xlabel('Year')
    ax[1].set_xlabel('Month')
    ax[0].set_ylabel('Page Views')
    ax[1].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    fig.savefig('box_plot.png')
    return fig
