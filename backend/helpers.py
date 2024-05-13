import re
from statistics import mean

def calculate_total_seconds(time_list):
    """
    Calculate the total time spent by a user on the application, handling missing values.

    Parameters:
    - time_list (list): List of session times in seconds.

    Returns:
    - float: Total time spent across all sessions.
    """
    # Convert all entries to strings, replace 'nan' with '0', convert to float, and sum up
    total_time = sum(float(re.sub('nan', '0', str(time))) for time in time_list)
    return total_time


def calculate_average_seconds(time_list):
    """
    Calculate the average session time spent by a user on the application, handling missing values.

    Parameters:
    - time_list (list): List of session times in seconds.

    Returns:
    - float: Average session time.
    """
    # Handle cases with all 'nan' to avoid division by zero
    if all(str(time) == 'nan' for time in time_list):
        return 0
    # Process time list to handle 'nan' and calculate mean
    processed_times = [float(re.sub('nan', '0', str(time))) for time in time_list]
    average_time = mean(processed_times)
    return average_time


def count_sessions(time_list):
    """
    Count the number of sessions recorded for a user.

    Parameters:
    - time_list (list): List of session times in seconds.

    Returns:
    - int: Number of sessions.
    """
    return len(time_list)

def compute_unique_actions(actions_list):
    """
    Computes a comma-separated string of unique actions taken by a user, ignoring missing values.

    Parameters:
    - actions_list (list): List of actions taken by the user.

    Returns:
    - str: Comma-separated string of unique actions.
    """
    # Filter out 'nan' values, convert to set for uniqueness, then join into a string
    filtered_actions = set(re.sub('nan', '', str(action)) for action in actions_list)
    unique_actions = ','.join(filtered_actions)
    
    return unique_actions

def count_unique_actions(action_list):
    """
    Calculates the number of unique actions for a user.

    Parameters:
    - action_list (list): List of actions.

    Returns:
    - int: Number of unique actions.
    """
    # Convert session times to a set to eliminate duplicates and count the unique elements
    unique_actions_count = len(set(action_list))
    return unique_actions_count