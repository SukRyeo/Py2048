# ������UI
# ���ܣ����ɽ������Ϣ��չʾ����
# ʱ�䣺2018��12��
# ���ߣ�������

class UI:

    def __init__(self):
        import time
        self.game_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        self.score = 0
        self.stime = time.time()

    # ����UI���󣬴�ӡUI
    def printUI(self):
        print('------------------------------------')
        print('|' + ('score: ' + str(self.score)).center(16) + '|' + ('time :' + str(self.get_time())).center(16) + '|')
        print('------------------------------------')
        print('\n')
        print('-----------------')
        for i in range(4):
            row = '|'
            for j in range(4):
                if self.game_matrix[i][j] == 0:
                    row += ''.center(3)
                else:
                    row += str(self.game_matrix[i][j]).center(3)
                row += '|'
            print(row)
            print('-----------------')

    def set_game_matrix(self, i, j, num):
        self.game_matrix[i][j] = num

    def get_game_matrix(self, i, j):
        return self.game_matrix[i][j]

    def set_score(self, num):
        self.score += num

    def get_time(self):
        import time
        time = int(time.time() - self.stime)
        s_time = time % 60
        min_time = (time - s_time) * 60
        time = str(min_time).center(2) + '�� ' + str(s_time).center(2) + '��'
        return time


if __name__ == '__main__':
    ui = UI()
    ui.printUI()
