def monitor_following_distance(distances: list[float], speeds: list[float]) -> tuple[int, float, int]:
    if not distances:
        return (0, 0.0, 0)

    tlgSeconds = 0
    minDist = distances[0]
    tlgIncidents = 0
    flg = False

    for i in range(len(distances)):
        if distances[i] < minDist:
            minDist = distances[i]
        
        if distances[i] < speeds[i] * 0.5:
            tlgSeconds += 1

            if flg == True:
                continue
            else:
                flg = True
                tlgIncidents += 1

        else:
            if flg == True:
                flg = False

    return (tlgSeconds, minDist, tlgIncidents)
# """
    # Analyzes following distance compared to safe distance (speed * 0.5).
    
    # Args:
    #     distances (list[float]): Distance to the lead car at each second.
    #     speeds (list[float]): Speed of our car at each second.
        
    # Returns:
    #     tuple[int, float, int]: (tailgating_seconds, minimum_distance, tailgate_incidents)
    #         - tailgating_seconds: total seconds distance was < safe distance
    #         - minimum_distance: absolute closest distance to the lead car (return 0.0 if empty list)
    #         - tailgate_incidents: number of separate instances the car started tailgating
    # """
    pass
