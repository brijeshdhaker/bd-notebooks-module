### Activate Python VENV
```bash

conda activate bash
conda install jupyter -c defaults

```
### jupyter lab
```bash

$ jupyter lab --port=8888 --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --notebook-dir=~/ideaProjects/bd-notebooks-module/notebooks
```

### jupyter notebook
#
```bash

$ jupyter notebook --port=8888 --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.token='' --notebook-dir=${HOME}/ideaProjects/bd-notebooks-module/notebooks
```


### Check the newly built image
```bash
$ docker run -it --rm jupyter/all-spark-notebook:latest pyspark --version
```

```bash
git reset --soft HEAD~2 # Changes stay in staging
git reset HEAD~2        # Changes become unstaged

```






