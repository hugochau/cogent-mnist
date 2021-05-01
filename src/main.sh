# exit when any command fails
set -e

# run script
python src/main.py $1 $2 $3 $4

# run simple http server
python -m http.server 8000
