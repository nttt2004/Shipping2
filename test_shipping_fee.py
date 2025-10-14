#C2
from shipping import calculate_shipping_fee

def test_case_1():
    """Trường hợp 1: weight=52, distance=1396 → đầu vào không hợp lệ"""
    assert calculate_shipping_fee(52, 1396) == 0


def test_case_2():
    """Trường hợp 2: weight=42, distance=2000 → hợp lệ, nhánh weight>20, distance>500"""
    result = calculate_shipping_fee(42, 2000)
    print("Case 2:", result)
    assert result == 750000


def test_case_3():
    """Trường hợp 3: weight=3, distance=72 → nhánh weight<5, distance<100"""
    result = calculate_shipping_fee(3, 72)
    print("Case 3:", result)
    assert result == 42200


def test_case_4():
    """Trường hợp 4: weight=17, distance=465 → nhánh weight 5–20, distance 100–500"""
    result = calculate_shipping_fee(17, 465)
    print("Case 4:", result)
    assert result == 227200


def test_case_5():
    """Trường hợp 5: weight=38, distance=846 → nhánh weight>=20, distance>500"""
    result = calculate_shipping_fee(38, 846)
    print("Case 5:", result)
    assert result == 632300

# C1
# import pytest
# from shipping import calculate_shipping_fee

# # Danh sách test case: (id, weight, distance, expected_output)
# test_data = [
#     ("Tc1", 52, 1396, 0),        # Đầu vào không hợp lệ (weight > 50)
#     ("Tc2", 42, 2000, 750000),   # weight > 20, distance > 500
#     ("Tc3", 3, 72, 42200),       # weight < 5, distance < 100
#     ("Tc4", 17, 465, 227200),    # weight 5–20, distance 100–500
#     ("Tc5", 38, 846, 632300),    # weight >= 20, distance > 500
# ]

# @pytest.mark.parametrize("test_id, weight, distance, expected", test_data)
# def test_calculate_shipping_fee(test_id, weight, distance, expected):
#     """
#     Kiểm tra hàm calculate_shipping_fee với các bộ dữ liệu khác nhau.
#     """
#     # Gọi hàm cần test
#     result = calculate_shipping_fee(weight, distance)
    
#     # In kết quả để dễ debug khi test
#     print(f"{test_id}: weight={weight}, distance={distance} => result={result}")
    
#     # So sánh với kết quả mong đợi
#     assert result == expected, f"Lỗi ở test case {test_id}: mong đợi {expected}, nhận được {result}"