def reward_function(params):

    center_variance = params["distance_from_center"] / params["track_width"]

    left_lane = [17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,106,107,108]#Fill in the waypoints
    
    center_lane = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,89,90,104,105,109,110,111,112,113,114,115,116,117,118]#Fill in the waypoints
    
    right_lane = [91,92,93,94,95,96,97,98,99,100,101,102,103]#Fill in the waypoints
    
    fast = []#Fill in the waypoints
    fast.extend(range(2,16)); fast.extend(range(52,60));fast.extend(range(103,114));
    slow = []#Fill in the waypoints
    slow.extend(range(22,45)); slow.extend(range(77,87));slow.extend(range(94,99));
    
    reward = 21

    if params["all_wheels_on_track"]:
        reward += 10
    else:
        reward -= 10

    if params["closest_waypoints"][1] in left_lane and params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in right_lane and not params["is_left_of_center"]:
        reward += 10
    elif params["closest_waypoints"][1] in center_lane and center_variance < 0.4:
        reward += 10
    else:
        reward -= 10
    if params["closest_waypoints"][1] in fast:
        if params["speed"] == 2 :
            reward += 10
        else:
            reward -= 10
    elif params["closest_waypoints"][1] in slow:
        if params["speed"] == 1 :
            reward += 10
        else:
            reward -= 10
        
    
    return float(reward)