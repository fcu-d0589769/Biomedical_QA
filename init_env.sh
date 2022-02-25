# /bin/bash
if ! type java &> /dev/null ; then
    apt-get install -y default-jre default-jdk
fi
if [ ! -d "/usr/local/spark" ]; then
	wget https://dlcdn.apache.org/spark/spark-3.0.3/spark-3.0.3-bin-hadoop2.7.tgz && \
	tar -xvf spark-3.0.3-bin-hadoop2.7.tgz && \
	mv spark-3.0.3-bin-hadoop2.7 /usr/local/spark
fi
echo "環境初始化完畢"