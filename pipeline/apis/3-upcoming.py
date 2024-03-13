#!/usr/bin/env python3

import requests
from datetime import datetime

def get_upcoming_launch():
    """
    Fetches the upcoming launch data from the SpaceX API.

    Returns:
        dict: The data of the upcoming launch.
    """
    # Make a GET request to the SpaceX API to get upcoming launches
    response = requests.get("https://api.spacexdata.com/v4/launches/upcoming")
    # Convert the response to JSON format
    data = response.json()
    # Find the upcoming launch with the earliest date_unix
    upcoming_launch = min(data, key=lambda x: x['date_unix'])
    return upcoming_launch

def format_launch_info(launch):
    """
    Formats the launch information into the specified format.

    Args:
        launch (dict): The data of the launch.

    Returns:
        str: The formatted launch information.
    """
    # Extract relevant information from the launch data
    launch_name = launch['name']
    # Convert the Unix timestamp to UTC datetime and then format it
    launch_date = datetime.utcfromtimestamp(launch['date_unix']).strftime('%Y-%m-%d %H:%M:%S')
    rocket_name = launch['rocket']
    # Check if launchpad information is available
    if 'launchpad' in launch and isinstance(launch['launchpad'], dict):
        launchpad_name = launch['launchpad']['name']
        launchpad_locality = launch['launchpad']['locality']
    else:
        launchpad_name = "Unknown"
        launchpad_locality = "Unknown"
    # Format the information according to the specified format
    formatted_info = "{} ({}) {} - {} ({})".format(launch_name, launch_date, rocket_name, launchpad_name, launchpad_locality)
    return formatted_info

def main():
    """
    Main function to fetch and display the upcoming launch information.
    """
    # Get the upcoming launch data
    upcoming_launch = get_upcoming_launch()
    # Format the launch information
    launch_info = format_launch_info(upcoming_launch)
    # Print the formatted launch information
    print(launch_info)

if __name__ == '__main__':
    main()
