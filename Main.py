from Login import login
from Matrix import Mat2x2

def main():
    # Ensure user logs in
    user_file = "user_data.txt"
    if not login(user_file):
        return

    # Start the matrix operations
    while True:
        print("\nMatrix Operations Menu:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Divide Matrices")
        print("5. Compare Matrices")
        print("6. Find Inverse")
        print("7. Compute Matrix Power")
        print("8. Find Eigenvalues")
        print("9. Exit")
        choice = input("Choose an option (1-9): ")

        if choice == '9':
            print("Exiting program. Goodbye!")
            break

        try:
            # Input the first matrix for all operations
            print("Enter the elements of matrix:")
            a1, b1, c1, d1 = map(float, input("a b c d: ").split())
            matrix1 = Mat2x2(a1, b1, c1, d1)

            if choice in ['1', '2', '3', '4', '5']:  # Operations requiring two matrices
                print("Enter the elements of the second matrix (required for this operation):")
                a2, b2, c2, d2 = map(float, input("a b c d: ").split())
                matrix2 = Mat2x2(a2, b2, c2, d2)

            if choice == '1':  # Addition
                result = matrix1.add(matrix2)
                print(f"Resulting Matrix:\n{result}")
            elif choice == '2':  # Subtraction
                result = matrix1.subtract(matrix2)
                print(f"Resulting Matrix:\n{result}")
            elif choice == '3':  # Multiplication
                result = matrix1.multiply(matrix2)
                print(f"Resulting Matrix:\n{result}")
            elif choice == '4':  # Division
                result = matrix1.divide(matrix2)
                print(f"Resulting Matrix:\n{result}")
            elif choice == '5':  # Compare Determinants
                comparison = matrix1.compare(matrix2)
                if comparison == 0:
                    print("Both matrices have the same determinant.")
                elif comparison == 1:
                    print("The first matrix has a larger determinant.")
                else:
                    print("The second matrix has a larger determinant.")
            elif choice == '6':  # Inverse
                result = matrix1.inverse()
                print(f"Inverse Matrix:\n{result}")
            elif choice == '7':  # Power
                n = int(input("Enter the power (non-negative integer): "))
                result = matrix1.power(n)
                print(f"Resulting Matrix:\n{result}")
            elif choice == '8':  # Inverse# Eigenvalues
                eigenvalues = matrix1.find_eigenvalues()
                print(f"Eigenvalues of the matrix: {eigenvalues}")

        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as e:
            print(f"Unexpected error: {e}")

# Run the main function
if __name__ == "__main__":
    main()