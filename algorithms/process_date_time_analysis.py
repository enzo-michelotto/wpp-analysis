import pandas as pd
import re
import matplotlib.pyplot as plt

def process_date_time_analysis(file_path, csv_file_path, hour_plot_path, date_plot_path):
    
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.readlines()

    date_time_pattern = r'\[(\d{2}/\d{2}/\d{2}), (\d{2}:\d{2}:\d{2})\]'
    date_time_data = [re.search(date_time_pattern, line) for line in text]
    date_times = [(match.group(1), match.group(2)) for match in date_time_data if match]

    df_date_time = pd.DataFrame(date_times, columns=['Date', 'Time'])

    df_date_time.to_csv(csv_file_path, index=False)
