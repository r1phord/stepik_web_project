sudo rm /etc/nginx/sites-enabled/default
sudo ln -s /home/box/web/etc/nginx.conf /etc/nginx/sites-enabled/default
sudo /etc/init.d/nginx restart

sudo gunicorn --bind 0.0.0.0:8080 hello:wsgi
#sudo ln -s /home/box/web/etc/gunicorn.conf /etc/gunicorn.d/default
#sudo /etc/inid.d/gunicorn restart
