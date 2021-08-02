from sys import argv
from versionchange import changeVersion
from utils import Tables


actions_classes = {
    'changeversion': {
        'action_name': 'changeversion',
        'action': changeVersion,
        'description': "Muda a versão do PHP instalada em seu dispositivo."
    }
}

def show_actions():
    valid_data = [['Ação', 'Descrição']]
    for action in actions_classes:
        valid_data.append([action, actions_classes.get(action)['description']])
    Tables().load(valid_data)


if not len(argv[1:]):
    show_actions()
else:
    file, argument = argv
    action = actions_classes.get(argument, False)
    if action:
        action['action']()
    else:
        print("A ação não encontrada")
