import karnaugh as kar


class KarnoCheck:
    def __init__(self, k_map):
        self.result = list()
        self.big_result = list()
        self.kar_map: list = k_map
        self.row = kar.check_row(list(self.kar_map))
        self.square = kar.check_squares(list(self.kar_map))
        self.pairs_v = kar.check_pairs_vertical(list(self.kar_map))
        self.pairs_h_t = kar.check_horiz_pairs_top(self.kar_map)
        self.pairs_h_b = kar.check_horiz_pairs_bottom(self.kar_map)

    def check_karno(self):
        for i in range(len(self.kar_map)):
            for j in range(len(self.kar_map[i])):
                if self.kar_map[i][j] == 1:
                    if self.__check_rows(i):
                        continue
                    elif self.__check_squares(j):
                        continue
                    elif self.__check_pairs_v(j):
                        continue
                    elif self.__check_pairs_h_t(j):
                        continue
                    elif self.__check_pairs_h_b(j):
                        continue
        self.big_result = remove_similar(self.big_result)
        return self.big_result

    def __check_rows(self, i):
        if self.row[i] and i == 0:
            self.result.append('!x1')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.row[i] and i == 1:
            self.result.append('x1')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        return False

    def __check_squares(self, j):
        if (self.square[j] and j == 0) or (self.square[(j // 2) * 2] and j == 1):
            self.result.append('!x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif (self.square[j] and j == 1) or (self.square[j - 1] and j == 2):
            self.result.append('x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif (self.square[j] and j == 2) or (self.square[(j // 2) * 2] and j == 3):
            self.result.append('x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif (self.square[j] and j == 3) or (self.square[j - 1] and j == 3):
            self.result.append('!x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        return False

    def __check_pairs_v(self, j):
        if self.pairs_v[j] and j == 0:
            self.result.append('!x2')
            self.result.append('!x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_v[j] and j == 1:
            self.result.append('!x2')
            self.result.append('x3')
            self.big_result.append(list(self.result))
            return True
        elif self.pairs_v[j] and j == 2:
            self.result.append('x2')
            self.result.append('x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_v[j] and j == 3:
            self.result.append('x2')
            self.result.append('!x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        return False

    def __check_pairs_h_t(self, j):
        if self.pairs_h_t[j] and j == 0:
            self.result.append('!x1')
            self.result.append('!x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_h_t[j] and j == 1:
            self.result.append('!x1')
            self.result.append('x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_h_t[j] and j == 2:
            self.result.append('!x1')
            self.result.append('x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_h_t[j] and j == 3:
            self.result.append('!x1')
            self.result.append('!x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        return False

    def __check_pairs_h_b(self, j):
        if self.pairs_h_b[j] and j == 0:
            self.result.append('x1')
            self.result.append('!x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_h_b[j] and j == 1:
            self.result.append('x1')
            self.result.append('x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_h_b[j] and j == 2:
            self.result.append('x1')
            self.result.append('x2')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        elif self.pairs_h_b[j] and j == 3:
            self.result.append('x1')
            self.result.append('!x3')
            self.big_result.append(list(self.result))
            self.result.clear()
            return True
        return False


def remove_similar(result):
    curr = list()

    for i in result:
        check = 0
        for j in curr:
            if i == j:
                check += 1
        if check == 0:
            curr.append(i)

    return curr
