import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_obj = datetime.fromisoformat(iso_string)
    formatted_date = date_obj.strftime('%A %d %B %Y')
    return formatted_date





def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """

    if isinstance(temp_in_fahrenheit, str):
        temp_in_fahrenheit = float(temp_in_fahrenheit)
        
    temp_in_celcius = (temp_in_fahrenheit - 32)*5/9
    return round(temp_in_celcius, 1)


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
   
    if len(weather_data) == 0:
        return 0
    weather_data_as_floats = [float(value) for value in weather_data]
    total = sum (weather_data_as_floats)
    mean = total/len(weather_data)
    return mean
    # return a number with a decimal place that is the mean of the group of values


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
  
    data = []
    with open(csv_file, 'r') as file:
        #add csv read
        csv_reader = csv.reader(file)
        next(csv_reader)
      
        for line in csv_reader:
            if line == []:
                continue
            else:
                line[1] = int(line[1])
                line[2] = int(line[2])
                data.append(line)
    
    return data

# print("csv data function")
# result = load_data_from_csv("tests/data/example_one.csv")
# print(result)




def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """

    if not weather_data:
        return ()
    
    lowest = float(weather_data[0])
    position = 0

    for index, num in enumerate (weather_data):
        if float(num) <= lowest:
            lowest = float(num)
            position = index

    return (lowest, position)




def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    highest = float(weather_data[0])
    position = 0

    for index, num in enumerate (weather_data):
        if float(num) >= highest:
            highest = float(num)
            position = index

    return (highest, position)


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    # Function returns a string containing the date, max, min and mean temperatures for each date. 
    if not weather_data:
            return ()
    num_days= 0
    for data in weather_data:     
        # print(f"Current data of days : {data}")
        # print(f"Current num of days : {num_days}")
        num_days = num_days +1
        # print(f"Current num of days  after adding 1: {num_days}")
        
    
    for data in weather_data:
        date = convert_date (data[0])
      
    
    
    list_of_mins = []
    for row in weather_data:
        list_of_mins.append(row[1])
    min_temp = find_min(list_of_mins)
    min_temp_celcius = convert_f_to_c(min_temp[0])
    min_temp_index = min_temp[1]
    date_lowest_temp = weather_data[min_temp_index][0]
    min_temp_date = convert_date(date_lowest_temp)
    mean_low = calculate_mean(list_of_mins)
    mean_low_celcius = convert_f_to_c(mean_low)
  
  

    list_of_maxes = []
    for row in weather_data:
        list_of_maxes.append(row[2])
    max_temp = find_max(list_of_maxes)
    max_temp_celcius = convert_f_to_c(max_temp[0])
    max_temp_index = max_temp[1]
    date_highest_temp = weather_data[max_temp_index][0]
    max_temp_date = convert_date(date_highest_temp)
    mean_high = calculate_mean(list_of_maxes)
    mean_high_celcius = convert_f_to_c(mean_high)
    
    return f"{num_days} Day Overview\n  The lowest temperature will be {min_temp_celcius}{DEGREE_SYMBOL}, and will occur on {min_temp_date}.\n  The highest temperature will be {max_temp_celcius}{DEGREE_SYMBOL}, and will occur on {max_temp_date}.\n  The average low this week is {mean_low_celcius}{DEGREE_SYMBOL}.\n  The average high this week is {mean_high_celcius}{DEGREE_SYMBOL}.\n"







   

    
    









    #     min_temp = find_min(data[1:])[0]
    #     print(f"min temp is {min_temp}")
    #     max_temp = find_max(data[1:])[0]
    #     print(f"max temp is {max_temp}")
    #     min_temp_celcius = convert_f_to_c(min_temp)
    #     print(f"min temp in celcius is {min_temp_celcius}")
    #     max_temp_celcius = convert_f_to_c(max_temp)
    #     print(f"max temp celcius is {max_temp_celcius}")
    #     min_temp_index = data[1:].index(min_temp)
    #     print(f"min temp index is {min_temp_index}")
    #     min_temp_date = convert_date(data[0])
    #     print(f"min temp date is {min_temp_date}")
    #     max_temp_index = data[1:].index(max_temp)
    #     print(f"max temp index is {max_temp_index}")
    #     max_temp_date = convert_date(data[0])
    #     print(f"max temp date is {max_temp_date}")
    #     mean_low = calculate_mean([min_temp_celcius])
    #     print(f"mean low is {mean_low}")
    #     mean_high = calculate_mean([max_temp_celcius])
    #     print(f"mean high is {mean_high}")
    #     summary = f"{num_days} Day Overview\nThe lowest temperature will be {min_temp_celcius}{DEGREE_SYMBOL}, and will occur on {min_temp_date}.\nThe highest temperature will be {max_temp_celcius}{DEGREE_SYMBOL}, and will occur on {max_temp_date}.\nThe average low this week will be {mean_low}{DEGREE_SYMBOL}. The average high this week will be {mean_high}{DEGREE_SYMBOL}."
        
        

    # return generate_summary

    
  
example_one = [
            ["2021-07-02T07:00:00+08:00", 49, 67],
            ["2021-07-03T07:00:00+08:00", 57, 68],
            ["2021-07-04T07:00:00+08:00", 56, 62],
            ["2021-07-05T07:00:00+08:00", 55, 61],
            ["2021-07-06T07:00:00+08:00", 53, 62]
        ]

generate_summary(example_one)
    
    # 


def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    if not weather_data:
        return ()
    
    summary = ""
    for row in weather_data:
        formatted_date = convert_date(row[0])
        min_temp_celcius = convert_f_to_c(row[1])
        max_temp_celcius = convert_f_to_c(row[2])
        summary += f"---- {formatted_date} ----\n  Minimum Temperature: {min_temp_celcius}{DEGREE_SYMBOL}\n  Maximum Temperature: {max_temp_celcius}{DEGREE_SYMBOL}\n\n"
    return(summary)

