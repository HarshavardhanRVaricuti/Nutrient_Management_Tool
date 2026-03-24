from engine import calculate_nitrogen

def test_corn_calculation():

    factors = {'target_n': 1.2, 'efficiency': 0.85}
    result = calculate_nitrogen(factors, target_yield=200, soil_n_ppm=20)
    assert result == 235.29, f"Corn Math failed: Expected 235.29, got {result}"

def test_wheat_calculation():

    factors = {'target_n': 1.0, 'efficiency': 0.80}
    result = calculate_nitrogen(factors, target_yield=200, soil_n_ppm=20)
    assert result == 200.0, f'Wheat Math failed: Expected 200.0, got {result}'
