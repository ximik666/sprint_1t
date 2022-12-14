### Установка виртуального сервера
В качестве основной системы используется [Proxmox](https://www.proxmox.com/en/proxmox-ve).
Развернем внутри нее виртуальную машину в контейнере LXC, в качестве ОС будем использовать Ubuntu 20.04
```
OS: Ubuntu 20.04.5 LTS x86_64
Host: SYS-XXXXXXXX
Kernel: 5.15.35-2-pve
Uptime: 20 hours, 57 mins
Packages: 547 (dpkg)
Shell: bash 5.0.17
Resolution: 1024x768
Terminal: /dev/pts/0
CPU: Intel Xeon E5-2623 v4 (2) @ 3.200GHz
GPU: 06:00.0 ASPEED Technology, Inc. ASPEED Graphics Family
Memory: 1167MiB / 4096MiB
```

После установки основной ОС обновим пакеты и установим минимальный набор необходимого софта
```bash
apt update
apt upgrade
apt dist-upgrade
apt install nano mc htop iftop net-tools
```
