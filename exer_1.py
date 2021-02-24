def increase_size_tree(size_tree, value ,year):
    init_size = size_tree
    for i in range(year):
        size_tree += value

    string = f"""
        initial size: {init_size}
        increase size value for year: {value}
        year: {year}
        after {year} years: {size_tree}
    """
    return string
    
retorno = increase_size_tree(10, 1.5, 4)
print(retorno)