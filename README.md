# pfrock-demos

demos for 微服务mock服务 using python. https://github.com/knightliao/pfrock
     
## demo

### install pfrock

    pip install pfrock==0.2.1.a2

### run demo
    
    cd demos/demo
    pfrockpy

运行结果

    knightliao@mynode03:~/tmp/pfrock-demos/demos/demo$ pfrockpy -d
       _ (`-.            _  .-')                          .-. .-')
      ( (OO  )          ( \( -O )                         \  ( OO )
     _.`     \   ,------.,------.  .-'),-----.    .-----. ,--. ,--.
    (__...--''('-| _.---'|   /`. '( OO'  .-.  '  '  .--./ |  .'   /
     |  /  | |(OO|(_\    |  /  | |/   |  | |  |  |  |('-. |      /,
     |  |_.' |/  |  '--. |  |_.' |\_) |  |\|  | /_) |OO  )|     ' _)
     |  .___.'\_)|  .--' |  .  '.'  \ |  | |  | ||  |`-'| |  .   \
     |  |       \|  |_)  |  |\  \    `'  '-'  '(_'  '--'\ |  |\   \
     `--'        `--'    `--' '--'     `-----'    `-----' `--' '--'
    pfrock version 0.2.1.dev16
    [D 2016-02-27 00:12:44,256 pfrock.core MainThread routes:74] add : (u'/api1/people2', <class 'pfrock_static_plugin.handlers.file.FrockStaticFileHandler'>, {'path': u'mocks/static/a.json', 'methods': []})
    [D 2016-02-27 00:12:44,256 pfrock.core MainThread routes:74] add : (u'/api1/(.*)', <class 'pfrock_static_plugin.handlers.dir.FrockStaticDirHandler'>, {'path': u'mocks/static', 'methods': []})
    [D 2016-02-27 00:12:44,257 pfrock.core MainThread routes:74] add : (u'/api2/people', <class 'pfrock_static_plugin.handlers.file.FrockStaticFileHandler'>, {'path': u'mocks/static/b.json', 'methods': []})
    [D 2016-02-27 00:12:44,257 pfrock.core MainThread routes:74] add : (u'/api3/(.*)', <class 'pfrock_static_plugin.handlers.dir.FrockStaticDirHandler'>, {'path': u'mocks/static', 'methods': []})
    [D 2016-02-27 00:12:44,258 pfrock.core MainThread routes:74] add : (u'/api', <class 'mocks.handler.hello_world.HelloWorldHandler'>, {u'query': u'1!', u'handler': u'mocks.handler.hello_world.HelloWorldHandler', 'methods': [u'GET'], u'pageno': 1})
    [D 2016-02-27 00:12:44,258 pfrock.core MainThread routes:74] add : (u'/api/persistence', <class 'mocks.handler.persistence.PersistenceHandler'>, {u'query': u'1!', u'handler': u'mocks.handler.persistence.PersistenceHandler', 'methods': [u'GET'], u'pageno': 1})
    [D 2016-02-27 00:12:44,261 pfrock.core MainThread routes:74] add : (u'.*', <class 'pfrock_proxy_plugin.proxy.ProxyHandler'>, {'header_host': '', 'proxy_url': u'http://www.sov5.com', 'methods': []})
    [I 2016-02-27 00:12:44,261 pfrock.core MainThread __init__:19] started server 8888 with autoreload mode

### demos

- [static-demo](https://github.com/knightliao/pfrock-demos/tree/master/demos/http-demo): 静态服务能力demo 
- [http-demo](https://github.com/knightliao/pfrock-demos/tree/master/demos/http-demo): http服务能力demo
- [proxy-demo](https://github.com/knightliao/pfrock-demos/tree/master/demos/proxy-demo): proxy服务能力demo
- [json-http-demo](https://github.com/knightliao/pfrock-demos/tree/master/demos/json-http-demo): json-rpc服务能力demo
- [demo](https://github.com/knightliao/pfrock-demos/tree/master/demos/demo) : 整合demo
  


