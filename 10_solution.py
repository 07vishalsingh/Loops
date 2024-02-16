'''
10.Implement an exponential backoff strategy that doubts the wait time between retries,starting from 1 second,but stops after retries.
'''
import time

wait_time = 1
max_retries = 5
attempts = 0

while attempts < max_retries:
    print("Attempts",attempts +1, "- wait time", wait_time,)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1