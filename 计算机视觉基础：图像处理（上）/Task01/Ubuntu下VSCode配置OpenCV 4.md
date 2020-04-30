### Ubuntu下VSCode配置OpenCV 4

前提：

这里假设你在本地build opencv时，cmake时`BUILD_opencv_world=ON`(这样就只有一个so库，不然会有很多单独的so库),`CMAKE_BUILD_TYPE=DEBUG`(用于debug),`OPENCV_GENERATE_PKGCONFIG=ON`,建议通过cmake-gui设置这些参数。安装成功后，`sudo ldconfig`,然后`pkg-config --cflags --libs opencv4`就可以看到编译时include和link指令，应该是这样的

```shell
-I/usr/local/include/opencv4/opencv -I/usr/local/include/opencv4 -L/usr/local/lib -lopencv_world
```

不过你会发现第一个`-I`的文件夹并不存在，所以可以去掉，使用第二个`-I`即可

注：

- 如果你之前已经在本地编译安装过了opencv，如果想要卸载opencv重新安装，可以[参考](https://answers.opencv.org/question/209088/how-to-completely-remove-opencv3/)
- 以个人本地安装opencv4过程为例，你可能会在make过程中会遇到`xx.i`文件找不到，我是通过手动下载解决，可以通过运行`build/download_with_curl.sh`来下载（可能需要代理才能下得动，最后还要改名，放到相应的目录下。。）。还有另外一个可能问题，cmake时`BUILD_TESTS=OFF`即可。

VSCode配置:

首先安装c/c++、code runner插件，然后创建一个cpp项目。

```cpp
// hello.cpp
# include  <opencv2/xx> //这里一定要加opencv2前缀
int main(){
    // code here
}
```

相关配置说明

- 智能提示:可以在c_cpp_property.json设置includepath为`/usr/local/include/opencv4`

- debug配置: 在tasks.json中，假设你的编译器是`g++`(`command`参数)，你需要设置`args`参数才能正常debug，一般以下设置就够了

  ```json
  			"args": [
  				"-g",
  				"-o",
  				"${fileDirname}/${fileBasenameNoExtension}",
  				"-I/usr/local/include/opencv4",
  				"-L/usr/local/lib",
  				"${file}",
  				"-lopencv_world"
  			]
  ```

- 运行配置：默认情况code runner执行cpp文件时命令`cd $dir && g++ $fileName -o $fileNameWithoutExt && $dir$fileNameWithoutExt`,可以看到并没有include和link必要的文件和库，所以在.vscode/settings.json下设置即可

  ```json
      "code-runner.executorMap":{
          "cpp": 
          "cd $dir && g++ -o $fileNameWithoutExt -I/usr/local/include/opencv4 -L/usr/local/lib $fileName -lopencv_world && $dir$fileNameWithoutExt"
      }
  ```

  另外如果你的程序需要接受用户输入，那就在`file->preferences->settings`,查找`code-runner: Run In Terminal`并打勾即可

至此配置结束，你可以正常运行并debug到opencv的源码了。至于在Windows利用mingw来配置vscode运行opencv（mingw版），过程应该也是大致一样的。

