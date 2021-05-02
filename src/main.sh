# exit when any command fails
set -e

# run cogent mnist CLI script
python src/main.py $1 $2 $3 $4

# run simple http server
# to view results in a browser
python -m http.server 8000
