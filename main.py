def add(a, b):
    return a + b


def add_tax(amount, tax_rate):
    return amount + (amount * tax_rate / 100)


if __name__ == "__main__":
    print("Sum:", add(10, 5))
    print("With tax:", add_tax(100, 15))