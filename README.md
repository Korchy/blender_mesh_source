# Mesh Source
Blender 3D add-on for converting meshes to python source code and saving it in a library for further distribution.

Add-on functionality
-
When you click on the "Mesh to Text" button the source code is generated for the currently selected meshes and shown in the "Text Editor" window.

<img src="https://b3d.interplanety.org/wp-content/upload_content/2020/11/preview_01_1200x600-560x280.jpg"><p>

The code can be copied to the clipboard or saved to a separate text file and then pasted or opened in any separate Blender project. When this code is executed, by clicking the "Run Script" button, the same set of meshes will be created in the scene.

The "Mesh Source" add-on also has its own library into which you can save the meshes source code. To save the mesh sources to the local library press the "Mesh to Library" button. Saved meshes can be loaded from the library right away.

<img src="https://b3d.interplanety.org/wp-content/upload_content/2020/11/preview_02_1200x600-560x280.jpg"><p>

If you want to distribute your materials to other users, the “Mesh Source” material library can be compiled into a separate add-on. Specify the path and click the “Distribute Library as Add-on” button. The complete archive with an add-on that includes the entire library of materials will be created. Users just need to download the add-on you provided and install it, after which they can immediately use the materials you provide.

Important
-
The local mesh source library is stored in the add-on directory. If you need to temporarily remove or reinstall the add-on, be sure to back up the library in a separate place on the disk first. After reinstalling the add-on, the library can be restored simply by copying it to the "mesh_source_library" directory of the add-on.

The following data is supported in meshes source code:

- mesh data (points, edges, polygons)
- vertex groups
- UV-s
- mesh modifier stack

Note that materials assigned to a mesh are not processed. The "NodeTree Source" add-on is intended for working with materials.

Current add-on version
-
1.0.0.

Blender versions
-
2.83, 2.90, 2.91

Location and call
-
“3D Viewport” window – N-panel – the “Mesh Source” tab

Installation
-
- Download the *.zip archive with the add-on distributive.
- The “Preferences” window — Add-ons — Install… — specify the downloaded archive.

Version history

1.0.0.
- This release.
