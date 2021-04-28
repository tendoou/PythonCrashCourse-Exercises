class MultiCommandParser:
    def __init__(self):
        self.commands = ['apaga', 'apagar',
                         'enciende', 'encender'
                         ]
        self.devices = ['tv', 'aire',
                        'estufa', 'pc',
                        'ventilador', 'calentador']

    def parser(self, order=''):
        words = list(order.split())
        parsed_instruction = []
        for word in words:
            if word in self.commands:
                parsed_instruction.append([word])
            elif word in self.devices:
                current_command = parsed_instruction[-1]
                current_command.append(word)
        return parsed_instruction


order1 = MultiCommandParser()
print(order1.parser('apaga la tv el aire calentador la estufa  y enciende el aire acondicionado la pc y ventilador'))
