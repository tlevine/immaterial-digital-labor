import argparse
from .download import download
from .condense import condense

ACCESS_TOKEN_MESSAGE = '''
Go to this address, get an access token, and paste it below.
https://developers.facebook.com/tools/explorer/

'''
FIELDNAMES = [
    'message',
    'facebook-link', 'external-link',
    'from-id', 'from-name',
]

def parse_args():
    argparser = argparse.ArgumentParser(
        description = 'Download links from the Immaterial Digital Labor group, '\
                      'and present them in some presentable way.',
    )
    argparser.add_argument('--access_token')

    _args = argparse.parse_args()
    if None == _args.access_taken:
        _args.access_token = input(ACCESS_TOKEN_MESSAGE)
    return _args

def cli():
    import csv, sys
    args()
    w = csv.DictWriter(sys.stdout, FIELDNAMES)
    for post in download(access_token):
        w.writerows(condense(post))
