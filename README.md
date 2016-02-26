# pfrock-demos

demos for 微服务mock服务 using python. https://github.com/knightliao/pfrock
    
       _ (`-.            _  .-')                          .-. .-')
      ( (OO  )          ( \( -O )                         \  ( OO )
     _.`     \   ,------.,------.  .-'),-----.    .-----. ,--. ,--.
    (__...--''('-| _.---'|   /`. '( OO'  .-.  '  '  .--./ |  .'   /
     |  /  | |(OO|(_\    |  /  | |/   |  | |  |  |  |('-. |      /,
     |  |_.' |/  |  '--. |  |_.' |\_) |  |\|  | /_) |OO  )|     ' _)
     |  .___.'\_)|  .--' |  .  '.'  \ |  | |  | ||  |`-'| |  .   \
     |  |       \|  |_)  |  |\  \    `'  '-'  '(_'  '--'\ |  |\   \
     `--'        `--'    `--' '--'     `-----'    `-----' `--' '--'
     
## demo

### install pfrock

    pip install pfrock==0.2.1.dev12

### run demo
    
    cd demos/demo
    pfrockpy

结果

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
    [D 2016-02-26 23:54:34,590 pfrock.core MainThread routes:74] add : (u'/api1/people2', <class 'pfrock_static_plugin.handlers.file.FrockStaticFileHandler'>, {'path': u'mocks/static/a.json', 'methods': []})
    [D 2016-02-26 23:54:34,590 pfrock.core MainThread routes:74] add : (u'/api1/(.*)', <class 'pfrock_static_plugin.handlers.dir.FrockStaticDirHandler'>, {'path': u'mocks/static', 'methods': []})
    [D 2016-02-26 23:54:34,590 pfrock.core MainThread routes:74] add : (u'/api2/people', <class 'pfrock_static_plugin.handlers.file.FrockStaticFileHandler'>, {'path': u'mocks/static/b.json', 'methods': []})
    [D 2016-02-26 23:54:34,590 pfrock.core MainThread routes:74] add : (u'/api2/people', <class 'pfrock_static_plugin.handlers.file.FrockStaticFileHandler'>, {'path': u'mocks/static/a.json', 'methods': []})
    [D 2016-02-26 23:54:34,591 pfrock.core MainThread routes:74] add : (u'/api3/(.*)', <class 'pfrock_static_plugin.handlers.dir.FrockStaticDirHandler'>, {'path': u'mocks/static', 'methods': []})
    [D 2016-02-26 23:54:34,592 pfrock.core MainThread routes:74] add : (u'/api', <class 'mocks.handler.hello_world.HelloWorldHandler'>, {u'query': u'1!', u'handler': u'mocks.handler.hello_world.HelloWorldHandler', 'methods': [u'GET'], u'pageno': 1})
    [D 2016-02-26 23:54:34,592 pfrock.core MainThread routes:74] add : (u'/api/persistence', <class 'mocks.handler.persistence.PersistenceHandler'>, {u'query': u'1!', u'handler': u'mocks.handler.persistence.PersistenceHandler', 'methods': [u'GET'], u'pageno': 1})
    [D 2016-02-26 23:54:34,595 pfrock.core MainThread routes:74] add : (u'.*', <class 'pfrock_proxy_plugin.proxy.ProxyHandler'>, {'header_host': u'tieba.baidu.com', 'proxy_url': u'http://tieba.baidu.com', 'methods': []})
    [I 2016-02-26 23:54:34,595 pfrock.core MainThread __init__:19] started server 8888 with autoreload mode

### 配置文件

    {
      "servers": [
        {
          "port": 8888,
          "routes": [
            {
              "path": "/api1/(.*)",
              "handler": "pfrock_static_plugin",
              "options": {
                "routes": [
                  {
                    "path": "people2",
                    "file": "mocks/static/a.json"
                  },
                  {
                    "dir": "mocks/static"
                  }
                ]
              }
            },
            {
              "path": "/api2/people",
              "handler": "pfrock_static_plugin",
              "options": {
                "file": "mocks/static/b.json"
              }
            },
            {
              "path": "/api2/people",
              "handler": "pfrock_static_plugin",
              "options": {
                "file": "mocks/static/a.json"
              }
            },
            {
              "path": "/api3/(.*)",
              "handler": "pfrock_static_plugin",
              "options": {
                "dir": "mocks/static"
              }
            },
            {
              "path": "/api",
              "methods": [
                "GET"
              ],
              "handler": "pfrock_http_plugin",
              "options": {
                "handler": "mocks.handler.hello_world.HelloWorldHandler",
                "query": "1!",
                "pageno": 1
              }
            },
            {
              "path": "/api/persistence",
              "methods": [
                "GET"
              ],
              "handler": "pfrock_http_plugin",
              "options": {
                "handler": "mocks.handler.persistence.PersistenceHandler",
                "query": "1!",
                "pageno": 1
              }
            },
            {
              "path": ".*",
              "methods": "any",
              "handler": "pfrock_proxy_plugin",
              "options": {
                "url": "http://tieba.baidu.com",
                "host": "tieba.baidu.com"
              }
            }
          ]
        }
      ]
    }


- /api1/(.*)
- /api2/people
- 


