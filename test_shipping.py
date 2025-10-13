from shipping import calculate_shipping_fee

# def test_case_1():
#     """Trường hợp 1: weight=52, distance=1396 → đầu vào không hợp lệ"""
#     assert calculate_shipping_fee(52, 1396) == 0


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
