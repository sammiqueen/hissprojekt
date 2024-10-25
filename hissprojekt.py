def moveElevator(queue) :

    currentFloor = queue[0]
    queue.remove(currentFloor)

    print (currentFloor)
    return currentFloor

def queueSort(queue, currentFloor) :

    if (queue[0] > currentFloor):
        goingDown = False
    else:
        goingDown = True

    queue.sort(reverse = goingDown)

    print (queue)
    return queue, goingDown

def buttonPress(queue, waitQueue, goingDown):

    while True:
        try:
            buttonPress = int(input("Önskad våning?"))
            break
        except:
            print("Endast integers tack")

    if (goingDown and (buttonPress <= queue [0]) or (not goingDown) and (buttonPress >= queue[0])):
        queue.append(buttonPress)
    else:
        waitQueue.append(buttonPress)

queueSort()