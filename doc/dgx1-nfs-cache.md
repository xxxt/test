### 配置NFS挂载和缓存

> DGX-1包括四个RAID 0配置的SSD。这些SSD用于应用程序缓存，因此您必须设置自己的NFS驱动器以进行长期数据存储。以下说明描述了如何将NFS挂载到DGX-1上，以及如何使用DGX-1 SSD缓存NFS以提高性能。

> 确保有至少一台NFS服务器，其中包含要由DGX-1访问的数据，并且DGX-1和NFS服务器之间具有网络访问权限。


1. 为DGX-1配置NFS挂载
    1. 编辑文件系统表配置。
    ```
    sudo vi /etc/fstab
    ```
    2. 添加以下内容：
    ```
    <nfs_server>:<export_path> /mnt nfs rw,noatime,rsize=32768,wsize=32768,nolock,tcp,intr,fsc,nofail 0 0
    ```
    - / mnt 这里用作示例挂载点。
    - 请咨询网络管理员以获取<nfs_server>和<export_path>的正确值。
    - 此处提供的挂载参数是基于典型用例的建议值列表。但是必须包含fsc`，因为该参数指定了FS-Cache的使用。
2. 验证NFS服务器是否可访问
```
ping <nfs_server>
```
3. 挂载NFS:
```
sudo mount /mnt
```
4. 确认已启用缓存:
```
cat /proc/fs/nfsfs/volumes
```
FSC=yes

