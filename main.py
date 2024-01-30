# lists activities 1
# Brayden Towner
# 01/30/2024

weather_list = ["sunny", "sleet", "rain", "hurricane", "tornado"]
other_weather_list = weather_list.copy()
other_weather_list.sort()
print("Original List: ", weather_list)
print("Other List: ", other_weather_list)
other_weather_list.clear()
print("Other List but empty: ", other_weather_list)

num_list_1 = [45, 6, 78.39494959487]
num_list_2 = [1,12]
all_nums = num_list_1 + num_list_2
num_list_1.extend(num_list_2)
print("Number lists combined (separate variable): ", all_nums)
print("Number lists combined (into list 1): ", num_list_1)

colors = ["red", "green", "purple", "yellow", "blue"]
descending_odd_colors = colors[::-2]
print("Colors of the list", colors, "but it's only the odd indexes descending: ", descending_odd_colors)
