import re

def Eliminate_implication(expression):
    x = re.findall(".->.", expression)
    if len(x) == 1:
        expression = re.sub("->", "|", expression)
        expression = "!" + expression
    else:
        # expression1 = expression[:expression.rindex("->") - 1]
        # expression1 = "!" + expression1
        # expression = expression.replace(expression[:expression.rindex("->")],expression1)
        while expression.find("->") != -1:
            expression1 = expression[:expression.rfind("->") - 1]
            expression1 = "!" + expression1
            expression = expression.replace(expression[:expression.rfind("->")], expression1)
            index = expression.rfind("->")
            expression = expression[:index] + "|" + expression[index + len("->"):]

    return expression

text = "!forall p(X) !| q(X)"


def move_negation(expression):
    expression = re.sub("!!","",expression)

    expression = re.sub("!&","|",expression)

    expression = expression.replace("!|","&")

    expression = re.sub("!exists","forall",expression)

    expression = re.sub("!forall","exists",expression)

    return expression


print(move_negation(text))