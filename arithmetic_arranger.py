def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems"

    arranged_problems = {'top': [], 'bottom': [], 'line': [], 'answer': []}

    for problem in problems:
        num1, operator, num2 = problem.split()

        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'"

        if not num1.isdigit() or not num2.isdigit():
            return "Error: Numbers must only contain digits"

        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits"

        width = max(len(num1), len(num2)) + 2
        arranged_problems['top'].append(num1.rjust(width))
        arranged_problems['bottom'].append(operator + num2.rjust(width - 1))
        arranged_problems['line'].append('-' * width)

        if show_answers:
            result = str(eval(problem))
            arranged_problems['answer'].append(result.rjust(width))

    arranged_output = ''
    for row in ['top', 'bottom', 'line', 'answer']:
        arranged_output += '    '.join(arranged_problems[row]) + '\n'

    return arranged_output

# Example usage:
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
