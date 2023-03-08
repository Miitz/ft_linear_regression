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
    try:
        mileage = input("Please enter mileage: ")
        if not mileage.lstrip("-").isnumeric():
            raise ValueError("Mileage must be an integer")
        if int(mileage) < 0 or int(mileage) > 2147483647:
            raise ValueError("Mileage value is less than zero or higher than maxint")
        prediction = theta0 + theta1 * int(mileage)
        if prediction < 0:
            raise Exception("Prediction is less than 0.\n"
                            "If you're trying to sell this car you should think about demolish it.\n"
                            "If you're trying to buy this car ... the owner should pay you.")
        print(f"The predicted price is: {round(prediction, 0)}")
        if input("Continue? (yes/no): ") != "yes":
            flag = False
    except Exception as e:
        print(e)
        sys.exit(1)

