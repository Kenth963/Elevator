from api import Command, Simulation, UP, DOWN, MOVE, STOP


def newone():
    """An example bot that sends elevators up and down and stops at floors if there are passengers waiting to get on or off"""
    simulation = Simulation(
        event="try",
        building_name="tiny_random",
        bot="newbot",
        email="tsukki963@mail.com",
        sandbox=True,
    )
    current_state = simulation.initial_state
    directions = {}  # current directions of elevators

    while current_state["running"]:
        commands = []
        for elevator in current_state["elevators"]:
        
            direction = directions.get(elevator["floor"], UP)

            directions[elevator["id"]] = direction
            action = MOVE

            for request in current_state["requests"]:
                if (
                    request["floor"] == elevator["floor"]
                    and request["direction"] == direction
                ):
                    action = STOP
                else:
                    if elevator["floor"] != request["floor"] and elevator["floor"] > request["floor"]:
                        direction = DOWN
                    elif elevator["floor"] != request["floor"] and elevator["floor"] < request["floor"]:
                        direction = UP
                    action = MOVE

                    

            commands.append(
                Command(elevator_id=elevator["id"], direction=direction, action=action)
            )

        current_state = simulation.send(commands)

    print("Score:", current_state.get("score"))
    print("Replay URL:", current_state.get("replay_url"))


if __name__ == "__main__":
    newone()
