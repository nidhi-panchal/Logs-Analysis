# Logs Analysis

This project is a reporting tool that prints out reports (in plain text) based on the data in the database.
This reporting tool is a Python program that uses the psycopg2 module to connect to the database.

## Prerequisites

### Getting the Virtual Machine Set Up
1. Install vagrant at https://www.vagrantup.com/
2. Install virtual machine at https://www.virtualbox.org/wiki/Download_Old_Builds_5_1
3. Install and unzip https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip
4. cd into the vagrant directory and use the command __*vagrant up*__ and then __*vagrant ssh*__ in the terminal

### Getting the Data Ready
1. Download the database at https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip and unzip the file
2. cd into the vagrant directory
3. Use the command __*psql -d news -f newsdata.sql*__ in the terminal
   * If this fails, reinstall the virtual machine as it may not be the most current version


## What is Reported:
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Each of the above questions is answered with one sql query with the results printed out in the terminal upon running.

## Running the Program:
1. Download the logsAnalysis.py file
2. Use the command __*python logsAnalysis.py*__ in the terminal

Results will be printed out in the terminal.

## Authors

* Nidhi Panchal - Initial work