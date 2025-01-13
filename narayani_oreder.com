cd narayani_order
git pull
sudo systemctl daemon-reload
sudo systemctl restart narayani_order.com.gunicorn
exit

git clone https://github.com/9730991252/narayani_order.git
cd narayani_order

********** Create Virtual env *****

virtualenv venv


********** Activate Virtual env ****

source venv/bin/activate


****************migrations******

python3 manage.py makemigrations

*********** migrate ********

python3 manage.py migrate



***** install django ******

pip install django
pip install pillow
pip install django-ckeditor


******** Install Gunicorn ******
 
pip install gunicorn

*********** Deactivate Virtualenv *****

deactivate


************ Create System Socket File for Gunicorn *******

Example:- sudo nano /etc/systemd/system/crenta.in.gunicorn.socket

cd  /etc/systemd/system/

sudo nano narayani_order.com.gunicorn.socket



[Unit]
Description=narayani_order.com.gunicorn socket

[Socket]
ListenStream=/run/narayani_order.com.gunicorn.sock

[Install]
WantedBy=sockets.target


************** Create System Service File for Gunicorn ******
Syntax:- sudo nano /etc/systemd/system/your_domain.gunicorn.service
Example:- sudo nano /etc/systemd/system/narayani_order.com.gunicorn.service

cd  /etc/systemd/system/

sudo nano narayani_order.com.gunicorn.service


[Unit]
Description=narayani_order.com.gunicorn daemon
Requires=narayani_order.com.gunicorn.socket
After=network.target

[Service]
User=root
Group=root
WorkingDirectory=/root/narayani_order
ExecStart=/root/narayani_order/venv/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/narayani_order.com.gunicorn.sock \
          narayani_order.wsgi:application

[Install]
WantedBy=multi-user.target

----------------------------------------------------------------
sudo systemctl start narayani_order.com.gunicorn.socket

sudo systemctl start narayani_order.com.gunicorn.service

-----------------------------------------------------------------

sudo systemctl enable narayani_order.com.gunicorn.socket

sudo systemctl enable narayani_order.com.gunicorn.service

-----------------------------------------------------------------------

sudo systemctl status narayani_order.com.gunicorn.socket

sudo systemctl status narayani_order.com.gunicorn.service

-------------------------------------------

sudo systemctl daemon-reload

sudo systemctl restart narayani_order.com.gunicorn

--------------------------------



****************** Create Virtual Host File ******
Syntax:- sudo nano /etc/nginx/sites-available/your_domain
Example:- sudo nano /etc/nginx/sites-available/crenta.in


cd /etc/nginx/sites-available

sudo nano narayani_order.com



server{
    listen 80;
    listen [::]:80;

    server_name narayaniorder.com www.narayaniorder.com;
    client_max_body_size 500M;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_set_header Host $http_host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_pass http://unix:/run/narayani_order.com.gunicorn.sock;
    }

    
    
}

-----------------------------------------------------


########## Enable Virtual Host or Create Symbolic Link of Virtual Host File ########

sudo ln -s /etc/nginx/sites-available/narayani_order.com /etc/nginx/sites-enabled/narayani_order.com


%%%%%%%%%%%%%%%%%%%%% Check Configuration is Correct or Not %%%%%

sudo nginx -t

%%%%%%%%%%%% Restart Nginx %%%%%%%%%

sudo service nginx restart
-------------------------------------

********** restart ******

sudo systemctl daemon-reload
sudo systemctl restart narayani_order.com.gunicorn

--------------------------------------- ssl ------------------

sudo certbot --nginx -d narayani_order.com -d www.narayani_order.com