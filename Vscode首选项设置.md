# VScode设置

## 小白科普
- 打开首选项有*用户设置*和*工作区设置*。用户方式进行的设置，会应用于该用户打开的所有工程；而工作空间是指使用VS Code打开的某个文件夹，在该文件夹下会创建一个名为.vscode的隐藏文件夹，里面包含着仅适用于当前目录的VS Code的设置，工作空间的设置会覆盖用户的设置。
用户设置的文件保存在如下目录：
  - Windows `%APPDATA%\Code\User\settings.json`
  - Linux `$HOME/.config/Code/User/settings.json`
工作区设置的文件保存在工作区的.vscode文件夹下。

## 小白经验
1. 在首选项写设置时，要在每一行后加逗号。
2. 如果不能在 `.vscode` 里的 `settings.json` 上进行编程，则可以按下**F1**打开命令行，选择 `Preferences: Open User Settings`。
3. 选择好用的Vscode插件，有
> - Anaconda Extension Pack anaconda插件，提供第三方库的识别
> - Bracket Pair Colorizer 括号彩虹色插件
> - Chinese (Simplified) Language Pack for Visual Studio Code 中文插件
> - Code Runner 一键运行插件，右键和界面上方会多出Run Code 
> - GitLens — Git supercharged Git版本库管理插件
> - indent-rainbow 缩进彩虹色插件
> - One Dark Pro 暗黑主题插件
> - Path Intellisense 自动识别路径文件插件
> - TabNine 自动缩进插件
> - vscode-icons 更改Vscode的目录文件图标插件
> - YAML 语法插件（配合anaconda插件和python）
> - filesize 左下角显示文件大小插件
4. python路径设置需要找到设置的 `python.Python Pat`,可以推出其他的路径设置。

## VScode的一些‘BUG’
1. 如果出现*波浪错划*，比如python的turtle画图工具包会错划波浪线。打开用户设置（或工作区设置），找到 `python.linting.Pylint Args`,添加“--generate-members”，[参考博客](https://blog.csdn.net/SJM1996_fighting/article/details/103272538)。
2. 如果出现*run-coder输出界面乱码*，按**F1**打开用户设置区，找到设置 `code-runner.executorMap`,添加‘ "python": "set PYTHONIOENCODING=utf8 && C:\\Users\\hasee\\Anaconda3\\envs\\MAX\\python.exe" ’[参考博客](https://www.cnblogs.com/charleswong/p/11367196.html)。
3. 如果出现*Code Runner输出窗口提示无法在只读编辑器中编辑*,此时需要在插件code-runner设置中勾选 `Run In Terminal`，若报错无法更改，这说明设置Json文件编写错误，需要删去划红线的代码"--generate-members"。

