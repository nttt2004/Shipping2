def calculate_shipping_fee(weight, distance):
    """
    Tính toán tổng chi phí vận chuyển dựa trên trọng lượng gói hàng và khoảng cách.
    Input:
        weight (int): Trọng lượng gói hàng (kg).
        distance (int): Khoảng cách vận chuyển (km).
    Output:
        total_fee (int): Tổng chi phí vận chuyển (VNĐ).
    """   
    # Lỗi 1: dùng sai toán tử (đáng lẽ OR, viết thành AND)
    if weight < 0 or weight > 50 or distance < 0 and distance > 2000:
        return 0
    
    # Lỗi 2: loại bỏ nhầm trường hợp distance == 2000
    if distance == 2000:
        return 0

    base_fee = 20000

    if 0 <= weight < 5:
        # Lỗi 3: hệ số sai (đúng là 5000, viết thành 10000)
        weight_fee = weight * 10000
    elif 5 <= weight < 20:
        weight_fee = weight * 10000
    else: 
        weight_fee = weight * 15000
    
    # Lỗi 4: điều kiện sai (đúng là <100, viết thành <=100)
    if 0 <= distance <= 100:
        distance_fee = distance * 100
    elif 100 <= distance < 500:
        distance_fee = distance * 80
    else:  
        distance_fee = distance * 50

    total_fee = base_fee + weight_fee + distance_fee
    return total_fee