from threading import Thread, Lock
import time

database_value = 0
lock = Lock()

def increase_unsafe():
    """نسخة غير آمنة - توضح مشكلة Race Condition"""
    global database_value
    local = database_value
    local += 1
    time.sleep(0.01) # محاكاة وقت معالجة قاعدة البيانات
    database_value = local

def increase_safe():
    """نسخة آمنة - الحل باستخدام Lock"""
    global database_value
    with lock:
        local = database_value
        local += 1
        time.sleep(0.01)
        database_value = local

def run_test(func, name):
    global database_value
    database_value = 0
    t1 = Thread(target=func)
    t2 = Thread(target=func)
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(f"{name} -> End Value: {database_value}")

if __name__ == "__main__":
    print("Start value: 0\n")
    run_test(increase_unsafe, "UNSAFE (Bug)  ")
    run_test(increase_safe, "SAFE (Fixed)  ")
    print("\nEnd Main")
