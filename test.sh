echo Running Keyword Search test

echo Set Test Environment
# Check if all the required environment variables are set
if [[ -z "$API_KEY" ]] && [[ -z "$CSE_ID" ]]; then
  echo "Error: Required environment variables not set"
  echo "Set the variables API_KEY & CSE_ID for GOOGLE API Key" \
        "and Google Programmable Search Engine ID"
  exit 1
fi

echo Test Read Keyword from keyword_path
python search.py  \
        -a $API_KEY \
        -c $CSE_ID \
        -k keywords.txt

echo Test Read Keyword from stdin
cat keywords.txt | python search.py  \
        -a $API_KEY \
        -c $CSE_ID \
        -i

echo Test Search multiple sites with comma seprated value
cat keywords.txt | python search.py  \
        -a $API_KEY \
        -c $CSE_ID \
        -i \
        -s stackoverflow.com,github.com

echo Test Limit Search Result
cat keywords.txt | python search.py  \
        -a $API_KEY \
        -c $CSE_ID \
        -i \
        -s stackoverflow.com,github.com \
        -l 1

echo Test Exact Search
cat keywords.txt | python search.py  \
        -a $API_KEY \
        -c $CSE_ID \
        -i \
        -s stackoverflow.com,github.com \
        -l 1 \
        -e