# Election Modeling

I have done several ad hoc models for specific elections and intend to:
- make code accessible as modules (code was in Jupyter notebooks)
- want to pull together my work into a more generalized form
- systematically track different methodologies
- keep "data wrangling" code separate from model code when possible
  
This project will use the pipenv (great tool) from: 
    [http://github.com/hemmendinger/analysistools]


## Election model: emodel.py

Uses Pandas.Dataframe as its main datastructure.

Data wrangling operations that are "editorial" in nature are included.
By editorial I mean, an operation that reflects some subjective decision
or assumption that could affect the model's performance.

## Goals
- Make it easy to add, remove, and change model features
- Make models easily reproducible
- Adequate performance for tens of thousands of polls


## Caution
Watch for bugs due to ordering of dates, currently assuming ascending,
but will attempt to avoid this problem.
