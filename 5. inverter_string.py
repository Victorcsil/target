def inverter_string(string):
    inverted_string = ''
    for i in range(len(string)):
        inverted_string += string[-i-1]
    print(inverted_string)

inverter_string('Isso foi meio complexo')
inverter_string('Mas deu certo')
inverter_string('Python é legal')