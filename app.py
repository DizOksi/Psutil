import os
import psutil
import time



def bytes_to_gb(n):
    res = n / (1024 ** 3)
    return round(res, 2)

def get_cpu():
    ...
    return {}

def write_to_file(func):
    def wrapper(*args, **kwargs):
        # Создаем строку с таблицей
        table = func(*args, **kwargs)

        # Записываем таблицу в файл
        with open("processes_table.txt", "w") as file:
            file.write(table)
        print('Таблица с информацией о процессах была успешно записана в файл "processes_table.txt".')
        # Возвращаем таблицу
        return table
    return wrapper


def get_mem():
    mem = psutil.virtual_memory()
    swap = psutil.swap_memory()
    templ_mem = "%-5s :%s %s"
    templ_swap = "%-5s :%s %s"
    print(templ_mem %("VM",int(mem.percent/2)*"/",f'{bytes_to_gb(mem.used)}G/{bytes_to_gb(mem.total)}G'))
    print(templ_swap %("SW",int(swap.percent/2)*"/",f'{bytes_to_gb(swap.used)}G/{bytes_to_gb(swap.total)}G'))

# def show_cpu():
    # columns = proc.as_dict(attrs=['name', 'username', 'pid', 'exe'])
    
    # for n, column in enumerate(columns):
    #     print(f'{column:{max_columns[n]+1}}')
    # i = 0
    # for proc in psutil.process_iter():
    #     pinfo = proc.as_dict(attrs=['name','username', 'pid', 'exe'])
    #     print(pinfo['name'], pinfo['username'] , pinfo['pid'], pinfo['exe'])
    #     i += 1
    #     if i == 30:
    #         break

def get_processes_info():
    processes_info = []
    for process in psutil.process_iter(['pid', 'name', 'username', 'ppid']):
        processes_info.append(process.info)
    return processes_info

@write_to_file
def display_processes_table():
    processes_info = get_processes_info()

    max_name_length = max([len(info['name']) for info in processes_info]) - 8
    max_username_length = max([len(info['username']) for info in processes_info])
    max_pid_length = max([len(str(info['pid'])) for info in processes_info])
    max_ppid_length = max([len(str(info['ppid'])) for info in processes_info])

    table = "{:<{name_length}} | {:<{username_length}} | {:<{pid_length}} | {:<{ppid_length}}\n".format('Name', 'Username', 'PID', 'Parent PID', 
                                                                                                        name_length=max_name_length,
                                                                                                        username_length=max_username_length,
                                                                                                        pid_length=max_pid_length,
                                                                                                        ppid_length=max_ppid_length)
    print("=" * (max_name_length + max_username_length + max_pid_length + max_ppid_length))   
    
    for info in processes_info[:30]:
        table += "{:<{name_length}} | {:<{username_length}} | {:<{pid_length}} | {:<{ppid_length}}\n".format(info['name'], info['username'], info['pid'], info['ppid'],
                                                                                                        name_length=max_name_length,
                                                                                                        username_length=max_username_length,
                                                                                                        pid_length=max_pid_length,
                                                                                                        ppid_length=max_ppid_length)
    print(table)
    return table

#display_processes_table()

    # with open('processes_info.txt', 'w') as file:
    #     file.write("{:<{name_length}} {:<{username_length}} {:<{pid_length}} {:<{ppid_length}}\n".format('Name', 'Username', 'PID', 'Parent PID', 
    #                                                                                 name_length=max_name_length,
    #                                                                                 username_length=max_username_length,
    #                                                                                 pid_length=max_pid_length,
    #                                                                                 ppid_length=max_ppid_length))
    #     file.write("=" * (max_name_length + max_username_length + max_pid_length + max_ppid_length) + "\n")
    # print("{:<{name_length}} | {:<{username_length}} | {:<{pid_length}} | {:<{ppid_length}}".format('Name', 'Username', 'PID', 'Parent PID', 
    #                                                                                         name_length=max_name_length,
    #                                                                                         username_length=max_username_length,
    #                                                                                         pid_length=max_pid_length,
    #                                                                                         ppid_length=max_ppid_length))
    # print("=" * (max_name_length + max_username_length + max_pid_length + max_ppid_length))
    # for info in processes_info[:30]:
    #     print("{:<{name_length}} | {:<{username_length}} | {:<{pid_length}} | {:<{ppid_length}}".format(info['name'], info['username'], info['pid'], info['ppid'], 
    #                                                                                                 name_length=max_name_length,
    #                                                                                                 username_length=max_username_length,
    #                                                                                                 pid_length=max_pid_length,
    #                                                                                                 ppid_length=max_ppid_length))
        

# def show(cpu, mem, disk):
#     show_cpu(cpu)
#     ...

# def main():
    # cpu_info = get_cpu()
    # mem_info = get_mem()
    # show(cpu=cpu_info, mem=mem_info, disk={})


if __name__ == "__main__":
#     main()

    while True:
        cpu = 'cpu_status'
        cpu_percents = psutil.cpu_percent(percpu=True)
        print("\033[33;40;1m%-69s\033[0m" % (f'{cpu:.^30}'))
        for i, percentage in enumerate(cpu_percents):
            print( f"Загруженность ядра процессора {i+1}: {percentage}%", int(percentage/2)*"/")
        get_mem()
        #write_to_file(func)
        get_processes_info()
        display_processes_table()
        # show_cpu()
        time.sleep(1)
        os.system('clear')
