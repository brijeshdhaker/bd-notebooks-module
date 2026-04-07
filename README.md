### Activate Python VENV
```bash

conda activate bash
conda install jupyter -c defaults

```
### jupyter lab
```bash

$ jupyter lab --port=8888 --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --notebook-dir=~/IdeaProjects/bd-notebooks-module/notebooks
```

### jupyter notebook
#
```bash

$ jupyter notebook --port=8888 --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --notebook-dir=${HOME}/IdeaProjects/bd-notebooks-module/notebooks
```


### Check the newly built image
```bash
$ docker run -it --rm jupyter/all-spark-notebook:latest pyspark --version
```

```bash
git reset --soft HEAD~2 # Changes stay in staging
git reset HEAD~2        # Changes become unstaged

```






## Create Zip File
```bash

python -m zipfile -c bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip bd-pyspark-module/src/main/py/*
```

## Run Python __main__.py get executed
```bash

python bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip --Host localhost --App hello_py
````

## Run Python module
```bash

export PYSPARK_DRIVER_PYTHON=/opt/conda/envs/env_python3_11_13/bin/python
export PYSPARK_PYTHON=/opt/conda/envs/env_python3_11_13/bin/python

export PYTHONPATH=$PYTHONPATH:./bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip
# or
export PYTHONPATH=$PYTHONPATH:~/IdeaProjects/bd-pyspark-module/src/main/py
export WORK_DIR=~/IdeaProjects/bd-pyspark-module/src/main/py

python -m com.example.app --Host localhost --App hello_py
python -m com.example.hello --Host localhost --App hello_py
```

# Check the newly built image
```bash

$ docker run -it --rm \
  -e PYSPARK_DRIVER_PYTHON=/opt/conda/bin/python \
  -e PYSPARK_PYTHON=/opt/conda/bin/python \
  brijeshdhaker/python-base:3.11.13 python /apps/bd-pyspark-module-1.0.0.zip --Host localhost --App hello_py
```
```bash

$ docker run -it --rm \
  -e PYSPARK_DRIVER_PYTHON=/opt/conda/bin/python \
  -e PYSPARK_PYTHON=/opt/conda/bin/python \
  brijeshdhaker/python-base:3.11.13 python -m com.example.app --Host localhost --App hello_py
```
```bash

$ docker run -it --rm \
  -e PYSPARK_DRIVER_PYTHON=/opt/conda/bin/python \
  -e PYSPARK_PYTHON=/opt/conda/bin/python \
  brijeshdhaker/python-base:3.11.13 python -m com.example.hello --Host localhost --App hello_py
```

#
```python
import sys
sys.path.insert(0, "/apps/hostpath/python/pyspark-module-distro.zip")
sys.path[0]
import hello
hello.greet("Pythonista")
```

```python
import sys
sys.path.insert(0, "~/IdeaProjects/bd-pyspark-module/src/main/py")
```
# or
```bash

export PYTHONPATH=$PYTHONPATH:${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
export WORK_DIR=${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
/opt/conda/bin/python ~/IdeaProjects/bd-pyspark-module/src/main/py/com/example/kafka/confluent/confluent_kafka_AvroProducer.py
/opt/conda/bin/python ~/IdeaProjects/bd-pyspark-module/src/main/py/com/example/kafka/confluent/confluent_kafka_AvroConsumer.py
/opt/conda/bin/python ~/IdeaProjects/bd-pyspark-module/src/main/py/com/example/utils/FileUtils.py

```

## Import modules in pyspark
```bash

pyspark --archives bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip#
from com.example.models.Transaction import Transaction
from main import print_hi
```

## Run Python Unit Test
```bash

export PYTHONPATH=$PYTHONPATH:${HOME}/IdeaProjects/bd-pyspark-module/target/bd-pyspark-module-1.0.0.zip
export PYTHONPATH=$PYTHONPATH:${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
export WORK_DIR=${HOME}/IdeaProjects/bd-pyspark-module/src/main/py
python -m unittest ${HOME}/IdeaProjects/bd-pyspark-module/src/test/py/TestUsers.py