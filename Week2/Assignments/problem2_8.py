def problem2_8(temp_list):
    sum_ = 0
    list_items = len(temp_list)
    for temp in temp_list:
        sum_ = sum_ + temp
        average = sum_ / list_items
    print("Average:", average)
    print("High:",max(temp_list))
    print("Low:",min(temp_list))