### Polæ Dash 

The first time you use this repo, in the root folder (/dash), run:

```
python -m venv .env
source .env/bin/activate
pip3 install -r requirements.txt

ipython kernel install --user --name=.venv
```

To run a notebook: 

```
jupyter notebook consensus.ipynb
```


You will only need to do this once. 

When you return to the project, be sure to activate your virtual environment.

```
source .env/bin/activate
```


UI THEMES

USE THE CODE BELOW IF YOU'D LIKE TO CHANGE YOUR JUPYTER THEME:
```
!pip install jupyterthemes
!jt -l #lists available themes
!jt -t onedork #choose your own theme if you'd like. may require restarting kernel
```



