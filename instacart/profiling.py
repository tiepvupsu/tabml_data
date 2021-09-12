import pandas as pd
from pandas_profiling import ProfileReport

def profile(input_file):
    output_html = input_file + ".html"
    train_df = pd.read_csv(input_file)
    prof = ProfileReport(train_df)
    prof.to_file(output_file=output_html)


profile("aisles.csv")
profile("departments.csv")
profile("order_products__prior.csv")
profile("order_products__train.csv")
profile("orders.csv")
profile("products.csv")
