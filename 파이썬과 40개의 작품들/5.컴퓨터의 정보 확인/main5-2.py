import psutil

# 필요한 정보만 출력하는 코드 만들기 

# cpu 속도 
cpu = psutil.cpu_freq()
cpu_current_ghz = round(cpu.current/1000, 2)
print("cpu속도:{}GHz".format(cpu_current_ghz))

# 코어 개수 
cpu_core = psutil.cpu_count(logical=False)
print("코어:{}개".format(cpu_core))

# 메모리 
memory = psutil.virtual_memory()
memory_total = round(memory.total/1024**3)
print("메모리:{}GB".format(memory_total))

# 디스크 크기
disk = psutil.disk_partitions()
print(disk)

for p in disk:
    print(p.mountpoint, p.fstype, end="")
    du = psutil.disk_usage(p.mountpoint)
    disk_total = round(du.total/1024**3)
    print("디스크크기:{}GB".format(disk_total))


# 네트워크를 통해 보내고 받은 데이터의 크기를 MB단위로 출력합니다.
net = psutil.net_io_counters()
sent = round(net.bytes_sent/1024**2, 1)
recv = round(net.bytes_recv/1024**2, 1)
print("보내기: {}MB 받기: {}MB".format(sent, recv))

 