---
id: core-hardware
type: telemetry
category: host
created_at: 2026-09-16T09:45:00+05:30
tags:
  - hardware
  - telemetry
  - asus-tuf
---

# 🖥️ Hardware Telemetry Matrix

## Physical Infrastructure
- **Machine**: [[ASUS_TUF_F15]]
- **CPU**: Intel Core i5-10300H (4C/8T, up to 4.50 GHz Turbo)
- **Memory**: 16 GB DDR4 RAM (15.5 GiB physical, 4.0 GiB swap)
- **Storage**: 512 GB High-Speed NVMe SSD (`/dev/nvme0n1p2`)
- **Graphics**:
  - iGPU: Intel CometLake-H GT2 (UHD Graphics 630)
  - dGPU: NVIDIA GeForce GTX 1650 Mobile (4096 MiB VRAM)

## Operating Environment
- **OS**: Arch Linux (rolling release, kernel 7.2.2-arch1-1 SMP PREEMPT_DYNAMIC)
- **Compositor**: [[Hyprland_Compositor]]
- **Terminals**: `foot` (Wayland primary), `kitty`
- **Shell**: `fish` (interactive), `bash` (system execution)
- **Remote Bridge**: [[Ultron_Web_Hub]] on port 7777 / 7778 / 7779
