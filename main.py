import pandas as pd 
import utils


def main():  
    utils.df = utils.convert(utils.df)
    utils.df = utils.remove_html_sign(utils.df)
    utils.df = utils.new_column(utils.df)
    utils.df = utils.sort(utils.df)
    utils.df = utils.country_rating(utils.df)
    utils.df = utils.filter_rows(utils.df)
    df = utils.status(utils.df)

    df.to_csv(r'week7_pandas\orders.csv')
    

if __name__ == "__main__":
    main()
    
    