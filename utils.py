# 1. Acquire Google API Key from system environment
# 2. Acquire Google Programmable search engine ID from system environment
# 3. Acquire the keywords from stdin or from the arguments -k
# 4. Acquire the excel file output path. If none is given, ignore

import argparse
from datetime import datetime


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug",
                        help="""
                        Whether to enable debug mode, which outputs more detailed information. 
                        Default to False.
                        """,
                        action='store_true',
                        default=False)
    google_group = parser.add_argument_group("google")
    google_group.add_argument("-a", "--api-key",
                              help="API key for accessing the Google Custom Search API.",
                              required=True)
    google_group.add_argument("-c", "--cse-id",
                              help="Custom Search Engine (CSE) identifier to use for the search.",
                              required=True)
    google_group.add_argument("-l", "--search-limit",
                              help="""
                              Maximum number of search results per keyword. 
                              Defaults to 3.
                              """,
                              default=3)
    google_group.add_argument("-e", "--exact-search",
                              help="""
                              Whether to perform an exact phrase match for each keyword. 
                              Default is False.
                              """,
                              action="store_true",
                              default=False)
    google_group.add_argument("-s", "--search-sites",
                              help="""
                              Comma-separated list of site names to search through. 
                              By default, searches all available sites on google.com .
                              """,
                              default="google.com")
    keyword_group = parser.add_mutually_exclusive_group(required=True)
    keyword_group.title = "Keyword"
    keyword_group.add_argument("-k", "--keyword-path",
                               help="""
                               Path to a text file containing keywords to search for. 
                               One keyword per line.
                               """)
    keyword_group.add_argument("-i", "--keyword-stdin",
                               help="""
                               Read the keywords from standard input (stdin) instead of a file.
                               Default to False.
                               """,
                               action='store_true',
                               default=False)
    # If this argument is ignored, output the result to a JSON
    parser.add_argument("-x", "--excel-path",
                        help="""
                        Path to save the search results as an Excel file. 
                        Default output to JSON
                        """)
    parser.add_argument("-n", "--excel-sheetname",
                        help="""
                        Name of sheet inside the Excel file to store the data.
                        Default to Search Result.
                        """,
                        default="Search Result")
    # TODO: print usage / print help
    return parser.parse_args()

# Keywords are store in a txt file. Each lines represent a keyword
# Multiple line keywords are enclosed in "---" symbol.

def read_keywords(keyword_in):
    MULTILINE_MARKER = "---"
    buffer = []
    # Indicate whether the multiline marker
    inside_marker = False
    for line in keyword_in:
        if line.startswith(MULTILINE_MARKER):
            # If we reach the end of marker, append the buffer to keywords
            if inside_marker and buffer:
                yield ''.join(buffer)
            buffer = []
            inside_marker = not inside_marker
        elif inside_marker:
            buffer.append(line)
        else:
            yield line.strip()

def now_as(fmtstr):
    now = datetime.now()
    return now.strftime(fmtstr)