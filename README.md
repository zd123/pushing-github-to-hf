---
title: Syncing Github To Huggingface
emoji: 📚
colorFrom: yellow
colorTo: red
sdk: streamlit
sdk_version: 1.45.0
app_file: app.py
pinned: false
license: mit
short_description: syncing-github-to-huggingface
---

# Linking and Pushing Github Repo to Huggingface Space

### Create HuggingFace Space. 
* Do NOT clone the HuggingFace Space's repo locally. 
* Just copy contents of its README.md file


### Create a GitHub repo
* DO clone the GitHub repo locally

### Edit your Github README.md file with the contents of your HF Space README.md file 

### Develop your app locally. 
Must have:
* requirements.txt 
* app.py  
* README.md <-- MUST START WITH with HuggingFace formatting (the stuff between the two --- at the top))

### Add, commit, and push to github
* Dont push any api keys... 
* If using any api keys, add them to your HF_SPACE secrets via the huggingface space web site.

### Linking Github to HF
Get URL of your huggingface space 
```bash
https://huggingface.co/spaces/HF_USERNAME/SPACE_NAME

https://huggingface.co/spaces/KingZack/syncing-github-to-huggingface
```


### Set Github remote to your HuggingFace space

```bash
git remote add space https://huggingface.co/spaces/KingZack/syncing-github-to-huggingface```
```

### Push what is in your Github to HuggingFace

```bash
git push --force space main
```


### FIN :) 
* Dont forget, everytime you push to github you also have to push to huggingface by doing:
```git push --force space main```