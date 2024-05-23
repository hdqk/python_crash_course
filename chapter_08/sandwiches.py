def make_sandwich(*ingredients):
    """prints a summary of the sandwich being made"""
    print("\nYour sandwich contains:")
    for ingredient in ingredients:
        print(f"- {ingredient}")


make_sandwich('ham', 'egg', 'cheese')
make_sandwich('provolone', 'salami')
make_sandwich('bacon')
