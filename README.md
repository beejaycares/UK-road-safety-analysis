About Dataset

Context

The UK government collects and publishes (usually on an annual basis) detailed information about traffic accidents across the country. This information includes but not limited to geographical locations, weather conditions, type of vehicles, number of casualties, and vehicle manoeuvres, making this a very interesting and comprehensive dataset for analysis and research.
This dataset was sourced from Kaggle website, a popular platform for contemporary data enthusiasts to share their codes, discoveries from data analyses, new projects, and machine learning competitions.
Moreover, the original source of the data is Open Data website of the UK government, where they have been published by the Department of Transport.

The dataset comprises of two csv files:
•	Accident_Information.csv: every line in the file represents a unique traffic accident (identified by the Accident_Index column), featuring various properties related to the accident as columns. Date range: 2005-2017
•	Vehicle_Information.csv: every line in the file represents the involvement of a unique vehicle in a unique traffic accident, featuring various vehicle and passenger properties as columns. Date range: 2004-2016

The two above-mentioned files/datasets were linked using the unique traffic accident identifier (Accident_Index column).
This enables me to analyse occurrences of accidents between 2005 and 2016. Consequently, the joined dataset produces over 2 million observations.
This rendered the use of Microsoft Excel useless as it is a Big Data that exceeds the capacity of Microsoft Excel. More so, the adoption of MySQL would have been most appropriate for this pre-analysis stage of this work, however, it occurs that uploading a dataset comprising millions of observations is extremely difficult on MySQL as the upload seems will be completed when pigs fly. 
Therefore, I resorted to using Python which did not only enable me load the two data sets but also facilitates smooth and efficient exploration of the data sets. 
The linked data sets could have been uploaded here for download but the size is quite enormous and larger than the 25mb restriction. However, the dataset is available upon request.

The four files in this repository are 
UK_road_accident.py (python file version)
UK_road_accident.ipynb (Jupyter Notebook file version)
Road_safety_analysis.twb (This a tableau workbook file containing the visualisations and dashboards for easy comprehension of the UK road accidents between 2005 and 2016)
Dashboard.pdf (This contains the three dashboards created from the linked data set but presented in pdf format for easy access on any device)
Cheers Mate!

I hope this helps.
