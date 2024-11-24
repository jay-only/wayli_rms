# build_files.sh
sudo apt update
sudo apt install sqlite3 libsqlite3-dev

python3.12 -m pip install -r requirements.txt
python3.12 -m pip install --upgrade pip
cd server
python3.12 -m pip list
python3.12 manage.py makemigrations
python3.12 manage.py migrate

python3.12 manage.py collectstatic --noinput