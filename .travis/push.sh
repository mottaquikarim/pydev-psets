#!/bin/sh

setup_git() {
  echo "IN setup_git"
  git config --global user.email "travis@travis-ci.org"
  git config --global user.name "Travis CI"
  echo "DONE setup_git"
}

commit_to_git() {
  echo "IN commit_to_git"
  git init
  git remote add origin https://${GH_TOKEN}@github.com/mottaquikarim/pydev-psets.git
  git fetch
  git checkout -f $TRAVIS_BRANCH 
  git pull

  python watch.py

  git add .
  git commit --message "Travis build: $TRAVIS_BUILD_NUMBER [ci skip]"
  echo "DONE commit_to_git"
}

push_to_git() {
  echo "IN push_to_git"
  echo ${GH_TOKEN}
  echo https://${GH_TOKEN}@github.com/mottaquikarim/pydev-psets.git
  git push --quiet --set-upstream origin $TRAVIS_BRANCH
  echo "DONE push_to_git"
}

setup_git || true
commit_to_git || true
push_to_git || true
EXIT_CODE=$?

exit ${EXIT_CODE}

# commit_files() {
#   git checkout master
#   git add .
#   git commit --message "Travis build: $TRAVIS_BUILD_NUMBER"
# }

# upload_files() {
#   git remote add origin https://$GH_TOKEN@github.com/mottaquikarim/pydev-psets
#   git push --quiet --set-upstream origin master 
# }

# setup_git
# commit_files
# upload_files