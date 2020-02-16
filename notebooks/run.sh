DIR=$(cd `dirname $0` && pwd)
jupyter notebook --notebook-dir=$DIR --no-browser --ip=0.0.0.0
