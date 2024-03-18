# Automatic_site_URL

这是一个通过Google浏览器自动site URL的项目，你可以快速检索你所有的文章是否被收录，并且可视化的呈现表格，方便你决定哪些文章是否应该修改/优化
你**必须**安装谷歌浏览器，本程序不支持其它浏览器<br>

点此查看我的文章的部分[示例数据](https://github.com/withAI777/Automatic_site_URL/blob/main/%E7%A4%BA%E4%BE%8B%E6%94%B6%E5%BD%95%E8%A1%A8.csv)，项目url已打码处理，第1-5列是基础数据，第6列是“是否被收录”的数据

## 声明

- 本程序仅供个人测试使用<br>
- 本程序不涉及爬取任何用户隐私数据

## 如何使用

### 下载必要插件

#### 你需要下载自己浏览器版本对应的ChromeDriver

- **查看自己浏览器版本**，请在地址栏输入`chrome://version`，第一行的`Google Chrome`便是你浏览器的版本
- 然后你可以复制版本，在ChrmoeDriver下载页面ctrl+F进行快速查询并下载版本对应的ChrmoeDriver

| 插件名称 | 下载链接 | 作用 |
|---|---|---|
| 油猴脚本 | [点此下载](https://chromewebstore.google.com/detail/%E7%AF%A1%E6%94%B9%E7%8C%B4/dhdgffkkebhmkfjojejmpbldmpobfkfo?hl=zh)     | 后台爬取自己文章的数据    |
| 谷歌浏览器| [点此下载](https://www.google.com/intl/zh-CN/chrome/)| 必须基于谷歌浏览器实现自动site |
| ChromeDriver| [点此下载](https://chromedriver.chromium.org/downloads)      | 浏览器自动化site的必要依赖 |

### [点此下载主程序压缩包](https://github.com/withAI777/Automatic_site_URL/raw/main/%E6%89%B9%E9%87%8F%E8%87%AA%E5%8A%A8%E5%8C%96site_URL.zip)
解压到任意文件夹，你会得到**四个文件**，分别是`数据表格`文件夹，`_internal`文件夹，`保存自己文章的数据到表格.js`，`主程序.exe`
| 文件名称 | 作用 |
|---|---|
| 数据表格 文件夹 | 该文件夹存储自己文章的数据表格 |
| _internal 文件夹 | 必要的依赖文件不要改动|
| 保存自己文章的数据到表格.js| 油猴脚本代码 |
| 主程序.exe| 该软件调用Chrome浏览器实现自动site |

### 导入爬虫代码到油猴插件
- 点击后台数据的`MINE`，复制页面URL
- **在你刚刚复制的URL其后加一个***，以表示匹配所有页面
- 打开油猴脚本，导入`保存自己文章的数据到表格.js`文件，注意修改代码`第7行`为你的文章页面的url(注意末尾加上*)
<p align = "center">
<img src="https://github.com/withAI777/Automatic_site_URL/blob/main/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E6%B7%BB%E5%8A%A0%E6%B2%B9%E7%8C%B4%E8%84%9A%E6%9C%AC.jpg">
</p>
<p align = "center">
<img src="https://github.com/withAI777/Automatic_site_URL/blob/main/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E4%BF%AE%E6%94%B9%E4%BB%A3%E7%A0%81%E7%AC%AC7%E8%A1%8C.jpg">
</p>

### 启动脚本，刷新页面，会自动爬取一系列数据表
- 启动脚本后，会在油猴脚本上显示一个红色的1
![image](https://github.com/withAI777/Automatic_site_URL/blob/main/%E6%BC%94%E7%A4%BA%E5%9B%BE%E7%89%87/%E5%90%AF%E5%8A%A8%E6%B2%B9%E7%8C%B4%E8%84%9A%E6%9C%AC.jpg)
- 爬取的所有数据表格按照顺序会从“1.xlsx” - “最后一页.xlsx”进行命名
- **爬取完毕所有数据表格后，将它们全部放在解压后的`数据表格`文件夹内**

### 运行程序，第一次运行需按照提示输入你电脑内软件的相关路径，路径以exe结尾
- ChromeDriver路径，在我的电脑上是：`E:\Google\Chrome\chromedriver-win64\chromedriver.exe`
- Chrome谷歌浏览器路径，在我的电脑上是：`E:\Google\Chrome\Application\chrome.exe`
- 此后运行程序，你可以根据提示选择是否更改之前设定的路径，你输入的路径将会自动创建并保存在`path.txt`文件内
- 如果程序无法正常运行，你可能需要**将ChromeDriver加入你的path环境变量中**：`windows搜索 - 编辑系统环境变量 - 高级 - 环境变量 - 双击Path - 新建 - 输入你的ChromeDriver路径 - 保存`

### 查看文章是否被收录的数据
- 第一次启动程序，将会自动创建一个你所有爬取到的数据表的合并表，自动命名为`收录表.xlsx`，**不要对它进行重命名或改动**
- 在**表格的第六列**可以查看文章是否被收录（是/否）

## 注意事项

### 运行程序的注意事项
- **第一次启动程序可能会自动停止运行程序或者打开浏览器后没反应或者直接自动结束程序，此时关闭浏览器和命令行窗口重新点击程序运行即可。** 原因不清楚，无法debug
- **程序运行过程中，不要打开表格查看数据！** 否则会报错或者程序崩溃

### 必看：关于谷歌反爬虫限制
- 由于谷歌反爬虫限制，此程序不能一次完成所有URL的site，一次大概能批量site60个URL，然后如果检测到被谷歌反爬虫，那么会输出`xx已被检测反爬，请切换代理节点后重新运行程序。`，此时请**关闭浏览器和命令行窗口，切换代理IP，重新运行程序**，或者等待一会重新运行程序，程序会自动从上次被反爬的URL的位置开始继续运行
- 所有文章的URL site完毕后，会自动输出`所有URL已site完毕`，然后自动关闭程序

## 开发者阅读

### 原理
- 使用`js`编写油猴脚本，爬取后台页面数据
- 使用`python`基于selenium库和chromedriver编写爬虫模拟用户操作，通过遍历数据表格的第一列，依次进行自动化site操作。
- 通过检测是否跳转到`https://www.google.com/sorry`页面，判定是否被谷歌检测爬虫，如果是则程序结束运行

### 源代码
[js源代码](https://github.com/withAI777/Automatic_site_URL/blob/main/%E4%BF%9D%E5%AD%98%E8%87%AA%E5%B7%B1%E6%96%87%E7%AB%A0%E7%9A%84%E6%95%B0%E6%8D%AE%E5%88%B0%E8%A1%A8%E6%A0%BC.js)<br>
[python源代码](https://github.com/withAI777/Automatic_site_URL/blob/main/%E4%B8%BB%E7%A8%8B%E5%BA%8F.py)

### 部分源代码释意
- 通过在页面等待随机2-5秒，尽可能的模拟真实用户，避免被反爬
```python
# 等待页面加载完成
    time.sleep(random.uniform(2, 5))
    html_content = driver.page_source
```
- 无头模式能够更方便的使用程序，但是似乎会导致搜索结果有些问题，一些URL原本被收录，但是判断为了没有被收录，故注释<br>
`# options.add_argument("--headless") # 无头模式，不显示浏览器窗口`

### 程序缺陷
- fake_useragent库打包为exe后，运行程序会报错导入失败，故将相关代码注释，但因此会加大被反爬的可能，导致原本能遍历约80个URL才被反爬，现在遍历约50-60个就会被反爬
```python
from fake_useragent import UserAgent
import random
# 生成随机的User-Agents --- 打包为exe后有问题，故注释
# ua = UserAgent()
# user_agent = ua.random
# options.add_argument(f"user-agent={user_agent}")
```

## 后记
如果对你有用的话，[打赏一元](https://github.com/withAI777/Automatic_site_URL/tree/main/%E8%AF%B7%E7%8B%A0%E7%8B%A0%E6%89%93%E8%B5%8F%E6%88%91)行不行🥰<br>
代码及注释使用chatGPT+手工编写
