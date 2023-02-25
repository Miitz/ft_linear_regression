import sys
try:
    import thetas
    theta0 = thetas.theta0
    theta1 = thetas.theta1
except:
    import ft_training
    import thetas
    theta0 = thetas.theta0
    theta1 = thetas.theta1


mileage = input("Please enter mileage: ")

try:
    if int(mileage) < 0:
        raise Exception()
    prediction = theta0 + theta1 * int(mileage)
    print(f"The predicted price is: {round(prediction, 0)}")
except:
    print("Error: please verify your input!")
    sys.exit(1)
