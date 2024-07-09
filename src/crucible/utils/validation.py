def check_exists(*args):
    for arg in args:
        if arg is None:
            raise ValueError(f"No globals provided for {arg}")
