### 更改Mellanox卡端口类型

> 默认情况下，Mellanox端口配置为Infiniband端口，但是您可以选择将其转换为以太网端口。


为了使这些更改正常工作，已配置的端口必须连接到与端口配置匹配的网络交换机。换句话说，如果端口配置设置为Infiniband，则外部交换机应该是具有相应Infiniband电缆的Infiniband交换机。同样，如果端口配置设置为以太网，则交换机也应为以太网。

##### 下载Mellanox软件工具
> DGX OS 4.x 自带mst工具，不能再次安装
1. 下载[http://www.mellanox.com/downloads/MFT/mft-4.6.0-48-x86_64-deb.tgz](http://www.mellanox.com/downloads/MFT/mft-4.6.0-48-x86_64-deb.tgz)。
2. 解压缩下载的软件包。
3. 切换到下载目录 mft-4.6.0-48-x86_64-deb / 然后运行安装脚本。
```
install.sh
```
##### 启动Mellanox软件工具
1. 启动MST驱动程序：
``` 
sudo mst start
```
2. 确定当前端口配置
```
ibv_devinfo | grep -e "hca_id\|link_layer" 
```
   - 以下输出指示为InfiniBand配置了端口。
```
hca_id：mlx5_1 link_layer：InfiniBand 
hca_id：mlx5_0 link_layer：InfiniBand
```
   - 以下输出表明端口已配置为以太网。
```
hca_id: mlx5_1  link_layer:  Ethernet 
hca_id: mlx5_0  link_layer:  Ethernet 
```

##### 将端口从InfiniBand切换到以太网
1. 将端口配置更改为以太网。
```
sudo mlxconfig -y -d /dev/mst/mt4115_pciconf0 set LINK_TYPE_P1=2
```
2. 确认已应用配置更改。
```
sudo mlxconfig query |grep -e "LINK_TYPE\|PCI\ device" 
```
```
输出结果： PCI device: /dev/mst/mt4115_pciconf0 LINK_TYPE_P1 ETH(2)
```
3. 重新启动系统
4. 当系统重启后，请确认端口为以太网。 
```
ibv_devinfo |grep -e "hca_id\|link_layer" 

输出结果： hca_id: mlx5_0  link_layer:  Ethernet 
```

##### 将端口从以太网切换到InfiniBand

1. 将端口配置更改为Infiniband。
```
sudo mlxconfig -y -d /dev/mst/mt4115_pciconf0 set LINK_TYPE_P1=1 
```
2. 确认已应用配置更改。

```
sudo mlxconfig query |grep -e "LINK_TYPE\|PCI\ device"
输出结果：PCI device: /dev/mst/mt4115_pciconf0 LINK_TYPE_P1 IB(1)

```
3. 重新启动系统
4. 当系统重启后，请确认端口为Infiniband。
```
ibv_devinfo |grep -e "hca_id\|link_layer" 
输出结果： hca_id: mlx5_0 link_layer: InfiniBand
```