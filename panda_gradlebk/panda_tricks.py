import pandas as pd

def start():
    options = {
        'display': {
            'max_columns': None,
            'max_colwidth': 25,
            'expand_frame_repr': False,  # Don't wrap to multiple pages
            'max_rows': 14,
            'max_seq_items': 50,         # Max length of printed sequence
            'precision': 2,
            'show_dimensions': False
        },
        'mode': {
            'chained_assignment': None   # Controls SettingWithCopyWarning
        }
    }
    
    for category, option in options.items():
        for op, value in option.items():
#            print(f'{category}.{op}: {value}')
            pd.set_option(f'{category}.{op}', value)


if __name__ == "__main__":
    
   
    url = ('https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data')
    cols = ['sex', 'length', 'diam', 'height', 'weight', 'rings']
    
    abalone = pd.read_csv(url, usecols=[0, 1, 2, 3, 4, 8], names=cols)
    print(abalone)

    start()
    
    abalone = pd.read_csv(url, usecols=[0, 1, 2, 3, 4, 8], names=cols)
    print(abalone)

    del start
