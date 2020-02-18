### 离线使用NGC
大致步骤：
  - 通过有网络连接的系统获得镜像包
  - 通过USB等方式拷贝到离线系统上


1. 在具有Internet访问的系统上，通过输入以下命令和凭据登录到NGC：
```
$ docker login nvcr.io
Username: $oauthtoken 
Password: apikey
```
2. 输入docker pull命令，指定镜像地址，镜像存储库和tag：
```
$ docker pull nvcr.io/nvidia/repository:tag
```
3. 使用`docker images`验证镜像在您的系统上
4. 将Docker映像另存为文件：
```
docker save nvcr.io/nvidia/repository:tag > framework.tar
```
5. 使用USB闪存驱动器等可移动介质将图像传输到离线系统。
6. 加载NVIDIA Docker映像：
```
docker load –i framework.tar
```
7. 验证映像在您的系统上。
```
docker images
```