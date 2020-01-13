class BMI:
    @staticmethod
    def bmicalc(weight,height):
        a=weight/(height/100)**2
        return float("%.2f" % a)
    @staticmethod
    def BMIcheck(bmi):
        if bmi>=18.5 and bmi<=24.9:
            return "Healty range"
        if bmi<18.5:
            return "Under weight"
        return "Over weight"

    @staticmethod
    def bubble_sort(nlist):
        for i in range(len(nlist)):
            for j in range(0,len(nlist)-i-1):
                if nlist[j]>nlist[j+1]:
                    nlist[j], nlist[j+1] = nlist[j+1], nlist[j]
        return nlist

