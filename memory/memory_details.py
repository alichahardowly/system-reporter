#this is for details
import psutil
def pc_details():
    memory_usage = psutil.virtual_memory()
    total= memory_usage.total // (1024 * 1024)
    free=memory_usage.free // (1024 * 1024)
    used=memory_usage.used // (1024 * 1024)
    return total,free,used
