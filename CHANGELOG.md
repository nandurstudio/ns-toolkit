# Changelog

## v1.0.1 - Blender Extensions Compliance Update

### Features
- add simplified success message for mesh cleanup operations
- add direct property access for mode switching (no bpy.ops dependency)
- add logo-free lightweight package for better performance

### Bug Fixes  
- ensure highlight topology operations don't register in undo history
- fix bpy.ops usage replaced with bmesh.ops for better reliability
- fix context-dependent operator calls with lower-level API implementation
- ensure mode switching uses direct property access instead of operators

### Performance Improvements
- reduce addon package size by 74% (32.9KB → 8.7KB) by removing logo
- optimize mesh operations with bmesh.ops instead of bpy.ops succession
- improve reliability by eliminating context-dependent operator chains

### Code Quality
- refactor OBJECT_OT_tris_to_quads_merge operator to use bmesh.ops exclusively
- remove all emoji characters from code for cleaner implementation  
- replace verbose success messages with concise user-friendly feedback
- ensure Blender Extensions platform best practices compliance