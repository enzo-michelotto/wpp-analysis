import pandas as pd
import matplotlib.pyplot as plt

def plot_from_csv(csv_file_path, hour_plot_path, date_plot_path, weekday_plot_path):

    df = pd.read_csv(csv_file_path)

    df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%y') 

    if 'Hour' not in df.columns:
        df['Hour'] = pd.to_datetime(df['Time'], format='%H:%M:%S').dt.hour

    df['DayOfWeek'] = df['Date'].dt.dayofweek

    day_name_map = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday', 
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }
    df['DayName'] = df['DayOfWeek'].map(day_name_map)

    hour_counts = df['Hour'].value_counts().sort_index()
    plt.figure(figsize=(10, 6))
    plt.bar(hour_counts.index, hour_counts.values, color='skyblue')
    plt.title('Messages by Hour of Day', fontsize=16)
    plt.xlabel('Hour of Day', fontsize=12)
    plt.ylabel('Number of Messages', fontsize=12)
    plt.xticks(range(0, 24))
    plt.grid(axis='y')
    plt.savefig(hour_plot_path)
    plt.show()

    date_counts = df['Date'].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    plt.plot(date_counts.index, date_counts.values, marker='o', color='orange')
    plt.title('Messages per Date', fontsize=16)
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Messages', fontsize=12)
    plt.xticks(rotation=45)
    plt.grid()
    plt.savefig(date_plot_path)
    plt.show()

    weekday_counts = df['DayName'].value_counts()
    weekday_counts = weekday_counts.reindex(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])  # Ensure correct order
    plt.figure(figsize=(10, 6))
    plt.bar(weekday_counts.index, weekday_counts.values, color='lightgreen')
    plt.title('Messages by Day of the Week', fontsize=16)
    plt.xlabel('Day of the Week', fontsize=12)
    plt.ylabel('Number of Messages', fontsize=12)
    plt.grid(axis='y')
    plt.savefig(weekday_plot_path)
    plt.show()

    print(f"Graphs saved as '{hour_plot_path}', '{date_plot_path}', and '{weekday_plot_path}'.")

csv_file_path = 'csv/date_time_data.csv'
hour_plot_path = 'messages_by_hour.png'
date_plot_path = 'messages_per_date.png'
weekday_plot_path = 'messages_by_weekday.png'

plot_from_csv(csv_file_path, hour_plot_path, date_plot_path, weekday_plot_path)
