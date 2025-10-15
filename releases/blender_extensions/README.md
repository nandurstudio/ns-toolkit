# NS Toolkit - Mesh Cleanup Pro

**Professional mesh cleanup with topology visualization tools for Blender 4.2+**

*Created by Nandur Studio (Nandang Duryat) © 2025*  
*Licensed under GPL 3.0+ - Free for all users*

---

## Overview

NS Toolkit - Mesh Cleanup Pro is a lightweight, **completely free** Blender add-on that streamlines mesh optimization workflows. Built with performance and reliability in mind, it uses advanced bmesh operations for fast, context-independent mesh processing.

**Perfect for game developers, 3D artists, architects, and anyone working with imported or complex geometry.**

---

## Key Features

### **Real-Time Topology Visualization**
- **Scene-wide highlighting** - Visualize ALL mesh objects simultaneously
- **Smart color coding**: Blue = N-gons, Red = Triangle-dominant, Green = Quad-dominant
- **Live updates** - Real-time feedback in both Edit and Object modes
- **Non-intrusive** - Doesn't clutter your undo history

### **Optimized Mesh Cleanup Engine**
1. **Smart Triangles to Quads** - Advanced bmesh.ops conversion algorithms
2. **Precise Vertex Merging** - Configurable distance threshold for duplicate removal
3. **Consistent Normal Calculation** - Automatic outside-facing normal correction
4. **Custom Normal Reset** - Clean slate for proper lighting calculations

All operations use **bmesh.ops** for maximum performance and reliability - no context-dependent operators!

### **Clean & Intuitive Interface**
- **Sidebar Integration**: Access via N-Panel under "NS Toolkit" tab
- **One-click operations** - "Clean Mesh" button handles everything
- **Simple feedback** - Concise success messages without clutter
- **Keyboard shortcut**: `Ctrl + Alt + J` for quick access
- **Batch processing**: Handle multiple selected objects at once

### **Performance & Reliability** 
- **Lightweight package**: Only 8.7KB - 74% smaller than previous versions
- **bmesh.ops powered**: No UI context dependencies, works in any situation  
- **Memory efficient**: Proper cleanup and error handling
- **Undo support**: Main cleanup operations integrate with Blender's undo system

---

## System Requirements

- **Blender**: 4.2.0 or higher
- **Platforms**: Windows, macOS, Linux
- **Package Size**: 8.7KB (lightweight!)
- **Dependencies**: None - uses Blender's built-in bmesh module

---

## Installation

1. **Blender Extensions**: Search "NS Toolkit" in `Edit > Preferences > Get Extensions`
2. **Enable**: Find "NS Toolkit - Mesh Cleanup Pro" and enable it
3. **Access**: Open sidebar (N-key) → "NS Toolkit" tab
4. **Ready!** Start cleaning your meshes

---

## How to Use

### Quick Workflow:
1. **Select** mesh object(s) in your scene
2. **Open** sidebar (N-key) → "NS Toolkit" tab  
3. **Optional**: Enable "Highlight All Objects" to see topology across your entire scene
4. **Adjust** merge distance if needed (default: 0.0001 works for most cases)
5. **Click** "Clean Mesh" button
6. **Done!** Get simple success notification: "Cleaned X mesh(es) successfully"

### Topology Visualization:
- **Blue objects** = Have N-gons (5+ sided faces) 
- **Red objects** = Triangle-dominant meshes
- **Green objects** = Quad-dominant meshes (optimal topology)
- **Live updates** = See changes instantly as you edit

### Pro Tips:
- Use **Ctrl + Alt + J** for quick cleanup access
- **Merge distance**: Start with 0.0001, increase for rougher meshes
- **Batch processing**: Select multiple objects for simultaneous cleanup
- **Real-time preview**: Enable highlighting before cleanup to see what needs fixing

---

## Perfect For

- **Game Development**: Clean imported CAD/FBX models for game engines
- **Architecture**: Process BIM and CAD models for clean visualization
- **3D Printing**: Ensure watertight geometry before slicing
- **Animation**: Prepare meshes for subdivision surfaces and rigging
- **Asset Creation**: Convert triangulated meshes to quad-based topology
- **Import Cleanup**: Fix messy geometry from various 3D software

---

## Technical Details

### What the Addon Does:
1. **bmesh.ops.join_triangles()** - Intelligently converts triangles to quads
2. **bmesh.ops.remove_doubles()** - Merges vertices within specified distance
3. **bmesh.ops.recalc_face_normals()** - Ensures consistent outside-facing normals
4. **Custom normal cleanup** - Removes custom split normals for clean lighting

### Why bmesh.ops?
- **Faster performance** - Direct mesh data manipulation
- **More reliable** - No dependency on UI context or active objects
- **Better error handling** - Robust operation in any Blender state
- **Memory efficient** - Proper cleanup and resource management

### Merge Distance Guide:
- **0.0001**: High-detail models, precise geometry
- **0.001**: Standard models, most common use case
- **0.01**: Rough imports, larger tolerances needed

---

## Troubleshooting

**Q: Panel doesn't appear after installation**  
A: Check that the addon is enabled in Preferences > Add-ons, search for "NS Toolkit"

**Q: "No mesh objects selected" warning**  
A: Select at least one mesh object before clicking "Clean Mesh"

**Q: Some triangles remain after cleanup**  
A: This is normal - only triangles that can form proper quads are converted

**Q: Merge distance removes too much detail**  
A: Use smaller values: try 0.0001 for detailed models, 0.001 for general use

**Q: Highlighting colors seem wrong**  
A: Colors show dominant topology: Blue=N-gons present, Red=mostly triangles, Green=mostly quads

---

## 🤝 Support & Contributing

This is a **free, open-source** project licensed under GPL 3.0+.

### Get Help:
- Check this documentation first
- Report bugs via [GitHub Issues](https://github.com/nandurstudio/ns-toolkit/issues)
- Join discussions in Blender community forums

### Contributing:
- Source code available on request
- Feature suggestions welcome
- Pull requests accepted for improvements

### About the Author:
Created by **Nandur Studio (Nandang Duryat)**, passionate Blender developer focused on workflow optimization tools.

---

## 📜 License

**GNU General Public License v3.0+**

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

Full license: https://www.gnu.org/licenses/gpl-3.0.txt

---

## Version History

### v1.0.1 (2025) - Compliance & Performance Update
- **Lightweight package**: 74% size reduction (33KB → 8.7KB)
- **Better reliability**: Replaced bpy.ops with bmesh.ops for all mesh operations
- **Cleaner feedback**: Simplified success messages without clutter
- **Improved performance**: Direct mesh data manipulation, no UI context dependencies
- **Undo optimization**: Highlight operations no longer clutter undo history
- **Blender Extensions compliant**: All validation requirements met

### v1.0.0 (2025) - Initial Release
- Real-time topology visualization with scene-wide highlighting
- Professional mesh cleanup toolkit with automated operations
- Smart color coding system for topology identification
- Live updates in both Edit and Object modes
- GPL 3.0+ open source licensing

---

## Why Choose NS Toolkit?

- **Completely Free**: GPL 3.0+ licensed, no premium versions
- **Lightweight**: Only 8.7KB package size
- **Fast & Reliable**: bmesh.ops powered operations 
- **No Dependencies**: Uses Blender's built-in tools only
- **Time Saver**: One-click mesh optimization
- **Professional Grade**: Built with industry best practices
- **Open Source**: Transparent, community-driven development

---

## Support

- **Documentation**: This README covers all functionality
- **Bug Reports**: [GitHub Issues](https://github.com/nandurstudio/ns-toolkit/issues)
- **Feature Requests**: Community suggestions welcome
- **Source Code**: Available under GPL 3.0+ license

**Ready to optimize your mesh workflow?** Download and start cleaning! 

---

*NS Toolkit v1.0.1 © 2025 | Created by Nandur Studio*  
*Free & Open Source - Licensed under GPL 3.0+*