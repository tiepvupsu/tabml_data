import pandas as pd
from pandas_profiling import ProfileReport

def profile(input_file, output_html):
    train_df = pd.read_csv(input_file)
    prof = ProfileReport(train_df)
    prof.to_file(output_file=output_html)


profile("train.csv", "train.html")
profile("test.csv", "test.html")
