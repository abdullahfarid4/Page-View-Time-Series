import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv')
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Clean data
value25 = df['value'].quantile(0.025)
value975 = df['value'].quantile(0.975)
df = df[df['value'] >= value25]
df = df[df['value'] <= value975]


def draw_line_plot():
    # Draw line plot

    fig, ax = plt.subplots(figsize=(50, 7))
    plt.plot(df.index, df['value'])
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xlabel("Date")
    plt.ylabel("Page Views")

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig


def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month'] = pd.DatetimeIndex(df_bar.index).month
    df_bar_month = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Draw bar plot
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    fig = df_bar_month.plot.bar()
    fig.legend(months, title='Months', prop={'size': 7.75})
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.tight_layout()

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig


def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols=2, figsize=(15, 5))
    sns.catplot(x='year', y='value', kind='box', data=df_box).set(title='Year-wise Box Plot (Trend)');
    sns.catplot(x='month', y='value', kind='box', data=df_box).set(title='Month-wise Box Plot (Seasonality)');

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
