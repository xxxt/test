### 搭建本地apt镜像库
> 本节中的说明将在具有网络访问权限的系统上执行。

#### 创建离线镜像库
##### 前提条件：
1. 需要使用装有Ubuntu OS的系统来创建镜像，因为需要使用多种Ubuntu工具。
2. 系统必须包含足够的存储空间，才能将存储库复制到文件系统。空间需求可能高达250GB。

##### 创建镜像：
1. 确保存储设备已通过网络访问连接到系统，并标识了安装点。 这些说明中使用的示例安装点：`/media/usb/repository`
2. 满足空间要求后，安装apt-mirror软件包。 确保目标目录属于用户apt-mirror所有，否则复制将无法进行。
```
sudo apt update
sudo apt install apt-mirror 
sudo chown apt-mirror:apt-mirror /media/usb/repository 
```
3. 在`/etc/apt/mirror.list`中配置目标目录的路径，并使用下面包含的存储库列表来检索Ubuntu基本OS和NVIDIA DGX OS软件包。
```
############# config ################## 
# 
set base_path /media/usb/repository #/your/path/here 
# 
# set mirror_path $base_path/mirror 
# set skel_path $base_path/skel 
# set var_path $base_path/var 
# set cleanscript $var_path/clean.sh 
# set defaultarch <running host architecture> 
# set postmirror_script $var_path/postmirror.sh 
set run_postmirror 0 
set nthreads 20 
set _tilde 0 
# 
############# end config ############## 
# Standard Canonical package repositories: 
deb http://security.ubuntu.com/ubuntu bionic-security main 
deb http://security.ubuntu.com/ubuntu bionic-security universe 
deb http://security.ubuntu.com/ubuntu bionic-security multiverse 
deb http://archive.ubuntu.com/ubuntu/ bionic main multiverse universe 
deb http://archive.ubuntu.com/ubuntu/ bionic-updates main multiverse universe 
# 
deb-i386 http://security.ubuntu.com/ubuntu bionic-security main 
deb-i386 http://security.ubuntu.com/ubuntu bionic-security universe 
deb-i386 http://security.ubuntu.com/ubuntu bionic-security multiverse 
deb-i386 http://archive.ubuntu.com/ubuntu/ bionic main multiverse universe 
deb-i386 http://archive.ubuntu.com/ubuntu/ bionic-updates main multiverse universe 
# 
# DGX specific repositories: 
deb http://international.download.nvidia.com/dgx/repos/bionic bionic main restricted universe multiverse 
deb http://international.download.nvidia.com/dgx/repos/bionic bionic-updates main restricted universe multiverse 
deb http://international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1 main multiverse restricted universe 
# 
deb-i386 http://international.download.nvidia.com/dgx/repos/bionic bionic main restricted universe multiverse 
deb-i386 http://international.download.nvidia.com/dgx/repos/bionic bionic-updates main restricted universe multiverse 
# Only for DGX OS 4.1.0 
deb-i386 http://international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1 main multiverse restricted universe 
# Clean unused items 
clean http://archive.ubuntu.com/ubuntu 
clean http://security.ubuntu.com/ubuntu
```
4. 运行apt-mirror，然后等待其完成下载。花费时间时长由网络连接速度决定。
    ```sudo apt-mirror```
5. 弹出可移动存储。
   ```sudo eject /media/usb/repository ```


