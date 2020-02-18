### 在Linux/MAC上创建可引导的系统U盘

Windows系统参考 [在Windows上创建可引导的系统U盘](create-bootable-usb-win.md)

> **注意**：请备份U盘数据
> **注意**：此操作将格式化U盘
> **注意**：U盘容量至少为8GB
1. [获取系统安装镜像](get-os-iso.md)([获取DGX OS安装镜像](get_dgxos.md))
2. 将USB闪存驱动器插入Linux系统的USB端口之一。
3. 通过运行`lsblk`命令获取USB闪存驱动器的设备名称。
   在以下示例中，USB闪存驱动器的设备名称为 sde
```
~$ lsblk
NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
sda      8:0    0   1.8T  0 disk 
|_sda1   8:1    0   121M  0 part /boot/efi
|_sda2   8:2    0   1.8T  0 part /
sdb      8:16   0   1.8T  0 disk 
|_sdb1   8:17   0   1.8T  0 part 
sdc      8:32   0   1.8T  0 disk 
sdd      8:48   0   1.8T  0 disk 
sde      8:64   1   7.6G  0 disk 
|_sde1   8:65   1   7.6G  0 part /media/Gen
~$

```
5. 以root用户身份，将镜像转换并复制到USB闪存驱动器。

    if为系统镜像；of为U盘(sde)
```
sudo dd if=path-to-software-image bs=2048 of=usb-drive-device-name
```