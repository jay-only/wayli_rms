# build_files.sh
python3.12 -m pip install -r requirements.txt
python3.12 -m pip install --upgrade pip
cd server
python3.12 -m pip list
python3.12 manage.py collectstatic --noinput