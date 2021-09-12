import pandas as pd
from pandas_profiling import ProfileReport

def profile(input_file):
    output_html = input_file + ".html"
    train_df = pd.read_csv(input_file)
    prof = ProfileReport(train_df)
    prof.to_file(output_file=output_html)


profile("items.csv")
profile("sales_train.csv")
profile("item_categories.csv")
profile("shops.csv")
