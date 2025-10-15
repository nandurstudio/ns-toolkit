# NS Toolkit - Smart Build System

## 🚀 **"Develop Once, Distribute Everywhere"**

Smart build system yang otomatis sync source code ke semua platform releases dan build packages.

---

## ⚡ **Quick Usage**

### Build All Platforms:
```bash
python smart_build.py
# or
python smart_build.py --platform all
```

### Build Specific Platform:
```bash
# Blender Extensions only
python smart_build.py --platform blender

# Gumroad Commercial only  
python smart_build.py --platform gumroad
```

---

## 🔧 **How It Works**

### 1. **Single Source Development**
- Edit **only** the source files in root directory:
  - `__init__.py` - Main addon code
  - `blender_manifest.toml` - Extension manifest
  - Logo image located in `assets/Nandur93_Logo_192.png`

### 2. **Smart Sync & Distribution**
- Automatically copies source files to platform directories
- Maintains platform-specific files (licenses, READMEs)
- Auto-detects version from source code
- Builds separate packages for each platform

### 3. **Intelligent Build Process**
```
Source Files (Root)
    ↓ Smart Sync
releases/blender_extensions/   ←→   releases/gumroad_commercial/
    ↓ Build                           ↓ Build
package-1.0.0.zip                package_commercial-1.0.0.zip
```

---

## 📁 **File Structure**

```
tris_to_quads_merge_addon/
├── __init__.py                    ← 🎯 EDIT HERE
├── blender_manifest.toml          ← 🎯 EDIT HERE  
├── assets/
│   └── Nandur93_Logo_192.png      ← 🎯 EDIT HERE
├── tools/
│   └── smart_build.py             ← 🛠️ BUILD SCRIPT
│
├── releases/
│   ├── blender_extensions/        ← 🤖 AUTO-SYNCED
│   │   ├── __init__.py
│   │   ├── blender_manifest.toml
│   │   ├── Nandur93_Logo_192.png
│   │   ├── LICENSE_GPL.txt        ← Platform-specific
│   │   ├── README.md              ← Platform-specific
│   │   └── *.zip                  ← Generated packages
│   │
│   └── gumroad_commercial/        ← 🤖 AUTO-SYNCED
│       ├── __init__.py
│       ├── blender_manifest.toml
│       ├── Nandur93_Logo_192.png
│       ├── LICENSE.txt            ← Platform-specific
│       ├── README.md              ← Platform-specific
│       ├── QUICK_START.md         ← Platform-specific
│       └── *.zip                  ← Generated packages
```

---

## ✨ **Features**

### 🔄 **Smart Sync**
- Copies source files to all platform directories
- Preserves platform-specific files
- Auto-detects version from source code
- No manual copying needed

### 🧹 **Auto Cleanup** 
- Removes old package files before building
- Cleans both root and platform directories
- Prevents conflicts with old versions

### 📦 **Multi-Platform Building**
- **Blender Extensions**: GPL package for official platform
- **Gumroad Commercial**: Commercial package for marketplace
- Different licensing and documentation per platform

### ✅ **Comprehensive Validation**
- Package structure validation
- Required files verification
- Blender extension validation (if available)
- File count and size reporting

### 🎛️ **Flexible Options**
- Build all platforms or specific ones
- Command-line interface
- Detailed progress reporting
- Error handling and rollback

---

## 🎯 **Development Workflow**

### Old Way (Manual):
```
1. Edit source __init__.py
2. Copy to releases/blender_extensions/__init__.py
3. Copy to releases/gumroad_commercial/__init__.py
4. Build blender package
5. Build gumroad package  
6. Validate both packages
```

### New Way (Smart):
```
1. Edit source __init__.py
2. python smart_build.py
   ✅ Done! Both packages built and validated
```

---

## 💡 **Benefits**

### For Development:
- ✅ **Single source of truth** - Edit once, distribute everywhere
- ✅ **No duplication** - Eliminate copy-paste errors
- ✅ **Version consistency** - Auto-sync ensures same version everywhere
- ✅ **Fast iteration** - Quick build and test cycle

### For Distribution:
- ✅ **Multi-platform support** - Blender Extensions + Commercial
- ✅ **Platform optimization** - Different files per platform
- ✅ **Quality assurance** - Built-in validation
- ✅ **Professional packages** - Clean, consistent releases

---

## 🛠️ **Advanced Usage**

### Version Detection:
The script automatically detects version from `bl_info` in source `__init__.py`:
```python
"version": (2, 2, 0)  # → Becomes "2.2.0" in packages
```

### Platform Configuration:
Each platform has its own config in `smart_build.py`:
```python
"blender_extensions": {
    "package_name": "ns_toolkit_mesh_cleanup_pro",
    "license": "LICENSE_GPL.txt", 
    "extra_files": ["LICENSE_GPL.txt", "README.md"]
}
```

### Custom Platforms:
Easy to add new platforms by extending the `platforms` dictionary.

---

## 🎉 **Result**

After running the smart build:

```
✅ Successfully built 2 packages:
  ✅ blender_extensions: ns_toolkit_mesh_cleanup_pro-2.2.0.zip (31.5 KB)
  ✅ gumroad_commercial: ns_toolkit_mesh_cleanup_pro_commercial-2.2.0.zip (33.0 KB)

📤 Submit to: https://extensions.blender.org/submit/
💰 Upload to Gumroad marketplace
```

---

**Created by NS Toolkit | Nandur Studio © 2025**