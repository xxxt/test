import curses
from random import randrange, choice
from collections import defaultdict



# ord() 函数以一个字符作为参数，返回参数对应的 ASCII 数值，便于和后面捕捉的键位关联
letter_codes = [ord(ch) for ch in 'WASDRQwasdrq']
actions_dict = dict(zip(letter_codes, actions * 2))

def init():
    '''初始化'''
    return 'Game'

def not_game():
    '''展示游戏结束页面，读取用户输入得到 action，判断是重启游戏还是结束游戏'''
    responses = defaultdict(lambda: state)
    responses['Restart'], responses['Exit'] = 'Init', 'Exit'
    return responses[action]

def game():
    '''画出当前棋盘状态，读取用户输入得到 action '''
    if action == 'Restart':
        return 'Init'
    if action == 'Exit':
        return 'Exit'
    if 成功移动了一步:
        if 游戏胜利了:
            return 'Win'
        if 游戏失败了:
            return 'Gameover'
    return 'Game'



state_actions = {
    'Init': init,
    'Win': lambda: not_game('Win')
    'Gameover': lambda: not_game('Gameover')
    'Game': game
}

state = 'Init'

while state != 'Exit':
    state = state_actions[state]()

def main(stdscr):
    def init():
        return 'Game'
    
    def not_game(state):
        '''画出 Gameover 或者 Win 的界面，读取用户输入得到action ，判断是游戏重启还是游戏结束'''
        responses = defaultdict(lambda: state)
        responses['Restart', 'Exit'] = 'Init', 'Exit'
        return responses[action]

    def game():
        if action == 'Restart':
            return 'Init'
        if action == 'Exit':
            return 'Exit'
        # if 成功移动了一步:
            if 游戏胜利了:
                return 'Win'
            if 游戏失败了:
                return 'Gameover'
        return 'Game'

    state_actions = {
            'Init': init,
            'Win': lambda: not_game('Win'),
            'Gameover': lambda: not_game('Gameover'),
            'Game': game
    }

    state = 'Init'

    # 状态机开始循环
    while state != 'Exit':
        state = state_actions[state]()
    
    def get_user_action(keyboard):
        char = 'N'
        while char not in actions_dict:
            char = keyboard.getch()
        return actions_dict[char]