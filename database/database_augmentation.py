from pathlib import Path
import pandas as pd
import os


CURRENT_DIR = Path(os.getcwd())
GENRE_DIR = Path(os.getcwd(), "Genre")

def get_csv_files():
    return [Path(GENRE_DIR, file) for file in os.listdir(GENRE_DIR) if Path(file).suffix == ".csv"]


def process_and_select_top_100(file_path):
    df = pd.read_csv(file_path, dtype={'votes': 'str', 'gross_income': 'str'})
    columns_to_drop = ['gross_income']
    df.drop(columns=columns_to_drop, inplace=True)
    df['votes'] = df['votes'].str.replace(',', '').astype(float)
    df.sort_values(by='votes', ascending=False, inplace=True)
    top_100 = df.head(100)

    top_100['rating_scaled'] = (5 * top_100['rating'] / 11).round(2)
    top_100.drop(columns=['rating'], inplace=True)
    return top_100


def setup_movie_database():
    csv_files = get_csv_files()
    combined_data = pd.DataFrame()
    for file in csv_files:
        top_100_df = process_and_select_top_100(Path(file))
        combined_data = pd.concat([combined_data, top_100_df], ignore_index=True)
    combined_data.to_csv('combined_data.csv', index=False)


if __name__ == "__main__":
    setup_movie_database()
