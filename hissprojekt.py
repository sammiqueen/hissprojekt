def moveElevator(queue):
    currentFloor = queue[0]
    queue.remove(currentFloor)
    
    pack = [queue, currentFloor]
    return pack

def queueSort(queue,currentFloor):
    queue.sort(reverse=isGoingDown(queue,currentFloor))

    return queue

def integerInput(question):
    while True:
        try:
            return int(input(question))
        except Exception:
            print("Endast integers tack")

def buttonPress(queue, waitQueue, currentFloor):
    buttonPress = integerInput("Önskad våning?")

    if (
        isGoingDown(queue, currentFloor)
        and (buttonPress <= queue[0])
        or (not isGoingDown(queue, currentFloor))
        and (buttonPress >= queue[0])
    ):
        queue.append(buttonPress)
    else:
        waitQueue.append(buttonPress)
    
    pack = [queue, waitQueue]
    return pack

def isGoingDown(queue, currentFloor):
    if queue[0] >= currentFloor:
        goingDown = False
    else:
        goingDown = True
    return goingDown

currentFloor = 0
queue = [0]
waitQueue = []

while(True):
    userInput = input("test prompt")

    #switch directions
    if(
        #queue.length == 0
        #or
        userInput == "swap"
    ):
        queue = waitQueue
        waitQueue = []

    if (userInput == "buttonpress"):
        pack = buttonPress(queue, waitQueue, currentFloor)
        queue = pack[0]
        print(queue)
        waitQueue = pack[1]
        print(waitQueue)

    if (userInput == "step"):
        pack = moveElevator(queue)
        queue = pack[0]
        currentFloor = pack[1]
        print(queue, currentFloor)

    if (userInput == "sort"):
        queue = queueSort(queue,currentFloor)
        print(queue)