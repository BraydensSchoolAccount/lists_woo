# lists activities 1
# Brayden Towner
# 01/30/2024


weather_list = ["sunny", "thunderstorm", "rain", "hurricane", "snow"]
other_weather_list = weather_list.copy()
other_weather_list.insert(2 , "sleet")
other_weather_list.append("tornado")
print("Original Weather List: ", weather_list)
print("Other Weather List: ", other_weather_list)
other_weather_list.clear()
print("Original Weather List (Post clear): ", weather_list)
print("Other Weather List but emptied: ", other_weather_list)

num_list_1 = [45, 6, 78.39494959487]
num_list_2 = [1,12]
all_nums = num_list_1 + num_list_2
num_list_1.extend(num_list_2)
print("Number lists combined (separate variable): ", all_nums)
print("Number lists combined (into list 1): ", num_list_1)

colors = ["red", "green", "purple", "yellow", "blue"]
descending_odd_colors = colors[::-2]
print("Colors of the list", colors, "but it's only the odd indexes descending: ", descending_odd_colors)

new_num_list = [4, 5, 6, 1, 3, 2, 0, 5]
new_num_list.extend([4,5,5])

print("The number list is the following: ", new_num_list)
print("The number 5 is in the list: ", 5 in new_num_list)
print("The number of 5s in the list: ", new_num_list.count(5))