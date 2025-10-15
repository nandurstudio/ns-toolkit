# NS Toolkit: Mesh Cleanup Pro

*Professional 5-in-1 mesh optimization toolkit for Blender 4.2+*

[![Version](https://img.shields.io/badge/Version-1.0.0-blue.svg)](https://github.com/your-username/ns-toolkit)
[![Blender](https://img.shields.io/badge/Blender-4.2+-orange.svg)](https://www.blender.org/)
[![License](https://img.shields.io/badge/License-GPL%203.0+-green.svg)](LICENSE_GPL.txt)

## 🚀 Quick Start

1. **Install**: Download from [Blender Extensions](https://extensions.blender.org/) or [Gumroad](https://gumroad.com/)
2. **Enable**: Preferences → Add-ons → Enable "NS Toolkit: Mesh Cleanup Pro"
3. **Use**: 3D Viewport → N-Panel → NS Toolkit tab

## ✨ Features

- **Real-Time Topology Highlighting** - Instantly visualize N-gons and triangles across your scene
- **Smart Triangles to Quads** - Advanced conversion with optimized algorithms
- **Merge by Distance** - Intelligent vertex cleanup for cleaner topology  
- **Recalculate Normals** - Fix lighting issues with proper normal direction
- **Reset Transform Vectors** - Clean up transform data for better performance

## 📁 Project Structure

```
ns-toolkit/
├── 📁 assets/           # Images, icons, and visual resources
├── 📁 development/      # Build guides and compliance reports  
├── 📁 docs/            # Full documentation and descriptions
├── 📁 releases/        # Built packages ready for distribution
├── 📁 tools/           # Build scripts and automation utilities
├── __init__.py         # Main addon file
├── blender_manifest.toml # Extension metadata
└── README.md           # This file
```

## 🛠️ Development

### Building
```bash
# Smart build (all platforms)
python tools/smart_build.py

# Manual build
python tools/build_extension.py
```

### Documentation
- **Full Documentation**: [`docs/README_FULL.md`](docs/README_FULL.md)
- **Build Instructions**: [`development/BUILD.md`](development/BUILD.md)  
- **Smart Build Guide**: [`development/SMART_BUILD_GUIDE.md`](development/SMART_BUILD_GUIDE.md)

## 📦 Downloads

| Platform | Link | License |
|----------|------|---------|
| **Blender Extensions** | [Download](releases/blender_extensions/) | GPL 3.0+ |
| **Gumroad** | [Download](releases/gumroad_commercial/) | Commercial |

## 🤝 Credits

**Developed by Nandur Studio**
- Original concept and implementation
- Real-time topology visualization system
- Professional packaging and distribution

**Powered by Blender Foundation**
- Built on Blender's powerful Python API
- Designed for Blender 4.2+ ecosystem

## 📄 License

- **Open Source**: [GPL 3.0+](LICENSE_GPL.txt) for Blender Extensions
- **Commercial**: [Custom License](LICENSE.txt) for Gumroad distribution

---

*Transform your mesh cleanup workflow with professional-grade tools. Download today!*