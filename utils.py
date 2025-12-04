import pandas as pd

df = pd.read_json(r"week7_pandas\orders_simple.json")


def convert(df): # type: ignore
    df["total_amount"] = df["total_amount"].apply(lambda x: x[0:-1])
    df["total_amount"] = pd.to_numeric(df["total_amount"])
    df["order_date"] = pd.to_datetime(df["order_date"])
    return df

    
def remove_html_sign(df):
    tags_list = ['<br>','</b>']
    for tag in tags_list:
        df["items_html"] = df["items_html"].apply(lambda x: x[3:])
        df["items_html"] = df["items_html"].str.replace(tag, '')
    return df
 



def new_column(df):
    df = df.assign(
        high_value_order=True
        )
    # if df['total_amount'] > df['total_amount'].mean():
    #     df = df.assign(
    #     high_value_order=True
    #     )
    return df


def sort(df):
    """sorting the values by total ammount"""
    df = df.sort_values('total_amount', ascending=False)
    return df


def country_rating(df):
    df = df.assign(
        country_rating=df.groupby('country')['rating'].mean()
    )
    return df

def filter_rows(df):
    df = df[(df['total_amount'] > 1000) & (df['rating'] > 4.5)]
    return df
    

def status(df): 
    """show the delivery status"""
    df = df.assign(
        delivery_status= 'ontime'
    )
    # df["shipping_days"].apply(lambda x = "delaed": x > 7)
    return df


    
