import pandas as pd

def sort_csv_by_frequency(input_csv_path, output_csv_path):

    df = pd.read_csv(input_csv_path)

    df.sort_values(by='Frequency', ascending=False, inplace=True)

    df.to_csv(output_csv_path, index=False)

    return df
