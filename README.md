# Kidney Disease Analysis with Pandas

Folder Structure:
```
kidney-disease-analysis/
├── data/
│   ├── raw_kidney.csv
│   └── processed/
│
├── scripts/
│   ├── a01_data_import.py
│   ├── a02_data_exploration.py
│   ├── a03_data_indexing.py
│   ├── a04_data_cleaning.py
│   ├── a05_transformation.py
│   ├── a06_groupby.py
│   ├── a07_merging.py
│   ├── a08_pivots.py
│   ├── a09_timeseries.py
│   ├── a10_advanced.py
│   ├── a11_visualization.py
│   ├── a12_ml_prep.py
│   ├── a13_performance.py
│   ├── a14_patterns.py
│   ├── a15_case_studies.py
│   ├── a16_errors.py
│   └── a17_integration.py
│
├── reports/
│   ├── figures/
│   └── analysis_logs/
│
├── .gitignore
├── requirements.txt
├── LICENSE
└── README.md

## Phase 1: Project Setup Complete

✅ Initialized project structure  
✅ Added Python requirements  
✅ Prepared data directory for kidney dataset

Next Phase: Data Import and Basic Exploration

## Phase 2: Data Import Complete

✅ Added a01_data_import.py  
- Demonstrates DataFrame creation  
- Basic CSV I/O operations  
- Sample kidney data generation  

Next Phase: Data Exploration (a02_data_exploration.py)

## Phase 3: Data Exploration Complete

✅ Added a02_data_exploration.py  
- Missing value analysis  
- Data type inspection  
- Statistical summaries  

Next Phase: Data Indexing (a03_data_indexing.py)

## Phase 4: Data Cleaning Complete

✅ Added `a04_data_cleaning.py`  
- Handled missing values in clinical metrics (age, bp, sg)  
- Removed duplicate patient records  
- Fixed data types (e.g., converted `classification` to categorical)  
- Saved cleaned data to `data/processed/cleaned_kidney.csv`  

**Kidney-Specific Notes**:  
- Used median imputation for vitals (robust to outliers in medical data)  
- Preserved nulls in `classification` for realistic ML testing  

Next Phase: Data Transformation (`a05_transformation.py`)  

## Phase 5: Data Transformation Complete

✅ Added `a05_transformation.py`  
- Created age groups (`<30`, `30-45`, `46-60`, `60+`)  
- Normalized blood pressure (z-score)  
- Added sorted indexes for clinical prioritization  

**Kidney-Specific Notes**:  
- Age bins align with CKD risk categories  
- Normalization enables cross-feature comparison  

Next Phase: GroupBy Analysis (`a06_groupby.py`)  

## Phase 6: GroupBy Analysis Complete

✅ Added `a06_groupby.py`  
- Calculated average blood pressure by age group  
- Counted patients by classification within each age group  
- Aggregated multiple metrics (mean, std) for `bgr` and `sc`  
- Applied a custom function to find the glucose range  
- Filtered groups based on a condition (high blood pressure)  

**Kidney-Specific Notes**:  
- Grouping by `age_group` and `classification` reveals how different clinical metrics vary across patient segments.  
- This analysis helps identify high-risk groups, such as older patients with high blood pressure or specific blood glucose patterns.  

Next Phase: Merging DataFrames (`a07_merging.py`)

## Phase 7: Merging DataFrames Complete

✅ Added `a07_merging.py`  
- Created dummy datasets for demographics and lab results to simulate real-world data integration.  
- Performed an **inner join** to combine core kidney data with patient demographics.  
- Used a **left join** to add supplementary lab results, preserving all original patient records.  
- Demonstrated an **outer join** to combine patient lists, ensuring no records were dropped.  
- Saved the primary merged data to `data/processed/merged_kidney_data.csv`.  

**Kidney-Specific Notes**:  
- Merging is crucial for building a holistic patient view. For instance, combining clinical data with demographics (`city`, `gender`) can help identify geographical or gender-based trends in kidney disease.  
- The use of a **left join** for lab results is standard practice to avoid losing patient records from the primary cohort, even if some test results are missing.  

Next Phase: Pivot Tables (`a08_pivots.py`)

## Phase 8: Pivot Tables Complete

✅ Added `a08_pivots.py`  
- Created a basic pivot table to show the average blood pressure, cross-referenced by `age_group` and `classification`.  
- Built an advanced pivot table with multiple aggregation functions (`mean`, `max`) for different clinical metrics (`bgr`, `sc`).  
- Demonstrated the use of `margins` to add row and column totals for a quick overview of patient counts.  
- Saved the resulting pivot tables to a log file for further analysis.  

**Kidney-Specific Notes**:  
- Pivot tables are excellent for summarizing the relationships between different categorical variables. For example, the first pivot table quickly highlights if a certain age group with CKD (`ckd`) has a notably higher average blood pressure.  
- The advanced pivot table helps in identifying complex patterns, such as whether patients in a particular `city` and `age_group` with `ckd` have dangerously high blood glucose (`bgr`) and serum creatinine (`sc`) levels.  

Next Phase: Time Series Analysis (`a09_timeseries.py`)

## Phase 9: Time Series Analysis Complete

✅ Added `a09_timeseries.py`  
- Synthesized a `record_date` column to simulate a real-world time series dataset.  
- Set the date column as the DataFrame index to enable time-based operations.  
- **Resampled** the data to a monthly frequency to aggregate patient counts and average blood pressure.  
- Calculated a 30-day **rolling average** for serum creatinine to smooth out noise and identify trends.  
- Used the **shift** method to compare current blood glucose levels with previous records, highlighting changes over time.  

**Kidney-Specific Notes**:  
- Time series analysis is critical for monitoring disease progression and treatment efficacy. For example, a rising rolling average of serum creatinine could indicate worsening kidney function.  
- Resampling data by month or quarter can help hospital administrators track patient admission rates and allocate resources more effectively.  
- Shifting data allows for direct period-over-period comparisons, which is essential for evaluating patient response to treatment.  

Next Phase: Advanced Pandas Features (`a10_advanced.py`)

## Phase 10: Advanced Pandas Features Complete

✅ Added `a10_advanced.py`  
- Utilized **categorical data types** to improve memory efficiency and enable logical sorting of `age_group` and `classification`.  
- Implemented **multi-level indexing** on `city` and `age_group` to demonstrate hierarchical data access and more complex querying.  
- Used the **`pipe`** method to create a clean, chainable data processing workflow for calculating a new clinical ratio.  
- Demonstrated the **`explode`** function to transform a list-like column (e.g., medications) into separate rows for more granular analysis.  

**Kidney-Specific Notes**:  
- Multi-level indexing is highly effective for analyzing nested data structures, such as patients within specific regions and age brackets.  
- The `pipe` function promotes reproducible and readable code, which is essential for clinical data analysis where transparency and validation are key.  
- Exploding a `medications` column would allow analysts to easily count the frequency of each medication or study the relationship between specific drugs and patient outcomes.  

Next Phase: Data Visualization (`a11_visualization.py`)

## Phase 11: Data Visualization Complete

✅ Added `a11_visualization.py` using Matplotlib and Seaborn.  
- Generated and saved the following plots to `reports/visualizations/`:  
  - **Histogram** of patient age distribution.  
  - **Bar chart** showing the count of patients with and without CKD.  
  - **Box plot** comparing blood pressure distributions between classifications.  
  - **Scatter plot** to visualize the relationship between serum creatinine and blood glucose.  
  - **Correlation heatmap** to show the relationships between all numeric clinical metrics.  

**Kidney-Specific Notes**:  
- The box plot of blood pressure clearly illustrates that patients with CKD tend to have higher and more variable blood pressure.  
- The scatter plot helps in identifying patients with concurrent high blood glucose and high serum creatinine, who may be at the highest risk.  
- The heatmap provides a comprehensive overview of which clinical indicators are correlated, guiding further investigation and feature selection for machine learning models.  

Next Phase: Machine Learning Preparation (`a12_ml_prep.py`)

## Phase 12: Machine Learning Preparation Complete

✅ Added `a12_ml_prep.py`  
- Separated features (X) and target (y).  
- Identified and processed categorical and numerical features separately.  
- Applied **one-hot encoding** to categorical features to convert them into a machine-readable format.  
- Used **StandardScaler** to normalize the numerical features, ensuring that all variables have a similar scale.  
- Created a `ColumnTransformer` to apply the correct preprocessing to each feature type.  
- Saved the fully preprocessed data, ready for model training.  

**Kidney-Specific Notes**:  
- Proper feature scaling is crucial in medical datasets where clinical metrics can have vastly different units and ranges (e.g., age vs. serum creatinine).  
- One-hot encoding is necessary for nominal categorical data like `city` or `gender` so that machine learning algorithms can interpret them correctly.  

Next Phase: Performance Analysis (`a13_performance.py`)  