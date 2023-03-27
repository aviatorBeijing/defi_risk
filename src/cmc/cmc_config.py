import datetime
ROOTDIR='/home/ubuntu'
CMC_KEY_FILE = f'/{ROOTDIR}/.cmc.json'
DATA_FILE_SYMBOL_LISTING = f'/{ROOTDIR}/data/cmc_symbol_listing_%s.csv'%(datetime.datetime.utcnow().strftime('%Y%m%d'))

