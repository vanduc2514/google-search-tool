# Running the Google Search Tool

The Google Search tool allows you to search for keywords on Google and export the results to either an Excel file or JSON file. 

## Getting Started

Before running the program, make sure you have Python 3.7+ installed on your machine. Clone this repository to your local machine and navigate to the root directory of the project.

```bash
git clone https://github.com/vanduc2514/google-search-tool.git
cd google-search-tool
```

### Installing Required Libraries

This project requires several third-party libraries to be installed first. To do this, run:

```bash
pip install -r requirements.txt
```

## Usage

To use the program, run `search.py` with parameters from the command line. Here's the basic command syntax:

```bash
python search.py [OPTIONS]
```

### Command Line Options

| Option               | Required? | Description                                                                                                                                                                                                                                                                                                                            |
|----------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `-k`, `--keyword-path` | Yes       | Path to a text file containing keywords to search for. One keyword per line. If `-i` is provided, ignore this argument.                                                                                                                                                                                                                                                    |
| `-s`, `--search-sites` | No        | Comma-separated list of site names to search through. By default, searches all available sites on google.com .                                                                                                                                                                                                                                          |
| `-a`, `--api-key`     | Yes       | API key for accessing the Google Custom Search API.                                                                                                                                                                                                                                                                                      |
| `-c`, `--cse-id`      | Yes       | Programmable Search Engine (CSE) ID to use for the search.                                                                                                                                                                                                                                                                             |
| `-l`, `--search-limit` | No        | Maximum number of search results per keyword. Defaults to 3.                                                                                                                                                                                                                                                                            |
| `-e`, `--exact-search` | No        | Whether to perform an exact phrase match for each keyword. Default is `False`.                                                                                                                                                                                                                                                            |
| `-i`, `--keyword-stdin` | Yes        | Read the keywords from standard input (`stdin`) instead of a file. If `-k` is provided, ignore this argument.                                                                                                                                                                                                                                                                 |
| `-x`, `--excel-path`   | No        | Path to save the search results as an Excel file.                                                                                                                                                                                                                                                                                          |
| `-n`, `--excel-sheetname` | No    | Name of sheet inside the Excel file to store the data.                                                                                                                                                                                                                                                                                       |
| `-d`, `--debug`       | No        | Whether to enable debug mode, which outputs more detailed information. Default is `False`.                                                                                                                                                                                                                                              |

### Example Usage

Here's how you might run `search.py` with some example parameters:

```bash
python search.py \
  --keyword-path my_keywords.txt \
  --search-sites=stackoverflow.com,docs.python.org \
  --api-key my_key \
  --cse-id my_cse_id \
  --exact-search \
  --excel-path my_results.xlsx \
  --excel-sheetname Sheet1 \
  --debug 
```

This would search for each keyword in `my_keywords.txt` on StackOverflow and Python documentation sites only, using the API key `my_key` and CSE ID `my_cse_id`. It would also use exact phrase matching and limit the number of search results to 3 per keyword per site. The resulting search results would be saved to an Excel file named `my_results.xlsx` with a sheet named `Sheet1`. Debug mode would also be enabled.

This tool can also be used with pipe operator `|` to search content of each lines in a file. Use the argument `-i` to select this mode.

```bash
cat my_file | python search.py -i -a my_key -c my_cse_id
```

## Output

The program will output either a JSON file or Excel file, depending on whether the `--excel-path` and `--excel-sheetname` options are provided. If an Excel file is not specified, the program will output a JSON file to the current directory with a filename based on the current date and time.
