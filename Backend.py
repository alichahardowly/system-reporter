import psutil
def pc_details():
    memory_usage = psutil.virtual_memory()
    total= memory_usage.total
    free=memory_usage.free
    used=memory_usage.used
    return total,free,used
