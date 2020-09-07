
## jupyter kernel list

```
jupyter kernelspec list
```

## 删除 kernel

```
jupyter kernelspec remove
```

## 安装 kernel

```
pip install ipykernel
```

## 安装 kernel 并指定名字

```
python -m ipykernel install --user --name=python --display-name py3-64
```

## 设置 jupyter 路径

```
jupyter notebook --generate-config

goto: jupyter_notebook_config.py

find #c.NotebookApp.notebook_dir = '' 
change to >> c.NotebookApp.notebook_dir = '(自己的路径)'
```

## jupyter 自动补全

```
python -m pip install jupyter_contrib_nbextensions
 
jupyter contrib nbextension install --user --skip-running-check
```
