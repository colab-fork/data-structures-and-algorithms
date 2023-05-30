class Solution(object):
    def calPoints(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        ops = operations
        final = []
        for i in ops:
            if i.isdigit() or (i[0] == '-' and i[1:].isdigit()):
                final.append(int(i))
            else:
                final.append(i)
        record = []
        for i in final:
            if i == 'C':
                last = record[-1]
                record.remove(last)
            elif i == '+':
                last = record[-1]
                second_last = record[-2]
                record.append(last+second_last)
            elif i =='D':
                last = record[-1] * 2
                record.append(last)
            else:
                record.append(i)
        return sum(record)
