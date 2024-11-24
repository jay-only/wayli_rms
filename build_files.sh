# build_files.sh
pip install -r requirements.txt
cd server
python3.9 manage.py collectstatic --noinput