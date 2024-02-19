from tools import adfocus
import random
import requests
import keyboard
from tools import click
import time
import threading

# Shared variable to signal threads to stop
found_url = None
lock = threading.Lock()

def find_url():
    global found_url
    while True:
        with lock:
            # Check if a URL has been found by any thread
            if found_url is not None:
                return
        try:
            url = 'https://' + ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(5)) + '.com'
            if requests.get(url, timeout=5).status_code == 200:
                with lock:
                    if found_url is None:  # Ensure no other thread has set it
                        found_url = url
                        print('Working URL found:', url)
                return
        except requests.RequestException:
            pass

def generate_url():
    threads = []
    for i in range(10):
        t = threading.Thread(target=find_url)
        t.daemon = True
        t.start()
        threads.append(t)
    
    # Wait for any of the threads to find a URL
    for t in threads:
        t.join()

    return found_url

def yn_input(prompt):
    print(prompt, end=' ', flush=True)
    while True:
        if keyboard.is_pressed('y'):
            print('y')
            return True
        elif keyboard.is_pressed('n'):
            print('n')
            return False

def main():
    api_key = input('Enter API Key: ')
    if yn_input('Use Threading? [Y/N]:'):
        threads = int(input('Enter number of threads: '))
    if yn_input('Optimize for real money making? [Y/N]:'):
        money = True
    else:
        money = False
    repeat = int(input('Enter number of times to click per thread: '))
    print('Generating random url to use as redirect...')
    adfocus_url = adfocus.create(api_key, generate_url())
    if adfocus_url.status_code == 200:
        if money == True:
            print('Waiting 60 seconds after url creation so that clicks look legit...')
            time.sleep(60)
        if threads:
            print(f'Adding {threads} clicks per round, {repeat} rounds, total clicks: {threads * repeat}')
            # alot of calculations here
            wait = 2
            threads_wait = wait + (threads * (0.15 + (threads // 1000)))
            extra = 4.5
            new_wait = threads_wait + extra
            ETA = new_wait * repeat
            if ETA > 60:
                ETA = ETA / 60
                if ETA > 60:
                    ETA = ETA / 60
                    print(f'Estimated time: {ETA} hours')
                else:
                    print(f'Estimated time: {ETA} minutes')
            else:
                print(f'Estimated time: {ETA} seconds')
            click.click(adfocus_url.text, threads, repeat)
        else:
            print(f'Adding 1 click per round, total clicks: {repeat}')
            ETA = 18
            print(f'Estimated time: {ETA} seconds')
            click.click(adfocus_url.text, repeat=repeat)

if __name__ == '__main__':
    main()