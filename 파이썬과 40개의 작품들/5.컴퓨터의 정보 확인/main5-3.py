import psutil

# 1초당 반복해서 정보를 출력하는 코드 만들기 

curr_sent = 0
curr_recv = 0

prev_sent = 0
prev_recv = 0

while True:
    cpu_p = psutil.cpu_percent(interval=1)
    print("CPU사용량: {}%".format(cpu_p))

    memory = psutil.virtual_memory()
    memory_avail = round(memory.available/1024**3, 1)
    print("사용 가능한 메모리: {}GB".format(memory_avail))

    net = psutil.net_io_counters()
    curr_sent = net.bytes_sent/1024**2
    curr_recv = net.bytes_recv/1024**2

    sent = round(curr_sent - prev_sent, 1)
    recv = round(curr_recv - prev_recv, 1)

    print("보내기: {}MB 받기: {}MB".format(sent, recv))

    prev_sent = curr_sent
    prev_recv = curr_recv