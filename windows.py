CYGWIN64
/cygdrive/c/cygwin64/home/carlos/wom/huawei_nbi/db-register-execution/app-nbi-kafka
$ (cd ../kafka-docker;docker-compose up -d)
$ (cd ../kafka-docker;docker-compose ps)
$ (cd ../kafka-docker;docker-compose stop)
$ docker rm $(docker ps -a -q -f status=exited)
$ docker ps -a
$ ./create-dev-topics.sh

carlos@DESKTOP-NTBDHGL /cygdrive/c/cygwin64/home/carlos/wom/huawei_nbi/kafka-docker
$ docker exec -t kafka-docker_kafka_1 kafka-topics.sh --bootstrap-server :9092 --describe --topic rst_topic

carlos@DESKTOP-NTBDHGL /cygdrive/c/cygwin64/home/carlos/wom/huawei_nbi/kafka-docker
$ docker exec -t kafka-docker_kafka_1 kafka-topics.sh --bootstrap-server :9092 --list

/cygdrive/c/cygwin64/home/carlos/wom/huawei_nbi/db-register-execution/scripts
$ ./delete_volume_mysql.sh
$ ./create_volume_mysql.sh
$ ./stop_mysql.sh
$ ./start_mysql.sh

$ git pull origin db-register-execution

$ tree -a -I ".git|__pycache__|.gitignore" -L 3 -D

MYSQL
# Para entrar a la consola mysql con el usuario testuser
$ docker exec -it mysql-test mysql -u testuser -ptestpassword
mysql> show databases;
mysql> use mytestdb;
mysql> show tables;
mysql> describe file;
mysql> describe result;
mysql> select * from file;
mysql> select * from result;
mysql> select * from result where file_id = '9ee266d5-63e4-4ee0-865a-01d9def35b8b.mml';
mysql> select id, file_id, executed_time_stamp, network_element, o_m_id, retcode, result from result order by executed_time_stamp asc;
mysql> quit

CONDA
# https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/20/conda/
(test36) C:\cygwin64\home\carlos\wom\huawei_nbi\nbi\app-nbi>python kafka_nbi.py
(test36) C:\cygwin64\home\carlos\wom\huawei_nbi\nbi\app-nbi>python kafka_client.py

(test36) C:\cygwin64\home\carlos\wom\huawei_nbi\nbi
> conda -V
> conda update conda
> conda create -n test37 python=3.7 anaconda
>conda deactivate
>conda info --envs
>conda activate test36
>python kafka_nbi.py
>


-----------------------------------------------------------------
CYGWIN64
/cygdrive/c/cygwin64/home/carlos/wom/huawei_nbi

- debo generar requirements.txt

I took files from:
C:\cygwin64\home\carlos\wom\Trash\20200903huawei_nbi\db-register-execution\app-nbi-kafka


C:\cygwin64\home\carlos
linux_mint.py
windows.py
