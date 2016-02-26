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

#### install pfrock

    pip install pfrock==0.2.1.dev12

#### run demo
    
    cd demos/demo
    pfrockpy

结果

    

### 解析

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





