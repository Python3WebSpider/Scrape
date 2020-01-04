cd source
DIR=`ls .`
for dir in ${DIR};do
	if [ -d ${dir} ];then
		echo $dir
		cd $dir
		npm install
		npm run build
		cd ..
	fi
done