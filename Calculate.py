# ������Calculate
# ���ܣ�������Ϸ
# ʱ�䣺2018��12��
# ���ߣ�������
class Calculate:
    def __init__(self):
        pass

    def set_a_random(self, matrix):
        import random
        num_kong = 0
        list_kong = []

        for i in range(4):
            for j in range(4):
                if matrix[i][j] == 0:
                    list_kong.append([i, j])
                    num_kong += 1
        if num_kong == 0:
            return False
        num = random.randint(0, num_kong - 1)
        random_num = random.randint(1, 2) * 2

        matrix[list_kong[num][0]][list_kong[num][1]] = random_num
        return matrix

    def up(self, matrix):
        # ѭ������
        # ���
        # ���ŵ�
        temp_score = 0
        for i in range(4):
            # ���ŵ�
            for j in range(4):
                # ������������λ����������һ��
                if j == 0:
                    pass
                else:
                    # �����������ȣ������
                    if matrix[j][i] == matrix[j - 1][i] and matrix[j][i] is not 0:
                        matrix[j - 1][i] += matrix[j][i]
                        matrix[j][i] = 0
                        # �������
                        temp_score += matrix[j - 1][i]

        for i in range(4):
            # ���ŵ�
            for t in range(4):
                for j in range(4):
                    # ���
                    # ���J����������һ��
                    if j == 0:
                        pass
                    else:
                        # �����ƶ�
                        if matrix[j - 1][i] == 0 and matrix[j][i] != 0:
                            matrix[j - 1][i] = matrix[j][i]
                            matrix[j][i] = 0
                            # �����ƶ�֮����Ҫ�ж��ǲ��Ǽ������

                            if matrix[j - 1][i] == matrix[j - 1 - 1][i] and matrix[j - 1][i] is not 0:
                                matrix[j - 1 - 1][i] += matrix[j - 1][i]
                                matrix[j - 1][i] = 0
                                # �������
                                temp_score += matrix[j - 1 - 1][i]

        return temp_score

    def down(self, matrix):
        # ѭ������
        # ���
        # ���ŵ�
        temp_score = 0
        for i in range(4):
            # ���ŵ�
            for j in range(4):
                # ������������λ����������һ��
                if j == 3:
                    pass
                else:
                    # �����������ȣ������
                    if matrix[3 - j][i] == matrix[3 - j - 1][i] and matrix[3 - j][i] != 0:
                        matrix[3 - j][i] += matrix[3 - j - 1][i]
                        matrix[3 - j - 1][i] = 0
                        temp_score += matrix[3 - j][i]

        for i in range(4):
            # ���ŵ�
            for t in range(4):
                for j in range(4):
                    # ���
                    # ���J����������һ��
                    if j == 3:
                        pass
                    else:
                        # �����ƶ�
                        if matrix[j + 1][i] == 0 and matrix[j][i] != 0:
                            matrix[j + 1][i] = matrix[j][i]
                            matrix[j][i] = 0
                            # +1 ����ΪԪ�ؽ�����λ��
                            if matrix[3 - j + 1][i] == matrix[3 - j - 1 + 1][i] and matrix[3 - j + 1][i] != 0:
                                matrix[3 - j + 1][i] += matrix[3 - j - 1 + 1][i]
                                matrix[3 - j - 1 + 1][i] = 0
                                temp_score += matrix[3 - j + 1][i]
        return temp_score

    def left(self, matrix):
        # ѭ������
        # ���
        # ���ŵ�
        temp_score = 0
        for j in range(4):
            # ���ŵ�
            for i in range(4):
                # ������������λ����������һ��
                if i == 0:
                    pass
                else:
                    # �����������ȣ������
                    if matrix[j][i] == matrix[j][i - 1] and matrix[j][i] != 0:
                        matrix[j][i - 1] += matrix[j][i]
                        matrix[j][i] = 0
                        temp_score += matrix[j][i - 1]

        for j in range(4):
            # ���ŵ�
            for t in range(4):
                for i in range(4):
                    # ���
                    # ���I����������һ��
                    if i == 0:
                        pass
                    else:
                        # �����ƶ�
                        if matrix[j][i - 1] == 0 and matrix[j][i] != 0:
                            matrix[j][i - 1] = matrix[j][i]
                            matrix[j][i] = 0

                            if matrix[j][i - 1] == matrix[j][i - 1 - 1] and matrix[j][i - 1] != 0:
                                matrix[j][i - 1 - 1] += matrix[j][i - 1]
                                matrix[j][i - 1] = 0
                                temp_score += matrix[j][i - 1 - 1]
        return temp_score

    def right(self, matrix):
        # ѭ������
        # ���
        # ���ŵ�
        temp_score = 0
        for j in range(4):
            # ���ŵ�
            for i in range(4):
                # ������������λ����������һ��
                if i == 3:
                    pass
                else:
                    # �����������ȣ������
                    if matrix[j][3 - i] == matrix[j][3 - i - 1] and matrix[j][3 - i] != 0:
                        matrix[j][3 - i - 1] += matrix[j][3 - i]
                        matrix[j][3 - i] = 0
                        temp_score += matrix[j][3 - i - 1]

        for j in range(4):
            # ���ŵ�
            for t in range(4):
                for i in range(4):
                    # ���
                    # ���I����������һ��
                    if i == 3:
                        pass
                    else:
                        # �����ƶ�
                        if matrix[j][i + 1] == 0 and matrix[j][i] != 0:
                            matrix[j][i + 1] = matrix[j][i]
                            matrix[j][i] = 0

                            if matrix[j][3 - i + 1] == matrix[j][3 - i - 1 + 1] and matrix[j][3 - i + 1] != 0:
                                matrix[j][3 - i - 1 + 1] += matrix[j][3 - i + 1]
                                matrix[j][3 - i + 1] = 0
                                temp_score += matrix[j][3 - i - 1 + 1]
        return temp_score


if __name__ == '__main__':
    temp = Calculate().up(matrix=[[0, 0, 0, 0], [4, 0, 0, 0], [2, 0, 0, 0], [2, 0, 0, 0]])
