class NegativeInputError(Exception):
    pass

def cal_area(length,breadth):
    if length>0 and breadth>0:
        area=length*breadth
        return area
    else:
        raise NegativeInputError("negative number provided for area calculation")


cal_area(34,-56)