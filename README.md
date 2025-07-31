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