import statistics   


# def funcName(parameter1, parameter2):
# print ("this is a dummy function")
# return 10

def display_main_menu():
    print("Enter some numbers separated by comas (eg. 2,3,4,5)")
def calc_average(num_list):
    average = sum(num_list)/len(num_list)
    return average

def find_min_max(num_list):
    max_temp = max(num_list)
    min_temp = min(num_list)
    min_max_list = [min_temp, max_temp]
    return min_max_list

def get_user_input():
    user_input = input()
    str_list = user_input.split(",")
    float_list = [float (num.strip()) for num in str_list]
    return float_list
def sort_temperature(num_list):
    assending_temp = sorted(num_list)
    return assending_temp


def median_temperature(sorted_list):
    median_temp = statistics.median(sorted_list)
    return median_temp

    
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print("the numbers ",num_list)

    print("average temp = ",calc_average(num_list))
    print("min_max_temp = ",find_min_max(num_list))
    print("assending = ", sort_temperature(num_list))
    sorted_list = sort_temperature(num_list)
    print("The median is ", median_temperature(sorted_list))


if __name__ == "__main__":
    main()