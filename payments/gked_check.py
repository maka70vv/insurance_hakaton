class CheckGKED:
    def check_gked_medical(self, gked):
        firstNums = gked.split('.')[0]
        parts = gked.split('.')[:2]
        secondNums = '.'.join(parts)
        if int(firstNums) == 86:
            return True
        elif secondNums == "46.46" or secondNums == "47.73":
            return True
        else:
            return False
