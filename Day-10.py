command = ""

started = False
while True:
    
    command = input("Enter a thing: ").lower()
    
    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started.")    
        
    elif command == "stop":
        if not started:
            print("Car is already stopped ...")   
        else:
            started = False
            print("Car stopped ...")
            
    elif command == "help":
        print("""
        start - Start the car
        stop - Stop the car
        quit - Exit the program
        """)
    elif command == "quit":
        print("Goodbye!")
        break
    else:
        print("I don't understand what you want.")  
