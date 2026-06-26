# 🌸 ORASI v1.1 ⚔️
An ultra-modern, high-concurrency network reconnaissance engine and real-time CVE mapping utility. Engineered to combine robust low-level socket handshakes with an elite, minimalist terminal presentation interface.

## 🛠️ System Architecture & Engineering
Unlike traditional sequential auditing utilities, Orasi relies on a sophisticated **Dual-Engine Execution Model**:
* **High-Speed Threaded Concurrency:** Leverages Python's `concurrent.futures` implementation to orchestrate thread-locked socket connection workers, reducing total network mapping latency across complex subnet targets from minutes to seconds.
* **Pass-Through Shell Orchestration:** Intercepts system process pipelines to cleanly inject advanced low-level firewall evasion parameters (such as MTU fragmentation, data length padding, and randomized decoy routing) without disturbing local execution integrity.

## 🎨 User Interface & The "Edo Premium Slant" Aesthetic
The terminal interface has been heavily optimized for scannability and professional presentation, moving away from cluttered, box-heavy terminal outputs:
* **The Slant Typography Branding:** Features a crisp, left-aligned standard ASCII typographic slant logo engineered for uniform presentation across all modern Linux terminal emulators.
* **Asymmetric Sakura Canopy:** Features a beautifully balanced right-margin TrueColor (`\033[38;2;...m`) cherry blossom cluster layout (🌸 🍃).
* **Samurai Blade Delimiter:** Implements an elegant katana indicator accent line (`═══⚔════►`) acting as a crisp structural separator between the system branding banner and functional operational telemetry grids.
* **The "Kyoto Minimalist" Matrix:** Open ports are rendered using clean, line-free layout spacing on a vertical pipeline axis (`│`) with sharp micro-indicators (`✦`), directly matching Nmap's scannability while adding a unique custom aesthetic.

## 🚀 Live Visuals & Interface Profile
<img width="1895" height="768" alt="Screenshot_2026-06-26_15_10_13" src="https://github.com/user-attachments/assets/c9f43bec-4c0e-44e1-b039-b3120bc4f01b" />



## 📊 Feature Metrics & Hardening
* **Network Jitter Resilience:** Calibrated with a dedicated 2.5–3.0 second socket timeout mechanism, specifically optimized to reliably pass target connection streams over unstable or high-latency OpenVPN routing layers.
* **Automated Parameter Parsing:** Includes an integrated operational dashboard accessible via native CLI syntax flags (`-h` / `--help`).
* **Passive Vulnerability Database:** Features a lightweight local validation dictionary that parses detected application service banners against known security risks in real-time, instantly flagging exposures directly inside the data layout.

## 💻 Operational Execution Examples
Ensure you execute infrastructure scanning tasks with elevated context (`sudo`) when calling raw socket manipulations or low-level SYN mechanisms:

```bash
# Trigger a fast, stealth reconnaissance sweep against a targeted infrastructure asset
sudo python3 orasi.py -sS -O --min-rate 500 10.49.169.61

# Execute a network scan utilizing random decoy targets and custom data length padding
sudo python3 orasi.py -D RND:5 --data-length 25 10.49.169.61
