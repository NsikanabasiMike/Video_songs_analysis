## Table of Contents
- [Installation](#install)
- [Project Motivation](#motivate)
- [File Descriptions](#describe)
- [Licensing, Authors, and Acknowledgements](#acknowledge)

<a id='install'></a>
### Installation
1. Python 3.6 and latest from [here](https://www.python.org/downloads/)
2. Anaconda distribution of Python from [here](https://www.anaconda.com/blog/anaconda-distribution-2022-10#).

<a id='motivate'></a>
# Video Songs Analysis

## Project Motivation

> This is an internship project organised by Mentorness online learning platform. The aim is to conduct a comprehensive analysis of YouTube songs data using Power BI/Tableau. The dataset contains key attributes such as video ID, channel title, title, description, tags, published date, view count, like count, favorite count, comment count, video duration, video definition, and caption details. The goal is to utilize Power BI to create insightful visualizations and reports that provide a deeper understanding of YouTube songs' performance, popularity, and user engagement. The analysis aims to uncover trends, preferences, and patterns in the data to aid content creators and stakeholders in optimizing their YouTube song content.<br>  

The first part is the Extract, Transform, and Load(ETL) process. Here, the dataset is read into a dataframe, then cleaned with pandas, and stored as a csv file.

The second part is the data visualisation. Tableau is used to create an interactive dashboard hosted [here](https://public.tableau.com/app/profile/nsikanabasi.essiet1825/viz/Mentorness_song_analysis/mentorness_somg_analysis_dashboard). Matplotlib is used for a quick exploratory analysis. <br>

<a id='describe'></a>
### File Descriptions
There are two files: visuals.py and Mentorness_youtube_songs_project.ipynb<br>
__visuals.py__ is a python module that contains the code for Matplotlib visualisation.
__Mentorness_youtube_songs_project.ipynb__ contains the ETL codes.

<a id='acknowledge'></a>
### Licensing, Authors, Acknowledgements
The data used is from Mentorness. online tranining platform and is strictly for interns.