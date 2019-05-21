class Count_letter:
    def count_letter(self,string):
        count_char = {}
        for i in string:
            if i in count_char.keys():
                count_char[i] += 1
            else:
                count_char[i] = 1
        return count_char

