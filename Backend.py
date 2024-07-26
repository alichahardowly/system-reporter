import psutil
def pc_details():
    memory_usage = psutil.virtual_memory()
    return memory_usage
