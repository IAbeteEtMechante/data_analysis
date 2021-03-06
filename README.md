# kaggle-template
Template to quickly get started on Kaggle competitions. 

**To get started:**
```
git clone https://github.com/alhankeser/kaggle-template my-kaggle-competition
virtualenv env
source env/bin/activate
pip install -r requirements.txt
kaggle kernels pull -p scripts -m kaggleuser/kernel-name
rm -rf .git
git init
git remote add origin https://github.com/my-username/my-repo
git add .
git commit -m "Initial setup"
git push -u origin master
cd input
kaggle competitions download -c kaggle-competition-slug
cd ../notebooks
jupyter notebook
```
