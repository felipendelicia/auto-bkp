INFO_UNIT = ["Byte", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB", "SB", "JB"]

def display_size(size:float, unit_index:int = 0)-> str: # size in bytes
    if size < 1024.0:
        return str(round(size, 2)) + INFO_UNIT[unit_index]
    return display_size(size / 1024, unit_index + 1)
