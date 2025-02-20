from module import read, add, subtract, multiplication

def main():
    try:
        while True:
            print("""
    ==============================
                """)
            print("1. Read matrices")
            print("2. Add matrices")
            print("3. Subtract matrices")
            print("4. Multiply matrices")
            print("5. Exit\n")
            choice = int(input("Enter your choice: "))
            if choice == 1:
                try:
                    file = input("Enter the file name: ")
                    print(read(file))
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
            elif choice == 2:
                try:
                    file1 = input("Enter the first file name: ")
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
                try:                        
                    file2 = input("Enter the second file name: ")
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
                matrix1 = read(file1)
                matrix2 = read(file2)

                result = add(matrix1[0], matrix2[0])
                with open("result.txt", "w") as f:
                    for line in result:
                        f.write(f"{line}\n")
                print("Result written to result.txt")

            elif choice == 3:
                try:
                    file1 = input("Enter the first file name: ")
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
                try:                        
                    file2 = input("Enter the second file name: ")
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
                result = subtract(file1, file2)
                with open("result.txt", "w") as f:
                    for line in result:
                        f.write(f"{line}\n")
                print("Result written to result.txt")

            elif choice == 4:
                try:
                    file1 = input("Enter the first file name: ")
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
                try:                        
                    file2 = input("Enter the second file name: ")
                except FileNotFoundError as e:
                    print("File not found", e)
                    main()
                result = multiplication(file1, file2)
                with open("result.txt", "w") as f:
                    for line in result:
                        f.write(f"{line}\n")
                print("Result written to result.txt")

            elif choice == 5:
                print("Exiting...Goodbye!")
                break
            else:
                print("Invalid choice")

    except ValueError as e:
        print("Invalid input. Please enter a number.")
        main()


if __name__ == "__main__":
    main()