capacity_pool=30
first_entrance=capacity_pool/10
second_entrance=capacity_pool/15
way_out=capacity_pool/30
water_amount=(first_entrance+second_entrance-way_out)
hour=capacity_pool/water_amount
print(f"Pool fill time {hour} hours")