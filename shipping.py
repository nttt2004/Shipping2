def calculate_shipping_fee(weight, distance):
    if weight < 0 or weight > 50 or distance < 0 and distance > 2000:
        return 0
    base_fee = 20000
    if weight < 5:
        weight_fee = weight * 5000
    elif weight < 20:
        weight_fee = weight * 10000
    else: 
        weight_fee = weight * 15000
    if distance < 100:
        distance_fee = distance * 100
    elif distance < 500:
        distance_fee = distance * 80
    else:  
        distance_fee = distance * 50
    total_fee = base_fee + weight_fee + distance_fee
    return total_fee