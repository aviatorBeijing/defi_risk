import requests
import json,datetime
import pandas as pd
from cmc.cmc_config import DATA_FILE_SYMBOL_LISTING,CMC_KEY_FILE

def ignore(d):
    for k in ['slug','name','id','date_added','platform','total_supply']:
        _ = d.pop(k)

def symbol_lst_from_cache():
    df = pd.read_csv(DATA_FILE_SYMBOL_LISTING, index_col='cmc_rank')
    return df
        
def symbol_lst():
    
    try:
        df = symbol_lst_from_cache()
        return df
    except FileNotFoundError as e:
        pass
    except Exception as realerror:
        raise realerror
    
    eles = []
    
    with open(CMC_KEY_FILE, encoding='utf-8') as f:
        cmckey = json.load(f)['apikey']
    
        cmcurl = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=500&convert=USD'
        resp = requests.get(cmcurl, headers={
            "X-CMC_PRO_API_KEY": cmckey,
            "Accept": "application/json"
            }).json()
        for cry in resp['data']:
            _ = ignore(cry)
            ele = {}
            for k,v in cry.items():
                if k=='quote':
                    ele['volume_24h_usd'] = v['USD']['volume_24h']
                    #print('volume_24h: %s USD' % v['USD']['volume_24h'])
                elif k=='tags':
                    ele['tags'] = '|'.join(v)
                    #print('tags: %s'%'|'.join(v))
                else:
                    ele[k] = v
                    #print(k,':', v)
            eles+=[ele]
            #print()
        df = pd.DataFrame.from_records(eles)
        df = df.set_index('cmc_rank')
        df.to_csv(DATA_FILE_SYMBOL_LISTING)
        return df
        #print( df )

if __name__ == '__main__':
    df = symbol_lst()
    vol = df[['symbol','volume_24h_usd']]
    ttl = vol.volume_24h_usd.sum()
    vol['vol_pct'] = vol.volume_24h_usd/ttl*100
    
    print(vol)
    print( df.columns )

