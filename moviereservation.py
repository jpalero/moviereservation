movies = ["Narnia", "Avatar", "Avatar 2", "Jurrasic Park", "John Wick", "Dawn of the dead"]
scheds = ["10:00 AM", "01:00 PM", "04:00 PM", "07:00 PM", "10:00 PM"]

def totalTicketPrice(ticket, price):
    return ticket * price
    
while True:
    isReserve= input("Do you want to reserve? yes or no: ").lower()
    
    if isReserve == "yes":
        count = 0 
        for count, movie in enumerate(movies, start=1):
            print(count, movie)

        movieName = int(input("What movie you want to watch: "))
        selectedMovie = movies[movieName - 1]

        count = 0 
        for count, sched in enumerate(scheds, start=1):
            print(count, sched)

        timeSched = int(input("Select time to watch: "))
        selectedTime = scheds[timeSched - 1]

        price = 200
        name = input("Reserve by? ")
        numOfTicket = int(input("Enter the number of ticket? "))
        totalPrice = totalTicketPrice(numOfTicket, price)
        
        print("----Movie reservation----")
        print("The selected movie is: " + selectedMovie)
        print("Shedule of: "+ selectedTime)
        print("Price of ticket: " + str(price))
        print("Rervation for: " + str(numOfTicket))
        print("Name who reserve: " + name)
        print("Total price of: " + str(totalPrice))
        
    else:
        break