def moveElevator(queue):
    currentFloor = queue[0]
    queue.remove(currentFloor)
    
    return currentFloor

def queueSort(queue, currentFloor):
    queue.sort(reverse=isGoingDown(queue, currentFloor))

    return queue

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

def integerInput(question):
    while True:
        try:
            answer = int(input(question))
            break
        except Exception:
            print("Endast integers tack")
    return answer


def isGoingDown(queue, currentFloor):
    if queue[0] >= currentFloor:
        goingDown = False
    else:
        goingDown = True
    return goingDown


queue = queueSort(queue, currentFloor)
print(queue)