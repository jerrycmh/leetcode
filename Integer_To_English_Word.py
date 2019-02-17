class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if not num:
            return 'Zero'
        
        one_ten = {
            1: 'One',
            2: 'Two',
            3: 'Three',
            4: 'Four',
            5: 'Five',
            6: 'Six',
            7: 'Seven',
            8: 'Eight',
            9: 'Nine'
        }
        
        ten_twenty = {
            10: 'Ten',
            11: 'Eleven',
            12: 'Twelve',
            13: 'Thirteen',
            14: 'Fourteen',
            15: 'Fifteen',
            16: 'Sixteen',
            17: 'Seventeen',
            18: 'Eighteen',
            19: 'Nineteen'
        }
        
        tens = {
            2: 'Twenty',
            3: 'Thirty',
            4: 'Forty',
            5: 'Fifty',
            6: 'Sixty',
            7: 'Seventy',
            8: 'Eighty',
            9: 'Ninety'
        }
        
        def two_digit(num):
            if not num:
                return ''
            if num < 10:
                return one_ten[num]
            if num < 20:
                return ten_twenty[num]
            if num >= 20:
                tenner = num//10
                rest = num - tenner * 10
                if rest:
                    return tens[tenner] + ' ' + one_ten[rest]
                else:
                    return tens[tenner]
        
        def three_digit(num):
            hundred = num // 100
            rest = num - hundred * 100
            if hundred and rest:
                return one_ten[hundred] + ' Hundred ' + two_digit(rest)
            elif not hundred and rest:
                return two_digit(rest)
            elif hundred and not rest:
                return one_ten[hundred] + ' Hundred'
        
        billion = num // 1000000000
        million = (num - billion * 1000000000) // 1000000
        thousand  = (num - billion * 1000000000 - million * 1000000) // 1000
        rest = (num - billion * 1000000000 - million * 1000000 - thousand * 1000)
        
        result = ''
        if billion:
            result += three_digit(billion) + ' Billion'
        if million:
            if result: result += ' '
            result += three_digit(million) + ' Million'
        if thousand:
            if result: result += ' '
            result += three_digit(thousand) + ' Thousand'
        if rest:
            if result:
                result += ' '
            result += three_digit(rest)
        return result