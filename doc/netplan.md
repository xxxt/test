### netplan网络配置（Ubuntu 18.04，DGXOS 4.x）

> 从Ubuntu 18.04（DGX OS 4.x）起，系统默认使用netplan进行网络管理

#### 配置方法
**配置文件**   `/etc/netplan/*.yaml` (`如：/etc/netplan/config.yaml`)
**解析配置并应用**    `sudo netplan apply`

##### 配置为DHCP
要让名为“enp3s0”的接口通过DHCP获取地址，须创建具有以下内容的YAML文件：
```shell
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: true
```
##### 配置为多端口DHCP
现在，许多设备都包含多个网络接口。服务器通常将需要连接到多个网络，并且可能要求通过特定的端口连接到Internet的，尽管它们都提供了有效的网关。

通过为通过DHCP检索的路由指定权重，可以实现DHCP所需的精确路由，这将确保某些路由优先于其他路由。在此示例中，“ enred”优于“ engreen”，因为它具有较高的优先级：
```
network:
  version: 2
  ethernets:
    enred:
      dhcp4: yes
      dhcp4-overrides:
        route-metric: 100
    engreen:
      dhcp4: yes
      dhcp4-overrides:
        route-metric: 200
```


##### 配置为静态IP
要改为设置静态IP地址，请使用`addresses`标签，该标签带有一个IP列表（IPv4或IPv6），以及子网掩码，也可以提供网关和DNS信息：
```shell
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      addresses:
        - 10.10.10.2/24
      gateway4: 10.10.10.1
      nameservers:
          search: [mydomain, otherdomain]
          addresses: [10.10.10.1, 1.1.1.1]
```
##### 连接开放的Wi-Fi网络
Netplan可以方便的连接到开放的无线网络（该网络不受密码保护），只需要定义访问点即可：
```
network:
  version: 2
  wifis:
    wl0:
      access-points:
        opennetwork: {}
      dhcp4: yes
```
##### 连接到WPA个人无线网络
无线设备使用`wifi`标签，并与有线以太网设备共享相同的配置选项。此外必须指定无线接入点的名称和密码：
```
network:
  version: 2
  renderer: networkd
  wifis:
    wlp2s0b1:
      dhcp4: no
      dhcp6: no
      addresses: [192.168.0.21/24]
      gateway4: 192.168.0.1
      nameservers:
        addresses: [192.168.0.1, 8.8.8.8]
      access-points:
        "network_ssid_name":
          password: "**********"
```

##### 在单个接口上使用多个地址
```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
     addresses:
       - 10.100.1.38/24
       - 10.100.1.39/24
     gateway4: 10.100.1.1
```

##### 通过多个网关使用多个地址
假设有多个地址，每个地址都有自己的网关，我们在此不指定gateway4，而是使用子网的网关地址将各个路由配置为0.0.0.0/0（任何地方）。通过对metric值进行调整，以使路由按预期进行。
```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
     addresses:
       - 9.0.0.9/24
       - 10.0.0.10/24
       - 11.0.0.11/24
     #gateway4:    # unset, since we configure routes below
     routes:
       - to: 0.0.0.0/0
         via: 9.0.0.1
         metric: 100
       - to: 0.0.0.0/0
         via: 10.0.0.1
         metric: 100
       - to: 0.0.0.0/0
         via: 11.0.0.1
         metric: 100
```
##### 使用NetworkManager网络管理器
```
network:
  version: 2
  renderer: NetworkManager
```
##### 配置接口绑定bond
通过配置绑定模式来绑定物理接口来实现高可用，以下是使用DHCP获取地址的主动备份绑定的示例：
```
network:
  version: 2
  renderer: networkd
  bonds:
    bond0:
      dhcp4: yes
      interfaces:
        - enp3s0
        - enp4s0
      parameters:
        mode: active-backup
        primary: enp3s0
```
##### 配置网桥
要创建一个由使用DHCP的单个设备组成的非常简单的网桥，请参考：
```
network:
  version: 2
  renderer: networkd
  ethernets:
    enp3s0:
      dhcp4: no
  bridges:
    br0:
      dhcp4: yes
      interfaces:
        - enp3s0
```