

def calculate_nitrogen(crop_factors, target_yield, soil_n_ppm):
    """Calculates the nitrogen requirement for a given crop using the crop factors."""
    soil_n_lbs = soil_n_ppm * 2
    base_requirement = target_yield * crop_factors["target_n"] - soil_n_lbs
    final_requirement = base_requirement / crop_factors["efficiency"]
    return max(0.0, round(final_requirement, 2))
