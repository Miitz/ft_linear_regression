import sys
try:
    import thetas
    theta0 = thetas.theta0
    theta1 = thetas.theta1
except:
    print("You should first run ft_linear_regression.py!")
    sys.exit(1)

flag = True

while flag:
    mileage = input("Please enter mileage: ")
    try:
        if int(mileage) < 0:
            raise Exception()
        prediction = theta0 + theta1 * int(mileage)
        print(f"The predicted price is: {round(prediction, 0)}")
        if input("Continue? (yes/no): ") == "no":
            flag = False
    except:
        print("Error: please verify your input!")
        print("You should enter an integer as mileage.")
        sys.exit(1)
