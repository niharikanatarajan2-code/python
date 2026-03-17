def shutdown():
    print("\nSaving data...")
    print("System is shutting down.Goodbye!")
    exit()


def start_program():
    print("Program restarted.\n")
    while True:
        print("\n-----MAIN MENU-----")
        print("1.Start Program")
        print("2.Restart Program")
        print("3.Shutdown")
        choice = input("Enter your choice:")
        if choice =="1":
            start_program()
        elif choice =="2":
            start_program()
        elif choice =="3":
            shutdown()
        else:
            print("Invalid choice.Try again.")

start_program()