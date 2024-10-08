import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
df['overweight']=(df['weight']/(df['height']/100)**2>25).astype(int)

# 3
df['cholesterol'] = (df['cholesterol']>1).astype(int)
df['gluc'] = (df['gluc']>1).astype(int)

# 4
def draw_cat_plot():
    #5, 6 and 7
    df_cat = pd.melt(df, id_vars=['cardio'],
                     value_vars=['active','alco','cholesterol','gluc','overweight','smoke'])
    df_cat_plot = sns.catplot(data=df_cat,x='variable', hue='value', col='cardio', kind='count')
    df_cat_plot.set_axis_labels('variable', 'total')
    #8
    fig = df_cat_plot.figure
    #9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    mask = (df['ap_lo'] <= df['ap_hi']) \
        & (df['height'] >= df['height'].quantile(0.025)) \
    & (df['height'] <= df['height'].quantile(0.975)) \
    &  (df['weight'] >= df['weight'].quantile(0.025)) \
    &  (df['weight'] <= df['weight'].quantile(0.975)) 
    df_heat = df.loc[mask]

    # 12
    corr = df_heat.corr()
    
    #13
    mask = np.triu(np.ones_like(corr, dtype=bool))

    #14
    fig, ax = plt.subplots()

    #15
    sns.heatmap(corr,annot=True, mask=mask, fmt='.1f')

    # 16
    fig.savefig('heatmap.png')
    return fig
