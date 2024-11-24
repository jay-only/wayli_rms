# build_files.sh
pip3 install -r requirements.txt
cd server
python3 manage.py collectstatic --noinput