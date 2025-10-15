# 📁 NS Toolkit - Project Organization Guide

## 🏗️ Project Structure

```
ns-toolkit/
├── 📁 assets/                      # Visual resources and branding
│   ├── Nandur93_Logo_192.png       # Studio logo (192x192)  
│   ├── tris_to_quads_banner_1920x1080.png    # Marketing banner
│   ├── tris_to_quads_icon_256x256.png       # Addon icon
│   ├── tris_to_quads_preview2_1920x1080.png # Feature preview
│   └── Screenshot 2025-10-15 001000.png     # UI screenshot
│
├── 📁 development/                 # Build guides and compliance
│   ├── BLENDER_BUILD_INSTRUCTIONS.md  # Step-by-step build guide
│   ├── BUILD.md                   # Quick build reference
│   ├── build_packages.py          # Legacy build script
│   ├── CHANGELOG_v1.0.0.md        # Version 1.0.0 changes
│   ├── COMPLIANCE_REPORT.md       # Extensions platform compliance
│   ├── PUBLISHING_STRATEGY.md     # Multi-platform strategy
│   ├── RELEASE_CHECKLIST.md       # Pre-submission checklist
│   └── SMART_BUILD_GUIDE.md       # Smart build system guide
│
├── 📁 docs/                       # Full documentation
│   ├── GUMROAD_DESCRIPTION.md     # Commercial marketplace description
│   ├── MARKETPLACE_DESCRIPTION.md # General marketplace description
│   └── README_FULL.md             # Complete feature documentation
│
├── 📁 releases/                   # Built packages (auto-generated)
│   ├── blender_extensions/        # GPL version for Blender Extensions
│   │   ├── __init__.py
│   │   ├── blender_manifest.toml
│   │   ├── LICENSE_GPL.txt
│   │   ├── Nandur93_Logo_192.png
│   │   ├── README.md
│   │   └── ns_toolkit_mesh_cleanup_pro-1.0.0.zip
│   └── gumroad_commercial/        # Commercial version for Gumroad
│       ├── __init__.py
│       ├── blender_manifest.toml  
│       ├── LICENSE.txt
│       ├── Nandur93_Logo_192.png
│       ├── README.md
│       ├── QUICK_START.md
│       └── ns_toolkit_mesh_cleanup_pro_commercial-1.0.0.zip
│
├── 📁 tools/                      # Build automation utilities
│   ├── build_extension.py         # Manual Blender extension builder
│   ├── build.bat                  # Windows batch build script  
│   └── smart_build.py             # Advanced multi-platform builder
│
├── __init__.py                    # ⭐ Main addon file
├── blender_manifest.toml          # ⭐ Extension metadata
├── LICENSE_GPL.txt               # GPL 3.0+ license
├── LICENSE.txt                    # Commercial license
└── README.md                      # ⭐ Project overview
```

## 🎯 Core Files (Essential)

| File | Purpose | Status |
|------|---------|--------|
| `__init__.py` | Main addon with professional mesh cleanup functionality | ✅ Ready |
| `blender_manifest.toml` | Extension metadata | ✅ Compliant |
| `README.md` | Project overview | ✅ Complete |

## 🔧 Development Workflow

### 1. **Make Changes**
```bash
# Edit main addon
edit __init__.py

# Update version in manifest  
edit blender_manifest.toml
```

### 2. **Build Packages**
```bash
# Smart build (recommended)
python tools/smart_build.py

# Manual build
python tools/build_extension.py
```

### 3. **Validate & Test**
- Packages automatically validated
- Blender compatibility checked
- Ready for submission

## 📦 Distribution Channels

### Blender Extensions (GPL)
- **Location**: `releases/blender_extensions/`
- **License**: GPL 3.0+
- **Package**: `ns_toolkit_mesh_cleanup_pro-1.0.0.zip`
- **Submit**: https://extensions.blender.org/submit/

### Gumroad (Commercial)
- **Location**: `releases/gumroad_commercial/`  
- **License**: Commercial
- **Package**: `ns_toolkit_mesh_cleanup_pro_commercial-1.0.0.zip`
- **Upload**: https://gumroad.com/

## 🚀 Smart Build Benefits

1. **Single Source**: Develop once in root directory
2. **Auto Sync**: Files automatically copied to platforms
3. **Dual License**: GPL and Commercial versions generated
4. **Validation**: Built-in compliance checking
5. **Clean Packages**: Only necessary files included

## 📋 Maintenance

### Monthly Tasks
- [ ] Update version numbers
- [ ] Test with latest Blender build
- [ ] Review documentation accuracy
- [ ] Check marketplace performance

### Release Tasks  
- [ ] Run smart build
- [ ] Validate packages
- [ ] Update changelogs
- [ ] Submit to platforms

## ⚠️ Important Notes

- **Assets excluded** from built packages via `blender_manifest.toml`
- **Development files excluded** to keep packages clean
- **Two licenses** maintained for dual distribution strategy
- **Version sync** handled automatically by smart build system

---

*This organization ensures clean separation of concerns while maintaining efficient development workflow.*