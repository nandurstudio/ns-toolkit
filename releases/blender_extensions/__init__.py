bl_info = {
    "name": "NS Toolkit - Mesh Cleanup Pro",
    "author": "NS Toolkit | Created by Nandur Studio (Nandang Duryat) © 2025",
    "version": (1, 0, 0),
    "blender": (4, 2, 0),
    "location": "Object > Convert / Sidebar (N) > NS Toolkit",
    "description": "Professional mesh cleanup toolkit: Highlight mesh topology + Tris to Quads + Merge by Distance + Recalculate Normals + Reset Vectors.",
    "category": "Mesh",
}

# Version constant for UI display
ADDON_VERSION = bl_info["version"]

import bpy
import bmesh
import os
from bpy.props import BoolProperty
from bpy.app.handlers import persistent

# --- Scene Properties ---
class NS_ToolkitProperties(bpy.types.PropertyGroup):
    highlight_topology: BoolProperty(
        name="Highlight Topology",
        description="Toggle mesh topology highlighting for ALL objects in scene (Triangles, Quads, N-gons)",
        default=False,
        update=lambda self, context: toggle_topology_highlight(self, context)
    )

def toggle_topology_highlight(self, context):
    """Toggle mesh topology highlighting"""
    if self.highlight_topology:
        apply_topology_highlighting(context)
        # Register update handlers for live updating (both Edit and Object mode)
        if depsgraph_update_handler not in bpy.app.handlers.depsgraph_update_post:
            bpy.app.handlers.depsgraph_update_post.append(depsgraph_update_handler)
        if scene_update_handler not in bpy.app.handlers.scene_update_pre:
            bpy.app.handlers.scene_update_pre.append(scene_update_handler)
    else:
        clear_topology_highlighting(context)
        # Unregister update handlers
        if depsgraph_update_handler in bpy.app.handlers.depsgraph_update_post:
            bpy.app.handlers.depsgraph_update_post.remove(depsgraph_update_handler)
        if scene_update_handler in bpy.app.handlers.scene_update_pre:
            bpy.app.handlers.scene_update_pre.remove(scene_update_handler)

def apply_topology_highlighting(context):
    """Apply topology highlighting to all mesh objects"""
    # Get ALL mesh objects in scene (not just selected)
    mesh_objects = [obj for obj in context.scene.objects if obj.type == 'MESH']
    
    if not mesh_objects:
        return
    
    # Set viewport shading to Solid with Object Color
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'SOLID'
                    space.shading.color_type = 'OBJECT'
                    break
    
    for obj in mesh_objects:
        # Get mesh data
        mesh = obj.data
        
        # Analyze topology and set object color based on dominant topology
        triangle_count = 0
        quad_count = 0
        ngon_count = 0
        
        # Use bmesh if in Edit mode for real-time data
        if context.mode == 'EDIT_MESH' and obj == context.active_object:
            # Get bmesh representation for real-time updates
            bm = bmesh.from_edit_mesh(mesh)
            
            for face in bm.faces:
                vertex_count = len(face.verts)
                if vertex_count == 3:
                    triangle_count += 1
                elif vertex_count == 4:
                    quad_count += 1
                else:
                    ngon_count += 1
        else:
            # Standard mesh analysis for Object mode
            for poly in mesh.polygons:
                vertex_count = len(poly.vertices)
                if vertex_count == 3:
                    triangle_count += 1
                elif vertex_count == 4:
                    quad_count += 1
                else:
                    ngon_count += 1
        
        # Set color based on dominant topology
        total_faces = triangle_count + quad_count + ngon_count
        if total_faces > 0:
            tri_ratio = triangle_count / total_faces
            quad_ratio = quad_count / total_faces
            ngon_ratio = ngon_count / total_faces
            
            # Color strategy: Prioritize N-gons for visibility since they're most important to identify
            if ngon_count > 0:
                obj.color = (0.0, 0.0, 1.0, 1.0)  # Blue for ANY N-gons present
            elif tri_ratio > quad_ratio:
                obj.color = (1.0, 0.0, 0.0, 1.0)  # Red for triangle-dominant (no n-gons)
            else:
                obj.color = (0.0, 1.0, 0.0, 1.0)  # Green for quad-dominant/equal (no n-gons)
        
        # Store original color for restoration
        if not hasattr(obj, "ns_original_color"):
            obj["ns_original_color"] = list(obj.color)

def clear_topology_highlighting(context):
    """Clear topology highlighting from all mesh objects"""
    # Get ALL mesh objects in scene
    mesh_objects = [obj for obj in context.scene.objects if obj.type == 'MESH']
    
    if not mesh_objects:
        return
    
    for obj in mesh_objects:
        # Restore original color if stored
        if "ns_original_color" in obj:
            obj.color = obj["ns_original_color"]
            del obj["ns_original_color"]
        else:
            # Default white color
            obj.color = (1.0, 1.0, 1.0, 1.0)
    
    # Reset viewport shading to Object Color (Random)
    for area in context.screen.areas:
        if area.type == 'VIEW_3D':
            for space in area.spaces:
                if space.type == 'VIEW_3D':
                    space.shading.type = 'SOLID'
                    space.shading.color_type = 'RANDOM'
                    break

@persistent
def depsgraph_update_handler(scene, depsgraph):
    """Handler for live updating topology highlighting when mesh changes"""
    # Check if highlight topology is active
    if hasattr(scene, 'ns_toolkit_props') and scene.ns_toolkit_props.highlight_topology:
        # Check if any mesh objects were updated
        for update in depsgraph.updates:
            if update.id.bl_rna.identifier == 'Mesh':
                # Mesh data was updated, refresh highlighting
                context = bpy.context
                apply_topology_highlighting(context)
                break

@persistent
def scene_update_handler(scene):
    """Handler for real-time updates in Edit mode"""
    # Check if highlight topology is active
    if hasattr(scene, 'ns_toolkit_props') and scene.ns_toolkit_props.highlight_topology:
        context = bpy.context
        # Only update if in Edit mode to avoid performance issues
        if context.mode == 'EDIT_MESH':
            apply_topology_highlighting(context)

# --- Load logo ---
custom_icons = None

def load_logo():
    import bpy.utils.previews
    global custom_icons
    if custom_icons is None:
        custom_icons = bpy.utils.previews.new()
        icons_dir = os.path.dirname(__file__)
        custom_icons.load("nandur_logo", os.path.join(icons_dir, "Nandur93_Logo_192.png"), 'IMAGE')

def unload_logo():
    import bpy.utils.previews
    global custom_icons
    if custom_icons is not None:
        bpy.utils.previews.remove(custom_icons)
        custom_icons = None


# --- Operator utama ---
class OBJECT_OT_tris_to_quads_merge(bpy.types.Operator):
    """Convert selected meshes: Tris → Quads + Merge by Distance + Recalculate Normals + Reset Vectors"""
    bl_idname = "object.tris_to_quads_merge"
    bl_label = "Clean Mesh"
    bl_options = {'REGISTER', 'UNDO'}

    merge_distance = bpy.props.FloatProperty(
        name="Merge Distance",
        description="Distance threshold for merging vertices",
        default=0.0001,
        min=0.0,
        max=1.0,
        precision=5
    )

    def execute(self, context):
        selected_objects = [obj for obj in context.selected_objects if obj.type == 'MESH']
        if not selected_objects:
            self.report({'WARNING'}, "Tidak ada mesh yang dipilih.")
            return {'CANCELLED'}

        # Get the merge distance value safely
        merge_dist = getattr(self, 'merge_distance', 0.0001)
        if not isinstance(merge_dist, (int, float)):
            merge_dist = 0.0001

        for obj in selected_objects:
            bpy.context.view_layer.objects.active = obj
            bpy.ops.object.mode_set(mode='EDIT')
            bpy.ops.mesh.select_all(action='SELECT')
            bpy.ops.mesh.tris_convert_to_quads()
            
            # Use remove_doubles - still available in Blender 4.5
            bpy.ops.mesh.remove_doubles(threshold=merge_dist)
            
            # Recalculate normals outside
            bpy.ops.mesh.normals_make_consistent(inside=False)
            
            # Reset custom normal vectors
            try:
                bpy.ops.mesh.customdata_custom_splitnormals_clear()
            except:
                # Fallback if custom normals operation is not available
                pass
            
            bpy.ops.object.mode_set(mode='OBJECT')

        self.report({'INFO'}, f"✅ NS Toolkit: {len(selected_objects)} mesh(es) processed successfully! (Tris → Quads + Merge + Normals + Reset)")
        return {'FINISHED'}


# --- Highlight Topology Operators ---
class NS_TOOLKIT_OT_highlight_topology(bpy.types.Operator):
    """Highlight mesh topology for ALL objects in scene using viewport color override"""
    bl_idname = "ns_toolkit.highlight_topology"
    bl_label = "Highlight Topology"
    bl_options = {'REGISTER'}

    def execute(self, context):
        # Get ALL mesh objects in scene (not just selected)
        mesh_objects = [obj for obj in context.scene.objects if obj.type == 'MESH']
        
        if not mesh_objects:
            self.report({'WARNING'}, "No mesh objects found in scene.")
            return {'CANCELLED'}

        # Ensure we're in Object mode
        if context.mode != 'OBJECT':
            bpy.ops.object.mode_set(mode='OBJECT')
        
        # Apply highlighting using the shared function
        apply_topology_highlighting(context)
        
        # Count colored objects for report
        red_count = sum(1 for obj in mesh_objects if obj.color[:3] == (1.0, 0.0, 0.0))
        green_count = sum(1 for obj in mesh_objects if obj.color[:3] == (0.0, 1.0, 0.0))
        blue_count = sum(1 for obj in mesh_objects if obj.color[:3] == (0.0, 0.0, 1.0))
        
        self.report({'INFO'}, f"✅ Highlighted {len(mesh_objects)} objects: {red_count}🔴Tri, {green_count}🟢Quad, {blue_count}🔵N-gon")
        return {'FINISHED'}


class NS_TOOLKIT_OT_clear_highlight(bpy.types.Operator):
    """Clear mesh topology highlighting and restore original colors for ALL objects"""
    bl_idname = "ns_toolkit.clear_highlight"
    bl_label = "Clear Highlight"
    bl_options = {'REGISTER'}

    def execute(self, context):
        # Get ALL mesh objects in scene
        mesh_objects = [obj for obj in context.scene.objects if obj.type == 'MESH']
        
        if not mesh_objects:
            self.report({'INFO'}, "No mesh objects found in scene.")
            return {'FINISHED'}
        
        # Clear highlighting using the shared function
        clear_topology_highlighting(context)
        
        self.report({'INFO'}, f"✅ Topology highlighting cleared for {len(mesh_objects)} objects")
        return {'FINISHED'}


# --- Panel di Sidebar (N) ---
class VIEW3D_PT_ns_toolkit_panel(bpy.types.Panel):
    bl_label = "NS Toolkit"
    bl_idname = "VIEW3D_PT_ns_toolkit_panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "NS Toolkit"

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        ns_props = scene.ns_toolkit_props
        
        # Header with logo
        if custom_icons and "nandur_logo" in custom_icons:
            layout.template_icon(icon_value=custom_icons["nandur_logo"].icon_id, scale=4.0)
        
        # Highlight topology section
        box = layout.box()
        box.label(text="Topology Visualization", icon="SHADING_WIRE")
        
        # Toggle for highlight topology
        row = box.row(align=True)
        row.prop(ns_props, "highlight_topology", text="Highlight All Objects", icon="RESTRICT_VIEW_OFF" if ns_props.highlight_topology else "RESTRICT_VIEW_ON")
        
        if ns_props.highlight_topology:
            col = box.column(align=True)
            col.scale_y = 0.8
            col.label(text="🔵 Blue = Has N-gons", icon="NONE")
            col.label(text="🔴 Red = Triangle-dominant", icon="NONE")
            col.label(text="🟢 Green = Quad-dominant", icon="NONE")
        
        # Main tool section
        layout.separator()
        box = layout.box()
        box.label(text="Mesh Cleanup Actions", icon="MESH_DATA")
        box.operator(OBJECT_OT_tris_to_quads_merge.bl_idname, text="Clean Mesh", icon="FACE_MAPS")
        
        # Credit section
        layout.separator()
        col = layout.column(align=True)
        col.scale_y = 0.7
        # Use module-level version constant
        version_str = f"v{ADDON_VERSION[0]}.{ADDON_VERSION[1]}.{ADDON_VERSION[2]}"
        col.label(text=f"NS Toolkit {version_str} © 2025", icon="INFO")
        col.label(text="Created by Nandur Studio")


# --- Shortcut ---
addon_keymaps = []

def register_shortcut():
    wm = bpy.context.window_manager
    km = wm.keyconfigs.addon.keymaps.new(name='Object Mode', space_type='EMPTY')
    kmi = km.keymap_items.new(OBJECT_OT_tris_to_quads_merge.bl_idname, 'J', 'PRESS', ctrl=True, alt=True)
    addon_keymaps.append((km, kmi))

def unregister_shortcut():
    for km, kmi in addon_keymaps:
        km.keymap_items.remove(kmi)
    addon_keymaps.clear()


# --- Registrasi ---
def menu_func(self, context):
    self.layout.separator()
    self.layout.operator(OBJECT_OT_tris_to_quads_merge.bl_idname, icon="FACE_MAPS")

def register():
    load_logo()
    bpy.utils.register_class(NS_ToolkitProperties)
    bpy.utils.register_class(OBJECT_OT_tris_to_quads_merge)
    bpy.utils.register_class(NS_TOOLKIT_OT_highlight_topology)
    bpy.utils.register_class(NS_TOOLKIT_OT_clear_highlight)
    bpy.utils.register_class(VIEW3D_PT_ns_toolkit_panel)
    bpy.types.Scene.ns_toolkit_props = bpy.props.PointerProperty(type=NS_ToolkitProperties)
    bpy.types.VIEW3D_MT_object_convert.append(menu_func)
    register_shortcut()

def unregister():
    # Clear any active highlighting and remove handlers
    if depsgraph_update_handler in bpy.app.handlers.depsgraph_update_post:
        bpy.app.handlers.depsgraph_update_post.remove(depsgraph_update_handler)
    if scene_update_handler in bpy.app.handlers.scene_update_pre:
        bpy.app.handlers.scene_update_pre.remove(scene_update_handler)
    
    unregister_shortcut()
    bpy.types.VIEW3D_MT_object_convert.remove(menu_func)
    del bpy.types.Scene.ns_toolkit_props
    bpy.utils.unregister_class(VIEW3D_PT_ns_toolkit_panel)
    bpy.utils.unregister_class(NS_TOOLKIT_OT_clear_highlight)
    bpy.utils.unregister_class(NS_TOOLKIT_OT_highlight_topology)
    bpy.utils.unregister_class(OBJECT_OT_tris_to_quads_merge)
    bpy.utils.unregister_class(NS_ToolkitProperties)
    unload_logo()

if __name__ == "__main__":
    register()
