# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 20:10:38 2021
https://github.com/big-data-europe/docker-hbase
https://tecadmin.net/install-apache-hive-on-centos-rhel/
https://tecadmin.net/steps-to-install-java-on-centos-5-6-or-rhel-5-6/
@author: Bishop
"""

# import happybase

# connection = happybase.Connection('172.16.16.222')
# table = connection.table('employees')

from impala.dbapi import connect

# from pyhive import presto  # or import hive or import trino
# cursor = presto.connect('172.16.16.222').cursor()

# cursor.execute('SELECT * FROM demo1 LIMIT 10')
# print(cursor.fetchone())
# print(cursor.fetchall())



# try:
#     transport = TSocket.TSocket('localhost', 10000)
#     transport = TTransport.TBufferedTransport(transport)
#     protocol = TBinaryProtocol.TBinaryProtocol(transport)
 
#     client = ThriftHive.Client(protocol)
#     transport.open()
 
#     client.execute("CREATE TABLE r(a STRING, b INT, c DOUBLE)")
#     client.execute("LOAD TABLE LOCAL INPATH '/path' INTO TABLE r")
#     client.execute("SELECT * FROM r")
#     while (1):
#       row = client.fetchOne()
#       if (row == None):
#         break
#       print row
#     client.execute("SELECT * FROM r")
#     print client.fetchAll()
 
#     transport.close()
 
# except Thrift.TException, tx:
#     print '%s' % (tx.message)