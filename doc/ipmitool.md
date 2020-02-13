### ipmitool工具
> **ipmitool** 是一种可用在 linux 系统下的命令行方式的 ipmi 平台管理工具


> **IPMI与BMC**
> 智能平台管理接口 (IPMI) 是一种开放标准的硬件管理接口规格，定义了嵌入式管理子系统进行通信的特定方法。IPMI 信息通过基板管理控制器 (BMC)（位于 IPMI 规格的硬件组件上）进行交流。
> **BMC**: 基板管理控制器（BMC），可让您独立于CPU或操作系统来管理和监视服务器主机。您可以通过与IPMI端口的以太网连接来远程访问BMC。
##### 安装ipmitool
1. ubuntu 安装
```
sudo apt install ipmitool
```
2. centos 安装
```shell
yum  -y install epel-release
yum  -y install ipmitool
```
##### 启用ipmitool内核模块


启用ipmi内核模块，在不重启系统的情况下使用ipmitool工具

```
modprobe ipmi_si
modprobe ipmi_devintf
```
> 通过重启系统可自动启用内核模块


##### ipmitool使用



- 列出用户
```
ipmitool user list 1
```
- 添加用户
```
ipmitool user set name <user id> <username>
```
- 查看用户权限
```
ipmitool channel getaccess 1 3
```
- 设置用户权限
```
ipmitool channel setaccess [ChannelNo] <user id>[callin=on|off] [ipmi=on|off] [link=on|off] [privilege=level]

# ipmitool channel setaccess 1 3 callin=off ipmi=on link=onprivilege=4
```
- 设置用户密码
```
ipmitool user set password <user id> <password>

# ipmitool user set password 3 123456
```
- 启用/禁用用户
```
ipmitool user enable/disable <user id>

# ipmitool disable user 3
```
> 禁用用户后登入会报错：Invalid Authentication（无效认证）

- 列出 IPMI 网络信息
```
ipmitool lan print [ChannelNo]

#ipmitool lan print 
```
- 修改IP为静态还是DHCP模式
```
ipmitool lan set <ChannelNo> ipsrc<static/dhcp>

# ipmitool lan set 1 ipsrc dhcp #修改为DHCP模式
```
- 配置BMC静态IP
```
sudo ipmitool lan set 1 ipsrc static #配置第一个通道为静态IP 
sudo ipmitool lan set 1 ipaddr  10.31.241.190 #配置IP地址
sudo ipmitool lan set 1 netmask  255.255.255.0 #配置子网掩码
sudo ipmitool lan set 1 defgw ipaddr  10.31.241.1 #配置网关地址
```

- SDR，Sensor信息查看
```
ipmitool sdr
ipmitool sensor list   #可以获得传感器ID号
ipmitool sensor get "CPU PVCCIO"    #其中"CPUPVCCIO"是ID号，即传感器的名称
```

- 查看BMC硬件信息
```
ipmitool mc info
```
- BMC重新启动
```
ipmitool mc reset <warm|cold>  # warm表示软重启；cold表示硬重启
```