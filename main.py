from pet import Pet

def main():
    print("🎮 Welcome to the Virtual Pet Game!")
    name = input("What's your pet's name? ")
    my_pet = Pet(name)

    while True:
        print("\nWhat would you like to do?")
        print("1. Feed your pet 🍗")
        print("2. Let your pet sleep 😴")
        print("3. Play with your pet 🎾")
        print("4. Teach a new trick 🎓")
        print("5. Show learned tricks 🧠")
        print("6. Check pet status 📊")
        print("7. Exit the game ❌")

        choice = input("Enter your choice (1–7): ")

        if choice == "1":
            my_pet.eat()
        elif choice == "2":
            my_pet.sleep()
        elif choice == "3":
            my_pet.play()
        elif choice == "4":
            trick = input("Enter the name of the trick: ")
            my_pet.train(trick)
        elif choice == "5":
            my_pet.show_tricks()
        elif choice == "6":
            my_pet.get_status()
        elif choice == "7":
            print(f"👋 Goodbye! {my_pet.name} will miss you!")
            break
        else:
            print("❗ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
