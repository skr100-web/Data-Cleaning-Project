import pandas as pd
import numpy as np
import os

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        self.df = df.copy()
        self.original = df.copy()

    def profile_data(self):
        print("Data Overview:")
        print(self.df.info())
        print("\nSummary Statistics:")
        print(self.df.describe(include='all'))

    def remove_duplicates(self):
        before = len(self.df)
        self.df = self.df.drop_duplicates()
        after = len(self.df)
        print(f"Removed {before - after} duplicate rows.")

    def handle_missing(self, strategy='drop', fill_value=None):
        if strategy == 'drop':
            self.df = self.df.dropna()
        elif strategy == 'fill':
            self.df = self.df.fillna(fill_value)
        print(f"Missing values handled using '{strategy}' strategy.")

    def standardize_text(self):
        object_cols = self.df.select_dtypes(include='object').columns
        for col in object_cols:
            self.df[col] = self.df[col].astype(str).str.strip().str.lower()
        print(f"Standardized text columns: {list(object_cols)}")

    def remove_outliers_iqr(self):
        numeric_cols = self.df.select_dtypes(include='number').columns
        for col in numeric_cols:
            Q1 = self.df[col].quantile(0.25)
            Q3 = self.df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower = Q1 - 1.5 * IQR
            upper = Q3 + 1.5 * IQR
            before = len(self.df)
            self.df = self.df[(self.df[col] >= lower) & (self.df[col] <= upper)]
            after = len(self.df)
            print(f"Removed {before - after} outliers from '{col}' using IQR method")

    def convert_dates(self):
        for col in self.df.columns:
            if "date" in col.lower():
                self.df[col] = pd.to_datetime(self.df[col], errors='coerce')
        print("Converted date columns to datetime format.")

    def feature_engineering(self):
        if "last_review" in self.df.columns and pd.api.types.is_datetime64_any_dtype(self.df["last_review"]):
            self.df["review_year"] = self.df["last_review"].dt.year
            self.df["review_month"] = self.df["last_review"].dt.month
        else:
            print("Skipping feature engineering: 'last_review' is not datetime.")
        print("Feature engineering completed.")

    def evaluate_changes(self):
        nulls_before = self.original.isnull().mean()
        nulls_after = self.df.isnull().mean()
        std_before = self.original.std(numeric_only=True)
        std_after = self.df.std(numeric_only=True)

        eval_df = pd.DataFrame({
            "Null % Before": nulls_before,
            "Null % After": nulls_after,
            "Std Dev Before": std_before,
            "Std Dev After": std_after
        })

        print("Evaluation Summary:")
        print(eval_df)

    def clean(self):
        return self.df

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        self.df.to_csv(path, index=False)
        print(f"Saved cleaned data to: {path}")

if __name__ == "__main__":
    raw_path = r"C:\Users\prabh\OneDrive\Documents\nyc_airbnb_project\Data\AB_NYC_2019.csv"
    df = pd.read_csv(raw_path)

    backup_path = r"C:\Users\prabh\OneDrive\Documents\nyc_airbnb_project\output\raw_backup.csv"
    clean_path = r"C:\Users\prabh\OneDrive\Documents\nyc_airbnb_project\output\cleaned_AB_NYC_2019.csv"

    os.makedirs(os.path.dirname(backup_path), exist_ok=True)
    df.to_csv(backup_path, index=False)  

    cleaner = DataCleaner(df)
    cleaner.profile_data()

    cleaner.remove_duplicates()
    cleaner.handle_missing(strategy='fill', fill_value=0)
    cleaner.standardize_text()
    cleaner.remove_outliers_iqr()
    cleaner.convert_dates()
    cleaner.feature_engineering()
    cleaner.evaluate_changes()

    cleaned_df = cleaner.clean()
    cleaner.save(clean_path)
