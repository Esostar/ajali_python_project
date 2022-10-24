# python game for a car game simulation using a while loop
# such that the car starts when you hit the start button and stop when you input the stop button
command = ""
started = False
while True:
    command = input(">    ").lower()
    if command == "start":
        if started:
            print("hey!! car is already started")
        else:
            started = True
            print("car started")
    elif command == "stop":
        if not started:
            print(" hey!! car is already stopped")
        else:
            started = False
            print("car stopped")
    elif command == "help":
        print("""
    start - to start car
    stop - to stop car
    quit - to quit """)
    elif command == "quit":
        print("game quit")
        break
    else:
        print(" hey!! i don't understand")
