import pandas as pd
import datetime as dt 

df = pd.read_csv('groupby-data/airqual.csv',
        parse_dates =[['Date','Time']],
        na_values = [-200],
        usecols=["Date", "Time", "CO(GT)", "T", "RH", "AH"]
       ).rename(
               columns={
        "CO(GT)": "co",
        "Date_Time": "tstamp",
        "T": "temp_c",
        "RH": "rel_hum",
        "AH": "abs_hum",
            }
    ).set_index('tstamp')


day_names = df.index.day_name()

hour = df.index.hour

df_by_days_hr =  df.groupby([day_names,hour])['co'].mean().rename_axis(['days','hr'])

bins = pd.cut(df['temp_c'], bins = 3, labels = ('cool','warm','hot'))
df_by_bins = df[["rel_hum", "abs_hum"]].groupby(bins).agg(['mean','median'])

print(df_by_bins)

def parse_millisecond_timestamp(ts: int) -> dt.datetime:
    """Convert ms since Unix epoch to UTC datetime instance."""
    return dt.datetime.fromtimestamp(ts / 1000, tz=dt.timezone.utc)

dtype={
        "outlet": "category",
        "category": "category",
        "cluster": "category",
        "host": "category",
    }


df = pd.read_csv('groupby-data/news.csv',
        dtype = dtype,
        sep = '\t',
        names=["title", "url", "outlet", "category", "cluster", "host", "tstamp"],
        index_col = 0,
        parse_dates = ['tstamp'],
        date_parser = parse_millisecond_timestamp,
        )


title, ser = next(iter(df.groupby("outlet", sort=False)["title"]))

#df_title_cont_fed_largest = df.groupby("outlet", sort=False)["title"].apply(lambda ser: ser.str.contains("Fed").sum()).nlargest(10)
#df_title_cont_fed = df.groupby("outlet", sort=False)["title"].apply(lambda ser: ser.str.contains("Fed").sum())
#print(df_title_cont_fed_largest)

mentions_fed = df["title"].str.contains("Fed")
print(mentions_fed.groupby(df['outlet'],sort = False).sum().nlargest(10))


