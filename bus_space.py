def enough(cap, on, wait):
    if on + wait > cap:
        return on + wait - cap
    else:
        return 0