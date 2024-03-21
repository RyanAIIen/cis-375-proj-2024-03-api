# build_files.sh

pip install -r requirements.txt

python3 manage.py check
python3 manage.py collectstatic --no-input
python3 manage.py migrate
