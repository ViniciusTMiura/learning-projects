import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def barplot_column(df, column, legend=True):
    ax = sns.barplot(data=df, x=column, y="count", hue=column, palette="hls")

    if legend:
        # Legend
        ax.legend(title="Category")
            # Personalize the legend
        legendas = [f"{i+1} - {cat}" for i, cat in enumerate(df[column])]
        plt.legend(legendas, title=column, bbox_to_anchor=(1.05, 1), loc='upper left')

        # Substitute x-axis labels with numbers
        ax.set_xticks(np.arange(len(df[column].unique())))
        ax.set_xticklabels(np.arange(1, len(df[column].unique())+1))

    # plt.tight_layout()
    for container in ax.containers:
        ax.bar_label(container)
    plt.show()