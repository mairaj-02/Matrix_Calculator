<div align="center">
<h1>Matrix Calculator</h1>
</div>

## Overview

This is a modular Python application for performing mathematical operations on **2×2 matrices**. The project emphasizes modularity, maintainability, and code reusability. It includes a secure login system and a menu-driven interface to perform various matrix operations, including addition, subtraction, multiplication, division, determinant comparison, eigenvalue computation, and more.

### Prerequisites

1. Python 3.8 or above.
2. Required libraries:
    - numpy

### Setup

1. Clone the repository:

    `git clone https://github.com/your-username/Matrix_Calculator.git`

    `cd Matrix_Calculator`

2. Install dependencies:

    `pip install numpy`

3. Run the application: 

    Copy the code in Main.py file into another ipynb notebook **Jupyter Notebook** and execute it.

### Usage

 1. Login or Register:
    The program starts with a secure login or registration process.
    User credentials are securely stored in a file (user_data.txt).

2. Select an Operation:
    Upon successful login, the user is presented with the following menu:

Matrix Operations Menu:
1. Add Matrices
2. Subtract Matrices
3. Multiply Matrices
4. Divide Matrices
5. Compare Determinants
6. Find Eigenvalues
7. Compute Matrix Power
8. Find Inverse
9. Exit

Select the operation, input the matrix or matrices **(2x2)**, and get the result.

## Modules and Libraries

1. `hashlib`

    Used for secure password hashing with SHA-256.

2. `os`

    Used for file existence checks during user authentication.

3. `numpy`

    Provides numerical computing functionality, such as eigenvalue calculations.

## Contribution

I am trying to improve this project by adding further functionalities and accepting larger matrices so contributions are welcome! Follow these steps to contribute:

Fork the repository.

Create a feature branch:

`git checkout -b feature/YourFeature`

Commit your changes:

`git commit -m "Add YourFeature"`

Push to your branch:

 `git push origin feature/YourFeature`

Submit a pull request.

## Acknowledgments

This project is developed as part of an academic assignment and adheres to the principles of modular and maintainable software design.
