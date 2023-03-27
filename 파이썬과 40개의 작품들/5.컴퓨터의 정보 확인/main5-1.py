import psutil

# cpu 속도
cpu = psutil.cpu_freq()
print(cpu)

# 물리 코어수 
cpu_core = psutil.cpu_count(logical=False)
print(cpu_core)

# 메모리
memory = psutil.virtual_memory()
print(memory)

# 디스크
disk = psutil.disk_partitions()
print(disk)

# 네트워크 
net = psutil.net_io_counters()
print(net)