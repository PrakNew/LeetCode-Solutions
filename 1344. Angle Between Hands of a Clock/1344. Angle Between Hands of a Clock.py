class Solution:
    def angleClock(self, hour, minutes):
        minute_angle = minutes  * 6
        hour_angle = 0.5 * (hour * 60 + minutes)
        angle = abs(hour_angle - minute_angle)
        return min(angle, 360-angle)