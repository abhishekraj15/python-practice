import time

wait_time = 1
max_retries = 5
atempts = 0

while atempts < max_retries:
    print("Attempt : ", atempts + 1, "Wait time :",wait_time, )
    time.sleep(wait_time)
    wait_time *= 2
    atempts += 1