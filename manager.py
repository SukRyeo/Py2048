# ������main
# ���ܣ�������
# ʱ�䣺2018��12��
# ���ߣ�������

import os
import Calculate
import UI

# ע��UI�齨 ���ɾ�����Ϣ
ui = UI.UI()
calu = Calculate.Calculate()
calu.set_a_random(ui.game_matrix)
global GameOver
GameOver = False
while not GameOver:
    os.system('clear')
    ui.printUI()
    temp = input('\n��������Ĳ������ϣ�w �£�s ��a �ң�d ��\n')
    print(temp)
    # print(ui.game_matrix)
    if temp == 'w':
        score = calu.up(ui.game_matrix)

    elif temp == 's':
        score =calu.down(ui.game_matrix)
    elif temp == 'd':
        calu.right(ui.game_matrix)
    elif temp == 'a':
        calu.left(ui.game_matrix)
    elif temp == 'q':
        break
    else:
        print('����������������룡')
    ui.set_score(score)

    gameover = calu.set_a_random(ui.game_matrix)

    if not gameover:
        break

print('GameOver!')
