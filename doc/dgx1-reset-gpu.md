### 重置DGX-1的GPU

> 在维护或修理工作期间，可能需要重置NVIDIA®DGX-1™GPU。例如，当GPU在同一位置出现ECC错误时，需要重置GPU。对于DGX-1平台，无法重置单个GPU，因为它们是通过NVLink链接的，因此必须同时重置所有GPU。

> 重置系统中所有GPU的最简单方法是重新引导系统。如果这破坏性太大，并且您需要保持系统引导，则本节说明如何在不重新引导系统的情况下重置GPU。


#### GPU重置过程

##### 停止运行应用程序和服务
要重置GPU，必须首先关闭在GPU上运行的所有应用程序。NVIDIA提供了一个工具（nvidia-smi）来监视和管理系统上的GPU。该工具可用于检查正在运行的应用程序，然后重置GPU。基本过程如下：
1. 用nvidia-smi检查运行的应用程序。
```
nvidia-smi -q -d PIDS
```
2. 关闭所有列出的应用程序。
```
# 使用 systemctl 或者 kill 关闭应用程序
```
3. 关闭nv-hostengine(仅DGX OS 3.x)
```
sudo nv-hostengine -t
```
4. 停止`nvidia-persistenced`、`nvsm-apis-gpumonitor`、 `nvidia-docker `、`dcgm`

```
sudo systemctl stop nvidia-persistenced
sudo systemctl stop nvsm-apis-gpumonitor 
sudo systemctl stop nvidia-docker 
sudo systemctl stop dcgm 
```
5. 使用systemctl重新启用NVIDIA进程。


#### 重置GPU
1. 运行nvidia-smi命令
```
sudo nvidia-smi -r
```
2. 启用nvidia-persistenced，nvidia-docker以及先前部分中已停止的其他任何监视代理和应用程序。
```
sudo systemctl start nvidia-persistenced 
sudo systemctl start nvsm-apis-gpumonitor
sudo systemctl start nvidia-docker
sudo systemctl start dcgm 
```