import time
import random

def attempt_connection(max_retries):
    current_try = 1
    wait_time = 1

    print(f"--Attempting Connection: Max Retires: {max_retries}")

    while current_try <= max_retries:
        print(f"Attempt: {current_try}")

        success_roll = random.randint(1,10)

        if success_roll > 8:
            print("Success, connected to database")
            return True

        print(f"Failed, retrying in {wait_time} seconds")
        time.sleep(wait_time)

        wait_time = wait_time * 2
        current_try = current_try + 1

    print("Critial Error: Connection timed out")
    return False

attempt_connection(5)
        
    
