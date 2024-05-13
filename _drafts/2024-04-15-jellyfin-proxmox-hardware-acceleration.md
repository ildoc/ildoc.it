---
title: Proxmox, Jellyfin dentro docker dentro LXC container e accelerazione hardware
date: 2024-04-15 11:54:00
tags: proxmox jellyfin docker
---

Per ottimizzare la transcodifica dei media, ho voluto addendtrarmi nei settings di [accelerazione hardware di Jellyfin](https://jellyfin.org/docs/general/administration/hardware-acceleration/).

Subito però si è palesato il primo problema: Jellyfin attualmente gira in un LXC container sul mio Proxmox, e da interfaccia grafica non c'è modo di fare il passthrougt della scheda video

https://github.com/gma1n/LXC-JellyFin-GPU

https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html

https://www.alteredtech.io/posts/Docker-Jellyfin-HWA/
