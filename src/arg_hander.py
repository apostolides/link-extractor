import agents
import scenarios
import results
from termcolor import cprint
from datetime import datetime

def handle_args(parser,args):
    agent = args.agent 
    domains_only = args.d
    extract_all = args.a
    
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cprint(f"[*] Starting process at: {current_time}",'yellow')

    res = None
    if args.r:
        agent = agents.random_agent()
    if args.file:
        res = scenarios.urls_from_file(args.file,domains_only=domains_only,extract_all=extract_all,agent=agent)
        results.pretty_print_many(res)
    elif args.url:
        res = scenarios.single_url(args.url,domains_only=domains_only,extract_all=extract_all,agent=agent)
        results.pretty_print_singe(res)
    else:
        parser.print_help()

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    cprint(f"[*] Process finished at: {current_time}",'yellow')

    