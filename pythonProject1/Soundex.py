import fuzzy

class Soundex:
    def soundex(self, token):
        dic = {}
        soundex = fuzzy.Soundex(4)
        for word in token:
                dic.setdefault(soundex(word), []).append(word)
        return dic

    def get_soundex(self, word,dict):
        dic = {}
        soundex = fuzzy.Soundex(4)

        dic.setdefault(soundex(word), word)
        key_list = list(dic.keys())
        val_list = list(dic.values())
        p = val_list.index(word)

        for key, value in dict.items():
            if key_list[p] == key:
                return value

        return val_list[p]

    def get_soundexQuery(self,q_tokens,soundex_dic):
        t = []
        q = []
        for word in q_tokens:

            a = self.get_soundex(word, soundex_dic)
            for w in a:
                z = self.get_levenshtein_distance(w, word)

                if z < 2:
                    q.append(w)

        return q


    def get_levenshtein_distance(self,word1, word2):
        matrix = [[0 for x in range(len(word2) + 1)] for x in range(len(word1) + 1)]

        for x in range(len(word1) + 1):
            matrix[x][0] = x
        for y in range(len(word2) + 1):
            matrix[0][y] = y

        for x in range(1, len(word1) + 1):
            for y in range(1, len(word2) + 1):
                if word1[x - 1] == word2[y - 1]:
                    matrix[x][y] = min(
                        matrix[x - 1][y] + 1,
                        matrix[x - 1][y - 1],
                        matrix[x][y - 1] + 1
                    )
                else:
                    matrix[x][y] = min(
                        matrix[x - 1][y] + 1,
                        matrix[x - 1][y - 1] + 1,
                        matrix[x][y - 1] + 1
                    )

        return matrix[len(word1)][len(word2)]

