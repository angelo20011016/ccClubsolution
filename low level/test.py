import math
from datetime import datetime

def calculate_fee(start_time_str: str, end_time_str: str, is_ntu: bool) -> int:
    time_format = '%H:%M'
    start_time_obj = datetime.strptime(start_time_str, time_format)
    end_time_obj = datetime.strptime(end_time_str, time_format)
    total_minutes = (end_time_obj - start_time_obj).total_seconds() / 60

    if total_minutes < 1:
        return 0
    if is_ntu and total_minutes < 30:
        return 0

    billing_blocks = math.ceil(total_minutes / 30)
    price_per_block = 10 if is_ntu else 20
    fee = billing_blocks * price_per_block
    return int(fee)

if __name__ == "__main__":
    start = input()
    end = input()
    is_ntu_input = input()
    has_id = (is_ntu_input == 'Y')
    print(calculate_fee(start, end, has_id))