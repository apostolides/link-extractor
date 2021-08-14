import argparse
from description import get_desc
from arg_hander import handle_args

parser = argparse.ArgumentParser(description=get_desc())
parser.add_argument('--url',metavar='URL',help='target url to extract information.')
parser.add_argument('--agent',metavar='AGENT',help='specify a User-Agent for outgoing requests.')
parser.add_argument('--file',metavar='URL_FILE',help='specify a file with multiple urls.')
parser.add_argument('-d',action='store_true',help='extract only domains and sub-domains.')
parser.add_argument('-r',action='store_true',help='use a random built-in User-Agent for outgoing requests.')
parser.add_argument('-a',action='store_true',help='extract hyperlinks from script and link tags too.')

args = parser.parse_args()
handle_args(parser,args)