import pandas as pd
# Libraries import
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Display inline matplotlib plots with IPython
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

# Read cleaned data
clean_song_df = pd.read_csv('clean_song_df.csv')
# Convert published_At to datetime
clean_song_df.publishedAt = pd.to_datetime(clean_song_df.publishedAt)

# Visualisation

def metrics_relationship_scatter_plot():
    
    """
    Visualise metrics relationship.
    
    Attributes: 
            None
    Output: 
        Scatter plot show casing a positive relationship between metrics
    """
    
    plt.figure(figsize= (13, 6))
    plt.scatter(clean_song_df.likeCount, clean_song_df.viewCount, c = clean_song_df.commentCount, cmap= 'viridis_r');
    xticks = ([0.0, 2000000, 4000000, 6000000, 8000000, 10000000, 12000000]);
    plt.xticks(xticks, labels=['0', '2m', '4m', '6m', '8m', '10m', '12m']);
    yticks = ([0.0, 200000000, 400000000, 600000000, 800000000, 1000000000, 1200000000, 1400000000, 1600000000]);
    plt.yticks(yticks, labels=['0', '200m', '400m', '600m', '800m', '1b', '1.2b', '1.4b', '1.6b']);
    plt.xlabel('like count');
    plt.ylabel('view count');
    plt.colorbar(label = 'comment count values', );
    plt.title('Relationship between video metrics');


def definition_bar_plot():
    """
    Visualise Influence of definition on median engagement metrics.
    
    Attributes: 
            None
    Output: 
        Bar plot showing definition types and median counts
    """
    
    definition_median_metrics = clean_song_df.groupby('definition')[['viewCount', 'likeCount', 'commentCount']].median()
    definition_median_metrics.plot(kind  = 'bar', figsize = [12, 5]);
    ticks = ([0, 100000, 200000, 300000, 400000])
    plt.yticks(ticks, labels=['0', '100k', '200k', '300k', '400k']);
    plt.ylabel('Video song count');
    plt.title('Influence of video definitions on median video metrics');


def video_published_time_by_count_plot():
    
    """
    Visualise Peak video upload/publishing times.
    
    Attributes: 
            None
    Output: 
        Bar plot showing counts of video publishing times.
    """
    clean_song_df.publishedAt.dt.hour.value_counts().plot(kind = 'bar', figsize=(12, 5));
    plt.xlabel('hours');
    plt.ylabel('Video song count');
    plt.title('Peak videos upload time');


def video_publishing_time_by_median_metrics_plot():
    
    """
    Visualise Peak video publishing times and influence on median metrics.
    
    Attributes: 
            None
    Output: 
        Bar plot showing video publishing times and their median metrics.
    """
    time_and_median_metrics = clean_song_df.groupby(
        clean_song_df.publishedAt.dt.hour)[['viewCount', 
           'likeCount', 
           'commentCount']].median().sort_values('viewCount', ascending=False)
    time_and_median_metrics.plot(kind = 'bar', figsize=(20, 10), fontsize = '20', width = .7);
    ticks = ([0, 200000, 400000, 600000, 800000, 1000000, 1200000, 1400000]);
    plt.yticks(ticks, labels=['0', '200k', '400k', '600k', '800k', '1m', '1.2m', '1.4m']);
    plt.xlabel('Published At', fontsize = 20);
    plt.ylabel('Median metrics count', fontsize = 20);
    plt.legend(fontsize = 20);
    plt.title('Influence of video publishing times on metrics', fontsize = 20);


def songs_over_time_plot():
    
    """
    Visualise Video song metrics over time.
    
    Attributes: 
            None
    Output: 
        Line plot showing median song metrics over time.
    """
    year_and_median_metrics = clean_song_df.groupby(clean_song_df.publishedAt.dt.year)[[
        'viewCount', 
        'likeCount', 
        'commentCount']].median()
    year_and_median_metrics.plot(kind = 'line', figsize = [10, 5]);
    plt.ylabel('Median metric value');
    ticks = ([0, 250000, 500000, 750000, 1000000, 1250000, 1500000])
    plt.yticks(ticks, labels=['0', '250k', '500k', '750k', '1m', '1.25m', '1.50m']);
    plt.title('Song video metrics over time (years)');


def top_ten_video_tags_count_plot():
    
    """
    Visualise Top 10 popular video tags by count.
    
    Attributes: 
            None
    Output: 
        Bar plot showing counts of top 10 popular video tags.
    """
    clean_song_df.tags.value_counts()[:10].plot(kind = 'bar', figsize = (13, 8));
    plt.xlabel('Video songs')
    plt.ylabel('Video song count');
    plt.title('Top ten popular tags');
    plt.title('Top ten popular video song tags by count');


def top_ten_video_tags_median():
    
    """
    Visualise Top 10 tags by median viewCounts.
    
    Attributes: 
            None
    Output: 
        Bar plot showing top 10 popular video tags by median views.
    """
    tags_by_median_viewcount = clean_song_df.groupby('tags')[[
        'viewCount'
    ]].median().sort_values('viewCount', ascending = False)[:10]
    tags_by_median_viewcount.plot(kind = 'bar', figsize = [10, 5]);
    yticks = ([0, 200000000, 400000000, 600000000, 800000000, 1000000000, 1200000000, 1400000000]);
    plt.yticks(yticks, labels=['0', '200m', '400m', '600m', '800m', '1b', '1.2b', '1.4b']);
    plt.xlabel('Video songs');
    plt.ylabel('Median view Count');
    plt.title('Top 10 tags by median viewCount');


if __name__ == '__main__':
    metrics_relationship_scatter_plot()
    definition_bar_plot()
    video_published_time_by_count_plot()
    video_publishing_time_by_median_metrics_plot()
    songs_over_time_plot()
    top_ten_video_tags_count_plot()
    top_ten_video_tags_median()