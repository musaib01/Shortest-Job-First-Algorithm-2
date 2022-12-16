def bubbleSort(cooking_arr, order_arr, order_id_arr):
    n = len(order_arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n - 1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n - i - 1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if order_arr[j] > order_arr[j + 1]:
                swapped = True
                cooking_arr[j], cooking_arr[j + 1] = cooking_arr[j + 1], cooking_arr[j]
                order_arr[j], order_arr[j + 1] = order_arr[j + 1], order_arr[j]
                order_id_arr[j], order_id_arr[j + 1] = order_id_arr[j + 1], order_id_arr[j]

            if order_arr[j] == order_arr[j + 1]:
                swapped = True
                if cooking_arr[j] > cooking_arr[j + 1]:
                    cooking_arr[j], cooking_arr[j + 1] = cooking_arr[j + 1], cooking_arr[j]
                    order_arr[j], order_arr[j + 1] = order_arr[j + 1], order_arr[j]
                    order_id_arr[j], order_id_arr[j + 1] = order_id_arr[j + 1], order_id_arr[j]

        if not swapped:
            # if we haven't needed to make a single swap, we
            # can just exit the main loop.
            return

if __name__ == '__main__':
    total_processes = int(input("Enter no of processes: "))
    order_id = []
    order_time = []
    cooking_time = []
    completion_time = []
    turn_around_time = []
    waiting_time = []
    # taking input
    for i in range(0, total_processes):
        x = int(input("Enter process id:"))
        order_id.append(x)
        y = int(input("Enter order time:"))
        order_time.append(y)
        z = int(input("Enter cooking time:"))
        cooking_time.append(z)
        print()
    # Sorting on the basis of order time
    bubbleSort(cooking_time, order_time, order_id)

    # Calculating CT
    x = cooking_time[0] + order_time[0]
    completion_time.append(x)
    for i in range(1, total_processes):

        if order_time[i] >= completion_time[i - 1]:
            y = order_time[i] - completion_time[i - 1]
            z = cooking_time[i] + completion_time[i - 1] + y
            completion_time.append(z)
        else:
            y = cooking_time[i] + completion_time[i - 1]
            completion_time.append(y)

    #  Calculating TAT
    for i in range(0, total_processes):
        x = completion_time[i] - order_time[i]
        turn_around_time.append(x)

    # Calculating WT
    for i in range(0, total_processes):
        x = turn_around_time[i] - cooking_time[i]
        waiting_time.append(x)

    # Printing sorted array
    print("Process Id\torder Time\tcooking Time\tCompletion Time\tTurn Around time\tWaiting time")
    for i in range(0, total_processes):
        print("%d\t\t\t\t%d\t\t\t\t%d\t\t\t\t%d\t\t\t\t%d\t\t\t\t%d" % (
        order_id[i], order_time[i], cooking_time[i], completion_time[i], turn_around_time[i], waiting_time[i]))
        print()

    x=0
    y=0
    # Calculating average TAT and WT
    for i in range(0, total_processes):
        x=x+turn_around_time[i]
        y=y+waiting_time[i]

    avgTAT=x/total_processes
    avgWT=y/total_processes

    print("\nAverage Turn around time: ",avgTAT)
    print("Waiting time: ",avgWT)
