# fluentd-deploytools
Step
1.install tools
install fluentd 
td-agent-gem install fluent-plugin-elasticsearch

2.Put your elasticsearch template to es
curl -XPUT -s http://es_host/_template/template_name -d@/etc/td-agent/template.json
or use the python script to put template to es
python elasticserach.py

3.Config
python gmet.py xxx_xxx_xxx  #need the parameter
