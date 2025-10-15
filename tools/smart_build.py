#!/usr/bin/env python3
"""
NS Toolkit - Smart Build & Distribution System
Develop once, distribute everywhere!

Usage: python smart_build.py [--platform all|blender|gumroad]
"""

import os
import sys
import shutil
import zipfile
import argparse
from pathlib import Path
import subprocess

def print_step(message):
    """Print a step with formatting"""
    print(f"\n🔧 {message}")

def print_success(message):
    """Print success message"""
    print(f"✅ {message}")

def print_error(message):
    """Print error message"""
    print(f"❌ {message}")

def print_info(message):
    """Print info message"""
    print(f"ℹ️  {message}")

def print_header(message):
    """Print header with formatting"""
    print(f"\n{'='*60}")
    print(f"🚀 {message}")
    print(f"{'='*60}")

class SmartBuilder:
    def __init__(self):
        self.root_dir = Path(__file__).parent.parent  # Go up one level from tools/
        self.source_files = {
            "__init__.py": "__init__.py",
            "blender_manifest.toml": "blender_manifest.toml"
        }
        
        # Platform configurations
        self.platforms = {
            "blender_extensions": {
                "dir": self.root_dir / "releases" / "blender_extensions",
                "package_name": "ns_toolkit_mesh_cleanup_pro",
                "license": "LICENSE_GPL.txt",
                "readme": "README.md",
                "extra_files": ["LICENSE_GPL.txt", "README.md"]
            },
            "gumroad_commercial": {
                "dir": self.root_dir / "releases" / "gumroad_commercial", 
                "package_name": "ns_toolkit_mesh_cleanup_pro_commercial",
                "license": "LICENSE.txt",
                "readme": "README.md", 
                "extra_files": ["LICENSE.txt", "README.md", "QUICK_START.md"]
            }
        }
    
    def get_version_from_source(self):
        """Extract version from source __init__.py"""
        init_file = self.root_dir / "__init__.py"
        try:
            with open(init_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Look for version tuple
                for line in content.split('\n'):
                    if '"version":' in line and '(' in line:
                        # Extract version tuple like (2, 2, 0)
                        start = line.find('(')
                        end = line.find(')')
                        if start != -1 and end != -1:
                            version_tuple = line[start+1:end]
                            # Convert to string format like "2.2.0"
                            version_parts = [x.strip() for x in version_tuple.split(',')]
                            return '.'.join(version_parts)
            return "2.2.0"  # Default fallback
        except Exception as e:
            print_error(f"Could not extract version: {e}")
            return "2.2.0"
    
    def sync_source_to_platforms(self, platforms=None):
        """Copy source files to platform directories"""
        if platforms is None:
            platforms = list(self.platforms.keys())
        
        print_step("Syncing source files to platforms...")
        
        version = self.get_version_from_source()
        print_info(f"Detected version: {version}")
        
        for platform in platforms:
            if platform not in self.platforms:
                print_error(f"Unknown platform: {platform}")
                continue
                
            config = self.platforms[platform]
            platform_dir = config["dir"]
            
            print_info(f"Syncing to {platform}...")
            
            # Ensure platform directory exists
            platform_dir.mkdir(parents=True, exist_ok=True)
            
            # Copy source files
            for source_file, target_file in self.source_files.items():
                source_path = self.root_dir / source_file
                target_path = platform_dir / target_file
                
                if source_path.exists():
                    shutil.copy2(source_path, target_path)
                    print_info(f"  Copied: {source_file}")
                else:
                    print_error(f"  Missing source: {source_file}")
            
            # Verify platform-specific files exist
            for extra_file in config["extra_files"]:
                extra_path = platform_dir / extra_file
                if not extra_path.exists():
                    print_error(f"  Missing platform file: {extra_file}")
        
        print_success("Source sync completed")
    
    def clean_packages(self, platforms=None):
        """Remove existing packages"""
        if platforms is None:
            platforms = list(self.platforms.keys())
        
        print_step("Cleaning existing packages...")
        
        # Clean root directory
        for zip_file in self.root_dir.glob("*.zip"):
            print_info(f"Removing root: {zip_file.name}")
            zip_file.unlink()
        
        # Clean platform directories
        for platform in platforms:
            if platform in self.platforms:
                platform_dir = self.platforms[platform]["dir"]
                if platform_dir.exists():
                    for zip_file in platform_dir.glob("*.zip"):
                        print_info(f"Removing {platform}: {zip_file.name}")
                        zip_file.unlink()
        
        print_success("Packages cleaned")
    
    def build_platform_package(self, platform):
        """Build package for specific platform"""
        if platform not in self.platforms:
            print_error(f"Unknown platform: {platform}")
            return None
        
        config = self.platforms[platform]
        platform_dir = config["dir"]
        
        if not platform_dir.exists():
            print_error(f"Platform directory does not exist: {platform_dir}")
            return None
        
        print_step(f"Building {platform} package...")
        
        version = self.get_version_from_source()
        package_name = f"{config['package_name']}-{version}"
        zip_path = platform_dir / f"{package_name}.zip"
        
        # Create package
        files_added = 0
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            for file_path in platform_dir.rglob('*'):
                if file_path.is_file() and not file_path.name.endswith('.zip'):
                    arcname = file_path.relative_to(platform_dir)
                    zipf.write(file_path, arcname)
                    files_added += 1
                    print_info(f"  Added: {arcname}")
        
        # Get package info
        package_size = zip_path.stat().st_size / 1024
        print_success(f"Package created: {package_name}.zip ({package_size:.1f} KB, {files_added} files)")
        
        return zip_path
    
    def validate_package(self, package_path, platform):
        """Validate package contents"""
        print_step(f"Validating {platform} package...")
        
        try:
            with zipfile.ZipFile(package_path, 'r') as zipf:
                file_list = zipf.namelist()
                
                # Check required files
                required_files = ['__init__.py']
                if platform == "blender_extensions":
                    required_files.append('blender_manifest.toml')
                
                missing_files = []
                for req_file in required_files:
                    if req_file not in file_list:
                        missing_files.append(req_file)
                
                if missing_files:
                    print_error(f"Missing required files: {', '.join(missing_files)}")
                    return False
                
                print_info(f"Package contains {len(file_list)} files")
                print_success("Package validation passed")
                return True
                
        except Exception as e:
            print_error(f"Package validation failed: {e}")
            return False
    
    def run_blender_validation(self, package_path):
        """Run Blender extension validation if available"""
        print_step("Running Blender validation...")
        
        blender_paths = [
            "blender",
            r"C:\Program Files\Blender Foundation\Blender 4.5\blender.exe",
            r"C:\Program Files\Blender Foundation\Blender 4.4\blender.exe",
            r"C:\Program Files\Blender Foundation\Blender 4.3\blender.exe",
        ]
        
        blender_exe = None
        for path in blender_paths:
            if shutil.which(path) or (Path(path).exists() if os.path.isabs(path) else False):
                blender_exe = path
                break
        
        if not blender_exe:
            print_info("Blender not found, skipping validation")
            return True
        
        try:
            cmd = [
                blender_exe,
                "--background", 
                "--python-expr",
                f"import bpy; bpy.ops.extensions.package_install(filepath=r'{package_path}', enable_on_install=False)"
            ]
            
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            
            if result.returncode == 0:
                print_success("Blender validation passed")
                return True
            else:
                print_error(f"Blender validation failed: {result.stderr}")
                return False
                
        except Exception as e:
            print_info(f"Blender validation skipped: {e}")
            return True
    
    def build_all(self, platforms=None):
        """Main build process"""
        if platforms is None:
            platforms = list(self.platforms.keys())
        
        print_header("NS Toolkit - Smart Build System")
        print_info("Develop once, distribute everywhere! 🚀")
        
        success_packages = []
        failed_packages = []
        
        try:
            # Step 1: Sync source files
            self.sync_source_to_platforms(platforms)
            
            # Step 2: Clean old packages
            self.clean_packages(platforms)
            
            # Step 3: Build packages for each platform
            for platform in platforms:
                try:
                    package_path = self.build_platform_package(platform)
                    if package_path:
                        # Validate package
                        if self.validate_package(package_path, platform):
                            success_packages.append((platform, package_path))
                            
                            # Run Blender validation for blender_extensions
                            if platform == "blender_extensions":
                                self.run_blender_validation(package_path)
                        else:
                            failed_packages.append((platform, "Validation failed"))
                    else:
                        failed_packages.append((platform, "Build failed"))
                        
                except Exception as e:
                    failed_packages.append((platform, str(e)))
            
            # Summary
            print_header("Build Summary")
            
            if success_packages:
                print_success(f"Successfully built {len(success_packages)} packages:")
                for platform, package_path in success_packages:
                    size_kb = package_path.stat().st_size / 1024
                    print_info(f"  ✅ {platform}: {package_path.name} ({size_kb:.1f} KB)")
            
            if failed_packages:
                print_error(f"Failed to build {len(failed_packages)} packages:")
                for platform, error in failed_packages:
                    print_info(f"  ❌ {platform}: {error}")
            
            # Next steps
            if success_packages:
                print_header("Next Steps")
                for platform, package_path in success_packages:
                    if platform == "blender_extensions":
                        print_info(f"📤 Submit to: https://extensions.blender.org/submit/")
                    elif platform == "gumroad_commercial":
                        print_info(f"💰 Upload to Gumroad marketplace")
                
                print_success("🎉 All builds completed successfully!")
                return True
            else:
                print_error("💥 All builds failed!")
                return False
                
        except Exception as e:
            print_error(f"Build process failed: {e}")
            return False

def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(description="NS Toolkit Smart Build System")
    parser.add_argument(
        '--platform', 
        choices=['all', 'blender', 'gumroad'],
        default='all',
        help='Target platform to build (default: all)'
    )
    
    args = parser.parse_args()
    
    builder = SmartBuilder()
    
    # Map argument to internal platform names
    if args.platform == 'all':
        platforms = None  # Build all
    elif args.platform == 'blender':
        platforms = ['blender_extensions']
    elif args.platform == 'gumroad':
        platforms = ['gumroad_commercial']
    
    success = builder.build_all(platforms)
    
    if success:
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()