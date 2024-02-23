import psutil
from perevod import bytes_to_gb

def get_mem():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    templ_mem = "%-5s :%s %s"
    templ_swap = "%-5s :%s %s"
    print(templ_mem %("VM",int(mem.percent/2)*"/",f'{bytes_to_gb(mem.used)}G/{bytes_to_gb(mem.total)}G'))
    print(templ_swap %("SW",int(swap.percent/2)*"/",f'{bytes_to_gb(swap.used)}G/{bytes_to_gb(swap.total)}G'))
