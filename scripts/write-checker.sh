
cd ./demo-writer || exit
npm run write-checker --silent > ../.temp
cd ../inkydraw || exit
python -m inkydraw 400 300 red demo < ../.temp
cd ..
rm .temp
