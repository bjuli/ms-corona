import pandas as pd
import locale


def cast_date_column(df: pd.DataFrame) -> pd.DataFrame:
    locale.setlocale(locale.LC_ALL, 'de_DE')  # assumes locale DE is available on system, check with locale -a
    return df.assign(datum=lambda df: pd.to_datetime(df['datum'].str.strip(" ") + " 2020", format='%d. %B %Y'))
