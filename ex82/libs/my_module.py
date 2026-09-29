def calc_electricity_bill(customer_type, kwh_old, kwh_new):
    """Tính tiền điện từ chỉ số công tơ cũ và mới.
    customer_type: 1 (giá bậc thang, 6 mức) hoặc 2 (giá cố định)
    kwh_old, kwh_new: chỉ số kWh cũ và mới trên công tơ
    Trả về (kwh_used, total)."""
    kwh_used = kwh_new - kwh_old

    if customer_type == 1:
        levels = [
            (50, 1549),    # Level 1: 0-50
            (100, 1600),   # Level 2: 51-100
            (200, 1858),   # Level 3: 101-200
            (300, 2340),   # Level 4: 201-300
            (400, 2615),   # Level 5: 301-400
            (None, 2701),  # Level 6: từ 401 trở lên
        ]
        total = 0
        remaining = kwh_used
        prev_cap = 0
        for cap, price in levels:
            if remaining <= 0:
                break
            tier_kwh = remaining if cap is None else min(remaining, cap - prev_cap)
            total += tier_kwh * price
            remaining -= tier_kwh
            if cap is not None:
                prev_cap = cap
        return kwh_used, total

    else:  # customer_type == 2
        total = kwh_used * 2271
        return kwh_used, total