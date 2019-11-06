#!/usr/bin/env bash
set -e

# config
git config --global user.email "${GH_USER_EMAIL}"
git config --global user.name "${GH_USER_NAME}"
git remote add gh-token "https://${GH_TOKEN}@github.com/ebmm01/machineLearning.git";
git fetch gh-token && git fetch gh-token gh-pages:gh-pages;

git init
git add -A
git commit -m 'deploy'

# if you are deploying to https://<USERNAME>.github.io
# git push -f git@github.com:<USERNAME>/<USERNAME>.github.io.git master

# if you are deploying to https://<USERNAME>.github.io/<REPO>
git push -f git@github.com:ebmm01/machineLearning.git master:gh-pages

echo "Completed deploying documentation"
