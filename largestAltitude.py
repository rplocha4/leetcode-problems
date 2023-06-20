def largestAltitude(gain):
    max_altitude = 0
    current_altitude = 0
    for n in gain:
        current_altitude += n
        max_altitude = max(max_altitude, current_altitude)

    return max_altitude
