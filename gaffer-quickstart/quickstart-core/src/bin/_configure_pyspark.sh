#!/bin/bash -e

if [[ -z "${GAFFER_HOME}" ]];
then
    echo "GAFFER_HOME environment variable not set"
    exit 0
else
    echo "GAFFER_HOME is $GAFFER_HOME"
fi

operationDeclarations="\ngaffer.store.operation.declarations=sparkAccumuloOperationsDeclarations.json,pySparkAccumuloOperationsDeclarations.json,${GAFFER_HOME}/conf/operationDeclarations.json"
pythonSerialisers="\npythonserialiser.declarations=${GAFFER_HOME}/conf/customPysparkSerialisers.json"

HERE=$(pwd)

echo -e "waiting for store.properties" >> $GAFFER_HOME/gaffer.log
while ! [ -f "$GAFFER_HOME/miniaccumulo/store.properties" ];
do
    echo -n "."
    sleep 0.5
done

#echo -e "\ngaffer.store.operation.declarations=${GAFFER_HOME}/conf/operationDeclarations.json" >> $GAFFER_HOME/miniaccumulo/store.properties

echo -e "creating gaffer pyspark properties file at $GAFFER_HOME/miniaccumulo/pyspark.store.properties" >> $GAFFER_HOME/gaffer.log

cp $GAFFER_HOME/miniaccumulo/store.properties $GAFFER_HOME/miniaccumulo/pyspark.store.properties

echo -e $operationDeclarations >> $GAFFER_HOME/miniaccumulo/pyspark.store.properties
echo -e $pythonSerialisers >> $GAFFER_HOME/miniaccumulo/pyspark.store.properties

echo -e "\nPyspark operations loaded"