def get_max_lengths(func):
    def decorator(processes_info):
        
        max_name_length = max(len(info['name']) for info in processes_info) + 2
        max_username_length = max(len(info['username']) for info in processes_info) + 2
        max_pid_length = max(len(str(info['pid'])) for info in processes_info) + 2
        max_ppid_length = max(len(str(info['ppid'])) for info in processes_info) + 2

        return func(processes_info, max_name_length, max_username_length, max_pid_length, max_ppid_length)
    return decorator