#extract.py

import os
import requests


def extract(url, filepath):
    """
    Download data from a URL and save it to a file
    """
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    print('Downloading data...')
    try:
        r = requests.get(url)
        r.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error: {e}')
        return
    else:
        with open(f'{filepath}/data.json', 'wb') as f:
            f.write(r.content)
        print(f'Data downloaded to {filepath}/data.json')
    finally:
        print('Data extraction completed.')



if __name__ == '__main__':
    print('URL not set, please set the URL, or continue using data.json')
    # url = 'changeme'
    # filepath = './data'
    # extract(url, filepath)
