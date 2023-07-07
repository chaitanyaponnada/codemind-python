
def calculate_angle(hour, minute):
    hour_angle = (60 * hour + minute) / 2
    minute_angle = 6 * minute
    angle = abs(hour_angle - minute_angle)
    return min(angle, 360 - angle)

# Example usage: Calculate angle at 3:30
a,b=input().split(":")
a=int(a)
b=int(b)
angle = calculate_angle(a,b)
print(angle)
