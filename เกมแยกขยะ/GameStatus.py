
class GameStatus:
    total_score = 0
    blue_trash_bin_score = 0
    green_trash_bin_score = 0
    yellow_trash_bin_score = 0
    red_trash_bin_score = 0

    

    food_trash = 5
    crisps_trash = 6
    bottle_trash = 3
    battery_trash = 1

    max_blue_trash_bin_score = 1 * crisps_trash
    max_green_trash_bin_score = 2 * food_trash 
    max_yellow_trash_bin_score = 3 * bottle_trash
    max_red_trash_bin_score = 5 * battery_trash

    max_total_score = max_blue_trash_bin_score \
                        + max_green_trash_bin_score \
                        + max_yellow_trash_bin_score \
                        + max_red_trash_bin_score

    max_trash = food_trash + crisps_trash + bottle_trash + battery_trash
    count_trash = 0

    running = True
    playing = False
    restart = False
    game_over = False
    win = False
    lose = False
