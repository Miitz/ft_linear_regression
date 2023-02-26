# ft_linear_regression


### *An Introduction to Machine Learning* at 42Roma Luiss

For this project, we will have to create a program that predicts the price of a car<br/>
by using a [linear function] train with a [gradient descent algorithm].

In this project we are free to use whatever language we want.

~~Jupiter Notebook~~ (*Work in progress*) &#8594; ~~[`ft_linear_regression.ipynb`](/ft_linear_regression.ipynb)~~

### Subject
- [ft_linear_regression_subject](/subject/en.subject.pdf)

### Usage

- Clone this repository
    ```bash
    git clone https://github.com/Miitz/ft_linear_regression.git
    ```
- Open a shell in the cloned directory and run the training program `ft_linear_regression.py`
    ```bash
    python3 ft_linear_regression.py
    ```
- Run the prediction program and follow the instructions `prediction.py`
    ```bash
    python3 prediction.py
    ```

### Bonus
Here are some bonus flags you can use while running the training program:
- "-np"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;visualize normalized dataset and solution.
  ```bash
  python3 ft_linear_regression.py -np
  ```
- "-rp"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;visualize real dataset and solution.
  ```bash 
  python3 ft_linear_regression.py -rp
  ```
- "-ep"&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;print thetas after each epoch.
  ```bash
  python3 ft_linear_regression.py -ep
  ```
  
  
[linear function]: <https://en.wikipedia.org/wiki/Linear_function>
[gradient descent algorithm]: <https://en.wikipedia.org/wiki/Gradient_descent>
