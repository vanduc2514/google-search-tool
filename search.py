
from dataclasses import asdict
import logging
import sys
import json

from utils import get_args, read_keywords, now_as
from engine import GoogleEngine
from excel import ExcelReporter

# Read the arguments
args = get_args()

# Debug Logging ?
if args.debug:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

# Read keywords
if args.keyword_stdin:
    keyword_in = sys.stdin
else:
    keyword_in = open(args.keyword_path, "rt")
keywords = read_keywords(keyword_in)

# 1. Call Google Custom Search API
engine = GoogleEngine(api_key=args.api_key,
                      cse_id=args.cse_id,
                      limit=args.search_limit,
                      exact_search=args.exact_search)
search_results = engine.search_keywords(keywords, args.search_sites.split(","))
logging.debug(f'Search Results:\n {search_results}')

# 2. Excel Report
if args.excel_path and args.excel_sheetname:
    logging.info(
        f"Export Search Result to Excel Workbook {args.excel_path} with {args.excel_sheetname}")
    excel_reporter = ExcelReporter(workbook_path=args.excel_path,
                                   sheet_name=args.excel_sheetname)
    excel_reporter.export_results(search_results)
else:
    # Write the search result to json
    JSON_OUT = f"search_results_{now_as('%Y-%m-%d_%H-%M-%S')}.json"
    logging.info(f"Export Search Result to {JSON_OUT}")
    with open(JSON_OUT, 'w') as f:
        serialized_results = [asdict(result) for result in search_results]
        json.dump(serialized_results, f, indent=4, sort_keys=True)
