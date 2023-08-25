echo "BUILD STARTED"
python3.9 -m pip install -r requirements.txt
echo "INSTALLATION COMPLETED... COLLECTING STATIC FILES"
python3.9 manage.py collectstatic --noinput --clear
echo "BUILD FINISHED"