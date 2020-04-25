# python-requests-scraping
This repo is my own personal playground for using the `python requests` module and web-scraping.
#
## COVID-19 Graph Visualzations
This is a quick script that can be run to view real-time updated graphs of the current COVID-19 data in any country of your choice. 
## Dependencies 
    requests
    csv
    contextlib 
    matplotlib.pyplot 
    argparse
## How To Run 
    python3 main.py --iso=<iso country code>
## Graph Info
The x-value in the graphs shown are the total number of days since December 31, 2019 (since that is when the data collection began). The graphs that are already included are:
* Total Cases
* New Cases 
* Derivative of Total Cases 
* 2nd Derivative of Total Cases
