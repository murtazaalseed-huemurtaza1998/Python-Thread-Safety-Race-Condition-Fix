# Python Thread Safety - Race Condition Fix 🔒

A practical demonstration of Race Condition problem in Python and how to fix it using `Lock`.

## 📌 The Problem

When two threads try to update the same variable (`database_value`) at the same time without protection, data is lost.

**Unsafe flow:**
1. Thread-1 reads `database_value = 0`
2. Thread-2 also reads `database_value = 0`
3. Both increase to 1
4. Final value = 1 (Wrong! Should be 2)

This is called **Race Condition**.

## ✅ The Solution

Using `threading.Lock()` to make the critical section safe. Only one thread can enter at a time.

```python
with lock:
    local = database_value
    local += 1
    database_value = local
