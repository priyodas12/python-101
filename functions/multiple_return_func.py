def mul_return_func(a,b,c):
    sum_of_numbers=a+b+c
    mul_of_numbers=a*b*c
    print(f"sum: {sum_of_numbers}, multiplication: {mul_of_numbers}")
    return sum_of_numbers,mul_of_numbers

# returns as tuple
print(mul_return_func(12,89,63))

def generate_marksheet(*args):
    subject_count=0
    total=0
    for marks in args:
        subject_count=subject_count+1
        total+=marks
    average=total/subject_count
    if average>=35:
        grade='PASS'
    else:
        grade='FAIL'
    print(f"\nTotal marks: {total}/{subject_count*100}, Average: {average}, Grade: {grade}")
    return total,average,grade

generate_marksheet(80,67,32)