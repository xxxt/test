#### 使用离线镜像(更新DGX-1系统)


创建离线镜像请参阅  [创建离线镜像](dgx-create-aptmirror.md)
##### 前提条件
1. 目标DGX系统已安装，已完成第一次引导过程，并准备使用最新软件包进行更新。

2. USB存储设备已连接到目标DGX服务器。

##### 配置目标系统
1. 为了保持一致性,将存储设备安装在离线系统上`/media/usb/repository`。
2. 配置apt以将文件系统用作文件中的存储库 `/etc/apt/sources.list `通过修改以下几行。
```
deb file:///media/usb/repository/mirror/security.ubuntu.com/ubuntu bionic-security main 
deb file:///media/usb/repository/mirror/security.ubuntu.com/ubuntu bionic-security universe 
deb file:///media/usb/repository/mirror/security.ubuntu.com/ubuntu bionic-security multiverse 
deb file:///media/usb/repository/mirror/archive.ubuntu.com/ubuntu/ bionic main multiverse universe 
deb file:///media/usb/repository/mirror/archive.ubuntu.com/ubuntu/ bionic-updates main multiverse universe
```
3. 配置apt以使用文件中的NVIDIA DGX OS软件包
`/etc/apt/sources.list.d/dgx.list`
```
deb file:///media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic main multiverse restricted universe
```
4. 删除文件 `/etc/apt/sources.list.d/docker.list` 
5. （仅适用于DGX OS版本4.1和更高版本）配置为使用文件中的NVIDIA DGX OS软件包 /etc/apt/sources.list.d/dgx-bionic-r418-cuda10-1-repo.list。
```
deb file:///media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic/ bionic-r418+cuda10.1 main multiverse restricted universe
```
6. 编辑文件 `/etc/apt/preferences.d/nvidia` ,更新Pin参数。
```
Package: * 
#Pin: origin international.download.nvidia.com 
Pin: release o=DGX Server 
Pin-Priority: 600 
```
7. 更新apt储存库，并确认没有错误。
```
sudo apt update 

Get:1 file:/media/usb/repository/mirror/security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB] 
Get:1 file:/media/usb/repository/mirror/security.ubuntu.com/ubuntu bionic-security InRelease [88.7 kB] 
Get:2 file:/media/usb/repository/mirror/archive.ubuntu.com/ubuntu bionic InRelease [242 kB] 
Get:2 file:/media/usb/repository/mirror/archive.ubuntu.com/ubuntu bionic InRelease [242 kB] 
Get:3 file:/media/usb/repository/mirror/archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB] 
Get:4 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1 InRelease [13.0 kB] 
Get:5 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic InRelease [13.1 kB] 
Get:3 file:/media/usb/repository/mirror/archive.ubuntu.com/ubuntu bionic-updates InRelease [88.7 kB] 
Get:4 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1 InRelease [13.0 kB] 
Get:5 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic InRelease [13.1 kB] 
Hit:6 https://download.docker.com/linux/ubuntu bionic InRelease Get:7 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1/multiverse amd64 Packages [10.1 kB] 
Get:8 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1/restricted amd64 Packages [10.3 kB] 
Get:9 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic-r418+cuda10.1/restricted i386 Packages [516 B] 
Get:10 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic/multiverse amd64 Packages [44.5 kB] 
Get:11 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic/multiverse i386 Packages [8,575 B] 
Get:12 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic/restricted i386 Packages [745 B] 
Get:13 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic/restricted amd64 Packages [8,379 B] 
Get:14 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic/universe amd64 Packages [2,946 B] 
Get:15 file:/media/usb/repository/mirror/international.download.nvidia.com/dgx/repos/bionic bionic/universe i386 Packages [496 B] 
Reading package lists... Done 
Building dependency tree 
Reading state information... Done 
249 packages can be upgraded. Run 'apt list --upgradable' to see them. 
```
8. 使用新配置的本地存储库升级系统。
```
sudo apt full-upgrade 
```
