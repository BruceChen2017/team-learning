## Windows下配置OpenCV
### 前提
- 下载pre-build的[opencv](https://sourceforge.net/projects/opencvlibrary/files/4.3.0/opencv-4.3.0-vc14_vc15.exe/download)并安装，比如`d:\opencv`
- 打开cmd设置变量**OPENCV_DIR**  
`setx -m OPENCV_DIR D:\OpenCV\Build\x64\vc15` -->vc15应该对应vs2017及以上
- 添加`%OPENCV_DIR%\bin`到系统的**PATH**变量中

### Visual Studio 2017 x64 Debug模式下配置 
- 添加include：项目 -> 某项目名 属性 -> C/C++ -> 常规 -> 附件包含目录 -> 添加  `%OPENCV_DIR%\..\..\include`
- 添加lib: 项目-> 某项目名 属性 -> 链接器 ->
  - 常规 -> 附加库目录 -> 添加：`%OPENCV_DIR%\lib`
  - 输入 -> 附加依赖项 -> 添加：`opencv_world430d.lib`
- 添加symbols: 工具 -> 选项 -> 调试 -> 符号 -> 符号文件的位置 -> 添加：`%OPENCV_DIR%\bin`   

实际上，如果只是运行的话，前两步就行了。如果要调试代码的话，因为程序无法找到`opencv_world430d.dll`，所以你要把放在与exe文件同目录下，或者直接把它放在`c:\windows\system32`下才行，这样加上第三步就可以调试了

### VS code下配置
TODO