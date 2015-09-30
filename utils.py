def fizz_buzz(visit_cnt):
    """
    Simple Algorighm
    3, 5, 15 times problem
    """
    if visit_cnt == 0:
        return '0'
    if visit_cnt % 15 == 0:
        return 'FizzBuzz'
    elif visit_cnt % 5 == 0:
        return 'Buzz'
    elif visit_cnt % 3 == 0:
        return 'Fizz'
    else:
        return visit_cnt