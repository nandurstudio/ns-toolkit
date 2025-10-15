# NS Toolkit - Mesh Cleanup Pro

![NS Toolkit Logo](Nandur93_Logo_192.png)

**Professional mesh cleanup toolkit for Blender 4.2+**

*Created by Nandur Studio (Nandang Duryat) © 2025*

---

## 🚀 Overview

NS Toolkit - Mesh Cleanup Pro is a powerful Blender add-on designed to streamline your mesh workflow with visual topology analysis and one-click automation. Perfect for game developers, 3D artists, and anyone working with imported meshes that need quick cleanup and optimization.

### ✨ What it does:
1. **Topology Visualization** - Highlights triangles, quads, and n-gons with color coding for easy identification
2. **Converts Triangles to Quads** - Automatically optimizes triangle meshes into quad-based topology
3. **Merges Vertices by Distance** - Removes duplicate vertices and cleans up overlapping geometry  
4. **Recalculates Normals Outside** - Fixes inverted faces and ensures consistent normal direction
5. **Resets Custom Normal Vectors** - Clears any custom split normals and returns to default calculations

Visualize before you clean! The new topology highlighting feature lets you see exactly what needs fixing before running cleanup operations.

---

## 🎯 Features

### 👁️ **Advanced Real-Time Topology Visualization**
- **Color-Coded Highlighting**: Red=Triangles, Green=Quads, Blue=N-gons
- **Real-Time Toggle**: Enable/disable highlighting instantly
- **Visual Feedback**: See problematic topology before cleanup
- **Professional Workflow**: Analyze then optimize with confidence

### 🔧 **One-Click Mesh Cleanup**
- **Tris to Quads Conversion**: Smart algorithm converts triangular faces to quads where possible
- **Merge by Distance**: Configurable threshold for removing duplicate vertices (default: 0.0001)
- **Normal Recalculation**: Ensures all faces point outward for proper lighting and rendering
- **Normal Vector Reset**: Clears custom split normals for clean, default normal calculations

### 🎨 **User-Friendly Interface**
- **Sidebar Panel**: Easy access via N-Panel in 3D Viewport under "NS Toolkit" tab
- **Object Menu Integration**: Available in Object > Convert menu
- **Keyboard Shortcut**: Quick access via `Ctrl + Alt + J`

### ⚙️ **Customizable Settings**
- **Adjustable Merge Distance**: Fine-tune vertex merging threshold for your specific needs
- **Batch Processing**: Process multiple selected objects simultaneously
- **Undo Support**: Full integration with Blender's undo system

### 🎨 **Professional UI**
- Clean, modern interface design
- Visual feedback with success notifications
- Branded NS Toolkit experience

---

## 📋 System Requirements

- **Blender Version**: 4.2.0 or higher
- **Operating System**: Windows, macOS, Linux
- **Memory**: Minimal requirements (processes mesh data in memory)

---

## 🔧 Installation

### Method 1: Standard Installation
1. Download the `tris_to_quads_merge_addon.zip` file
2. Open Blender
3. Go to `Edit > Preferences > Add-ons`
4. Click `Install...` button
5. Navigate to the downloaded ZIP file and select it
6. Enable the add-on by checking the checkbox next to "NS Toolkit - Mesh Cleanup Pro"

### Method 2: Manual Installation
1. Extract the ZIP file to your Blender add-ons directory:
   - **Windows**: `%APPDATA%\Blender Foundation\Blender\[VERSION]\scripts\addons\`
   - **macOS**: `~/Library/Application Support/Blender/[VERSION]/scripts/addons/`
   - **Linux**: `~/.config/blender/[VERSION]/scripts/addons/`
2. Restart Blender
3. Enable the add-on in Preferences > Add-ons

---

## 🎮 How to Use

### Quick Start
1. Select one or more mesh objects in your scene
2. Access NS Toolkit via any of these methods:
   - **Sidebar**: Press `N` to open sidebar, go to "NS Toolkit" tab
   - **Menu**: Object > Convert > "Tris to Quads + Merge + Normals"
   - **Shortcut**: `Ctrl + Alt + J`
3. Adjust merge distance if needed (default: 0.0001 works for most cases)
4. Click the button and watch the magic happen!

### Detailed Workflow
1. **Select Target Meshes**: Choose the objects you want to clean up
2. **Configure Settings**: Adjust merge distance based on your mesh scale and requirements
3. **Execute Operation**: Run the cleanup process
4. **Review Results**: Check the console message for processing summary

### Best Practices
- **Backup Your Work**: Always save before running batch operations
- **Test Settings**: Try different merge distances on a copy first
- **Check Results**: Verify normals and topology after processing
- **Iterative Workflow**: Can be run multiple times for complex meshes

---

## ⚙️ Settings Reference

### Merge Distance
- **Range**: 0.0 to 1.0
- **Default**: 0.0001
- **Purpose**: Determines how close vertices need to be for merging
- **Recommendations**:
  - **Small objects/high detail**: 0.0001 - 0.001
  - **Medium objects**: 0.001 - 0.01
  - **Large objects/rough meshes**: 0.01 - 0.1

---

## 🎯 Use Cases

### Game Development
- Clean up imported CAD models
- Optimize mesh topology for real-time rendering
- Prepare assets for game engines

### 3D Printing
- Fix mesh issues before slicing
- Ensure manifold geometry
- Optimize file sizes

### Animation & Rendering
- Prepare meshes for subdivision surface
- Fix imported model issues
- Standardize mesh topology

### Architecture Visualization
- Clean up imported BIM models
- Optimize complex architectural meshes
- Prepare models for rendering

---

## 🔍 Troubleshooting

### Common Issues

**Q: The add-on doesn't appear after installation**
A: Make sure you've enabled it in Preferences > Add-ons. Search for "NS Toolkit" if the list is long.

**Q: Getting errors when running the tool**
A: Ensure you have mesh objects selected and you're in Object mode before running the operation.

**Q: Merge distance seems too aggressive**
A: Try reducing the merge distance value. Start with 0.0001 and adjust as needed.

**Q: Some faces are still triangles after conversion**
A: This is normal. The algorithm only converts triangles to quads where it makes topological sense.

**Q: Normals are still incorrect after processing**
A: Some complex meshes might need manual normal correction. Try running the tool multiple times or use Blender's manual normal tools.

### Performance Tips
- Process objects in smaller batches for very large scenes
- Consider the merge distance relative to your object scale
- Use on duplicate objects first to test settings

---

## 📞 Support & Contact

### Get Help
- **Documentation**: This README file
- **Blender Community**: Post questions in Blender forums with "NS Toolkit" tag
- **Bug Reports**: Include Blender version, OS, and steps to reproduce

### About the Creator
**NS Toolkit** is created by **Nandur Studio (Nandang Duryat)** © 2025

- Passionate Blender developer focused on workflow optimization
- Committed to creating tools that save time and improve productivity
- Active in the Blender community since 2020+

---

## 📄 License & Terms

### Usage Rights
- ✅ Personal and commercial use allowed
- ✅ Use in client projects
- ✅ Modify for personal use
- ❌ Redistribute or resell the add-on
- ❌ Remove copyright notices

### Disclaimer
This add-on is provided "as is" without warranty. Always backup your work before using any automation tools.

---

## 🔄 Version History

### v1.0.0 (2025) - Initial Release
- ✅ **Revolutionary Real-Time Topology Visualization**: Industry-first scene-wide highlighting system
- ✅ **Intelligent Color Coding**: Priority-based detection (Blue=N-gons, Red=Triangles, Green=Quads)
- ✅ **Live Edit Mode Updates**: Instant visual feedback as you modify mesh topology
- ✅ **Complete 5-in-1 Toolkit**: Visualization + Tris to Quads + Merge + Normals + Reset Vectors
- ✅ **Performance Optimized**: Dual handler system with automatic cleanup
- ✅ **Professional Interface**: Dynamic version display, branded experience, comprehensive UI
- ✅ **Cross-Platform Ready**: Dual licensing for Blender Extensions (GPL) and Commercial (Gumroad)
- ✅ **Modern Compatibility**: Blender 4.2+ with extensive validation and testing
- ✅ **Developer-Friendly**: Smart build system, comprehensive documentation, extensible architecture

---

## 🎉 Thank You!

Thank you for choosing NS Toolkit! Your support helps us continue developing quality tools for the Blender community.

**Happy Blending!** 🚀

---

*NS Toolkit © 2025 | Created by Nandur Studio*