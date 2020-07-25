if [ -d 'build' ]; then rm -Rf 'build'; fi
mkdir -p build
cd build

git clone https://github.com/twenty5151/koneko.git

cp ../*.py koneko/koneko
rm koneko/setup.py
mv koneko/koneko/setup.py koneko/
cp ../requirements.txt koneko/

# For reference, doesn't include koneko -> koneko-twitter search and replace
cd koneko
git diff > ../../patch.diff

grep -rl 'koneko' . | grep -v '.git' | xargs sed -i 's/koneko/koneko_twitter/g'
mv koneko koneko_twitter


