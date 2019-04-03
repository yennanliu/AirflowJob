# XBot
> A POC project that automate various jobs by Airflow. The jobs including Spark python/Java, ML, IG bot, and customized daily routines.

## Tech 
- Programming : Python 3, Java, Shell 
- Framework   : Airflow, Spark, InstaPy, scikit-learn, Keras 
- dev-op      : Docker, Travis  

## File structure

```bash
# .
# ├── Dockerfile             : Dockerfile define astro airflow env 
# ├── Dockerfile_dev         : Dockerfile dev file 
# ├── README.md
# ├── airflow_quick_start.sh : commands help start airflow 
# ├── clean_airflow_log.sh   : clean airflow job log / config before reboost airflow
# ├── dags                   : airflow job main scripts 
# ├── ig                     : IG job scripts 
# ├── install_pyspark.sh     : script help install pyspark local 
# ├── packages.txt           : packages for astro airflow in system level 
# ├── plugins                : plugins help run airflow jobs 
# ├── populate_creds.py      : script help populate credential (.creds.yml) to airflow 
# ├── requirements.txt       : packages for astro airflow in python  level 
# ├── .creds.yml             : yml save creds access services (slack/s3/...) 

```


### Prerequisites
- Copy [.creds.yml.dev](https://github.com/yennanliu/XBot/blob/master/.creds.yml.dev) as `.creds.yml` file then input your credential in it.

### Quick Start (Airflow)
- [Airflow quick start](https://github.com/yennanliu/XBot/blob/master/doc/airflow_quick_start.md)

### Quick Start (Astronomer Airflow)
- There is an issue when run Spark job via Astro airflow, feel free to leave a [ PR ](https://github.com/yennanliu/XBot/pulls)for that 🙏
- [Astro Airflow quick start ](https://github.com/yennanliu/XBot/blob/master/doc/astro_airflow_quick_start.md)

### Docker Deploy 
- dev 

### CI/CD 
- Travis CI (Legacy Services Integration)
- https://travis-ci.org/yennanliu/XBot/builds

### Development 
- dev 
