import psutil
def get_processes_info():
    def decorator2():
        processes_info = []
        for process in psutil.process_iter(['pid', 'name', 'username', 'ppid']):
            processes_info.append(process.info)
        return processes_info
    return decorator2
