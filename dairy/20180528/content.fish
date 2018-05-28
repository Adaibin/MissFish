Deployment
deploy django(sqlite) application with Nginx, gunicon and gevent

install:
pip install gunicon
pip install gevent
yum install nginx

config:
1) 将项目目录放入环境变量PATH
vi /etc/profile
export PATH="$PATH:/mnt/SlwSiteOriginal
source /etc/profile

2) 修改sqlite线程共享
vi /usr/local/lib/python3.5/site-packages/django/db/backends/base/base.py
line 46-47:
def __init__(self, settings_dict, alias=DEFAULT_DB_ALIAS,
             allow_thread_sharing=True):

3) 配置Nginx
vi /etc/nginx/nginx.conf:
server {
        listen       9755;
        server_name  118.126.104.198;

        charset utf-8;

        access_log  /var/log/nginx/access.log;
        error_log  /var/log/nginx/error.log;
        access_log  /var/log/nginx/access.log;

        location /static {
            alias /mnt/SlwSiteOriginal/SlwSite/static;
        }

        location / {
            proxy_pass         http://0.0.0.0:8000/;
            proxy_redirect     off;

            proxy_set_header   Host                 $host;
            proxy_set_header   X-Real-IP            $remote_addr;
            proxy_set_header   X-Forwarded-For      $proxy_add_x_forwarded_for;
            proxy_set_header   X-Forwarded-Proto    $scheme;
        }
}

run:
1) nginx
nginx -c /etc/nginx/nginx.conf
nginx -s reload

2) gunicon
gunicorn --worker-class=gevent SlwSite.wsgi:application


reference:
1) Deploy Flask with Proxy
http://flask.pocoo.org/docs/1.0/deploying/wsgi-standalone/#deploying-proxy-setups
2) Django database connection’s thread-locality
https://docs.djangoproject.com/en/dev/releases/1.4/#database-connection-s-thread-locality
3) deploy
https://code.ziqiangxuetang.com/django/django-nginx-deploy.html
4) gevent
http://www.open-open.com/lib/view/open1405475790571.html
http://www.open-open.com/lib/view/open1409705174822.html
5) django优化
https://blog.csdn.net/u011546806/article/details/45576669
6) Sqlite线程安全
https://blog.csdn.net/ssyyjj88/article/details/51065874
https://www.sqlite.org/faq.html#q6
https://www.sqlite.org/threadsafe.html