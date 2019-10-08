# -*- coding: UTF-8 -*-
"""PyBoss Homework Solution."""

# Import required packages
import csv
import os
from datetime import datetime
import re

# Files to load and output (Remember to change these)
file_to_load = os.path.realpath("D:/Git/GWU-ARL-DATA-PT-09-2019-U-C/02-Homework/03-Python/Instructions/Part-3/PyBoss/employee_data.csv")
file_to_output = os.path.realpath("D:/Git/MChinchilla_GW_HW/03_HW_MC/python-challenge/PyBoss/output.txt")

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

# Placeholders for re-formatted contents
emp_ids = []
emp_first_names = []
emp_last_names = []
emp_dobs = []
emp_ssns = []
emp_states = []

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as emp_data:
    reader = csv.reader(emp_data)

    header = next(reader)

    # Loop through each row, re-grab each field and store in a new list
    for row in reader:
        
        # Grab emp_ids and store it into a list
        emp_ids = emp_ids + [row[0]]

        # Grab names, split them, and store them in a temporary variable
        split_name = row[1].split(" ")

        # Then save first and last name in separate lists
        emp_first_names.append(split_name[0])
        emp_last_names.append(split_name[1])

        # Grab DOB and reformat it
        olddate = datetime.strptime(row[2], "%Y-%m-%d")
        newdate = datetime.strftime(olddate, "%m/%d/%Y")

        # Then store it into a list
        emp_dobs.append(newdate)

        # Grab SSN and reformat it
        newssn = re.sub("[0-9]+-[0-9]+-", "***-**-", row[3])
                
        # Then store it into a list
        emp_ssns.append(newssn)

        # Grab the states and use the dictionary to find the replacement
        for key, value in us_state_abbrev.items():
        # sub item for item's paired value in string
            if row[4] == key:
                newstate = value
        
        # Then store the abbreviation into a list
        emp_states.append(newstate)

# Zip all of the new lists together
zipped = zip(emp_ids, emp_first_names, emp_last_names, emp_dobs, emp_ssns, emp_states)
zipped = list(zipped)

# Write all of the election data to csv
with open(file_to_output, "w") as txt_file:
    for lines in zipped:
        re.sub("[)]", "", str(lines))
        re.sub("[(]", "", str(lines))
        re.sub("[']", "", str(lines))
        txt_file.write(str(f"{lines}\n"))
        print(zipped)