import time

REQUEST_LIMIT = 200
WINDOW = 86400

request_log = []

def check_rate_limit():
    global request_log
    now = time.time()
    request_log = [t for t in request_log if now - t < WINDOW]

    if len(request_log) >= REQUEST_LIMIT:
        return False

    request_log.append(now)
    return True