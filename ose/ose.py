import os.path
import urllib.request
import zipfile
import pandas as pd

def ose(date, maturities, strikes):
    '''Download Options DATA(NK255) from JPX   　
    
    Returns
    -------
    Options : DataFrame(Pandas)
    
    Parameters
    ----------
    date :int 
        #eg: 20190122
    maturities:list
        #eg1(monthly type): [201902]
        #eg2(weekly type): [20190125]
        #eg3: [201902 , 20190125]
    strikes: list
        #eg: [19000,20000]
    
    Examples
    --------
    >>>  ose(
        20190121,
        [201902, 20190125],
        [19000, 20000]
        )
    '''

    if not os.path.isdir('zips'):
        os.mkdir('zips')
        print('mkdir >> zips')

    fname = f'ose{str(date)}tp.zip'
    f_path = f'zips/{fname}'
    if not os.path.isfile(f_path):
        fbase = 'http://www.jpx.co.jp/markets/derivatives/option-price/data/'
        print(f'Download >> {fbase}/{fname} >> {f_path}')
        urllib.request.urlretrieve(f'{fbase}/{fname}', f_path)

    colName = ("CODE", "TYPE", "MATURITY", "STRIKE", "RSV",
               "PUT_CODE", "PUT_PRICE", "PUT_RSV", "PUT", "PUT_VOLATILITY",
               "CALL_CODE", "CALL_PRICE", "CALL_RSV", "CALL", "CALL_VOLATILITY",
               "F225_PRICE", "Base_VOL")

    with zipfile.ZipFile(f_path) as z:
        with z.open(f'ose{str(date)}tp.csv') as f:
            df = pd.read_csv(f, names=colName)

    return df.query("CODE in ['NK225E    ','NK225WE   ']").query(
        f" {strikes[0]} <= STRIKE <= {strikes[1]} ").query(
        f" MATURITY in {maturities}"
    )[['STRIKE', "CALL", "PUT", "MATURITY"]].round().astype(int).set_index('STRIKE')