from termcolor import cprint

def pretty_print_singe(results):
    if results[0]:
        cprint("[*] Content extracted from href tags:",'green')
        for res in results[0]:
            cprint(res,'blue')
    if results[1]:
        cprint("[*] Content extracted from action forms:",'green')
        for res in results[1]:
            cprint(res,'blue')
    if results[2]:
        cprint("[*] Content extracted from script and link tags:",'green')
        for res in results[2]:
            cprint(res,'blue')
        for res in results[3]:
            cprint(res,'blue')

def pretty_print_many(results):
    for sublist in results:
        pretty_print_singe(sublist)