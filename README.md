# 自制的python版本的socket.io

> 你们为什么不出个python 版本代号666的socket.io呢？？ 非得让我喷！！气人


## 开发节奏

- 先看engine.io 源码和了解背后逻辑
https://github.com/veaba/engine.io


- socket.io 协议 https://github.com/socketio/engine.io-protocol

- engine.io-pasrser https://github.com/learnboost/engine.io-parser

- engine.io-client https://github.com/learnboost/engine.io-client

- engine.io https://github.com/learnboost/engine.io

- 再看socket.io 源码和了解背后设计逻辑

- 再了解node 版本的socket.io 

- 接下来是python 的http

- 以及python 的socket

- 还有 python 的websocket

- HTTP 协议 HTTP1.1 HTTP2.0  HTTPS socket

- 利用Python 搭建HttpServer https://www.jianshu.com/p/279473392f38

## python 创建基本的http服务

```python
from http.server import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8000

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

    #Handler for the GET requests
    def do_GET(self):
        print(111,self)
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write(bytes("Hello World !",encoding='utf-8'))
        return

try:
    server = HTTPServer(('', PORT_NUMBER), myHandler)
    print('Started httpserver on port ' , PORT_NUMBER)

    #Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print('^C received, shutting down the web server')
    server.socket.close()
```

## node 版本的socket.io方法

- checkRequest: [Function],
- serveClient: [Function],
- set: [Function],
- checkNamespace: [Function],
- path: [Function],
- adapter: [Function],
- origins: [Function],
- attach: [Function],
- listen: [Function],
- initEngine: [Function],
- attachServe: [Function],
- serve: [Function],
- serveMap: [Function],
- bind: [Function],
- onconnection: [Function],
- of: [Function],
- close: [Function],
- setMaxListeners: [Function],
- getMaxListeners: [Function],
- emit: [Function],
- addListener: [Function],
- on: [Function],
- prependListener: [Function],
- once: [Function],
- prependOnceListener: [Function],
- removeListener: [Function],
- off: [Function],
- removeAllListeners: [Function],
- listeners: [Function],
- rawListeners: [Function],
- listenerCount: [Function],
- eventNames: [Function],
-  to: [Function],
- in: [Function],
- use: [Function],
- send: [Function],
- write: [Function],
- clients: [Function],
- compress: [Function],
- binary: [Function] }

## 原生python 内置的socket

- AF_APPLETALK
- AF_DECnet
- AF_INET
- AF_INET6
- AF_IPX
- AF_IRDA
- AF_SNA
- AF_UNSPEC
- AI_ADDRCONFIG
- AI_ALL
- AI_CANONNAME
- AI_NUMERICHOST
- AI_NUMERICSERV
- AI_PASSIVE
- AI_V4MAPPED
- AddressFamily
- AddressInfo
- CAPI
- EAGAIN
- EAI_AGAIN
- EAI_BADFLAGS
- EAI_FAIL
- EAI_FAMILY
- EAI_MEMORY
- EAI_NODATA
- EAI_NONAME
- EAI_SERVICE
- EAI_SOCKTYPE
- EBADF
- EWOULDBLOCK
- INADDR_ALLHOSTS_GROUP
- INADDR_ANY
- INADDR_BROADCAST
- INADDR_LOOPBACK
- INADDR_MAX_LOCAL_GROUP
- INADDR_NONE
- INADDR_UNSPEC_GROUP
- IPPORT_RESERVED
- IPPORT_USERRESERVED
- IPPROTO_ICMP
- IPPROTO_IP
- IPPROTO_RAW
- IPPROTO_TCP
- IPPROTO_UDP
- IPV6_CHECKSUM
- IPV6_DONTFRAG
- IPV6_HOPLIMIT
- IPV6_HOPOPTS
- IPV6_JOIN_GROUP
- IPV6_LEAVE_GROUP
- IPV6_MULTICAST_HOPS
- IPV6_MULTICAST_IF
- IPV6_MULTICAST_LOOP
- IPV6_PKTINFO
- IPV6_RECVRTHDR
- IPV6_RECVTCLASS
- IPV6_RTHDR
- IPV6_TCLASS
- IPV6_UNICAST_HOPS
- IPV6_V6ONLY
- IP_ADD_MEMBERSHIP
- IP_DROP_MEMBERSHIP
- IP_HDRINCL
- IP_MULTICAST_IF
- IP_MULTICAST_LOOP
- IP_MULTICAST_TTL
- IP_OPTIONS
- IP_RECVDSTADDR
- IP_TOS
- IP_TTL
- IntEnum
- IntFlag
- MSG_BCAST
- MSG_CTRUNC
- MSG_DONTROUTE
- MSG_MCAST
- MSG_OOB
- MSG_PEEK
- MSG_TRUNC
- MSG_WAITALL
- MsgFlag
- NI_DGRAM
- NI_MAXHOST
- NI_MAXSERV
- NI_NAMEREQD
- NI_NOFQDN
- NI_NUMERICHOST
- NI_NUMERICSERV
- RCVALL_MAX
- RCVALL_OFF
- RCVALL_ON
- RCVALL_SOCKETLEVELONLY
- SHUT_RD
- SHUT_RDWR
- SHUT_WR
- SIO_KEEPALIVE_VALS
- SIO_LOOPBACK_FAST_PATH
- SIO_RCVALL
- SOCK_DGRAM
- SOCK_RAW
- SOCK_RDM
- SOCK_SEQPACKET
- SOCK_STREAM
- SOL_IP
- SOL_SOCKET
- SOL_TCP
- SOL_UDP
- SOMAXCONN
- SO_ACCEPTCONN
- SO_BROADCAST
- SO_DEBUG
- SO_DONTROUTE
- SO_ERROR
- SO_EXCLUSIVEADDRUSE
- SO_KEEPALIVE
- SO_LINGER
- SO_OOBINLINE
- SO_RCVBUF
- SO_RCVLOWAT
- SO_RCVTIMEO
- SO_REUSEADDR
- SO_SNDBUF
- SO_SNDLOWAT
- SO_SNDTIMEO
- SO_TYPE
- SO_USELOOPBACK
- SocketIO
- SocketKind
- SocketType
- TCP_MAXSEG
- TCP_NODELAY
- _GLOBAL_DEFAULT_TIMEOUT
- _GiveupOnSendfile
- _LOCALHOST
- _LOCALHOST_V6
- __all__
- __builtins__
- __cached__
- __doc__
- __file__
- __loader__
- __name__
- __package__
- __spec__
- _blocking_errnos
- _intenum_converter
- _realsocket
- _socket
- create_connection
- dup
- errno
- error
- errorTab
- fromfd
- fromshare
- gaierror
- getaddrinfo
- getdefaulttimeout
- getfqdn
- gethostbyaddr
- gethostbyname
- gethostbyname_ex
- gethostname
- getnameinfo
- getprotobyname
- getservbyname
- getservbyport
- has_ipv6
- herror
- htonl
- htons
- inet_aton
- inet_ntoa
- inet_ntop
- inet_pton
- io
- ntohl
- ntohs
- os
- selectors
- setdefaulttimeout
- socket
- socketpair
- sys
- timeout