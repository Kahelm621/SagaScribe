def handle_combat(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player.attack(enemy)
        if enemy.health > 0:
            enemy.attack(player)
    return "You have defeated the enemy!" if player.health > 0 else "You have been defeated."

def handle_event(event):
    if event == "discover_glade":
        return "You have discovered a hidden glade with an ancient altar."
    elif event == "find_stream":
        return "You have found a sparkling stream."
