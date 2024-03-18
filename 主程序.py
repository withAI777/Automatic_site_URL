# 导入所需模块
import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
import random
from tqdm import tqdm
import sys
import time
from colorama import init, Fore, Style # 输出样式库
init(autoreset = True) # 初始化 colorama -- 只针对当前print生效

# # 获取当前可执行文件所在的文件夹路径
base_folder = os.path.dirname(sys.executable) + os.path.sep

# # 在路径末尾添加路径分隔符，确保路径以反斜杠结尾
base_folder = base_folder.rstrip(os.path.sep) + os.path.sep

# 控制台运行程序
# base_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')

# 定义各个表格路径
each_path = base_folder + r"数据表格"

# 定义总表格路径
all_path = base_folder + r"收录表.xlsx"

def print_center(text):
    cols = os.get_terminal_size().columns
    lines = text.split('\n')
    for line in lines:
        print("\033[1;32m" + line.center(cols-20) + "\033[0m")  # 设置颜色，并在每行输出开头使用

# 输出带颜色的文本
print_center(r"""
     __  __   _   _   ____   _  __
    |  \/  | | | | | / ___| | |/ /
      ----|-|\/|-|-|-|-|-|-\-_-_\-|-'-/---->>>
    | |  | | | |_| |  ___) || . \
    |_|  |_|  \___/  |____/ |_|\_\

获取更多项目：https://github.com/withAI777/en_state_demo_video
""")
print("-" * 100)

# 检查all_path表是否存在，如果不存在则创建
if not os.path.exists(all_path):
    # 创建一个空的DataFrame
    all_data = pd.DataFrame(columns=["url", "category", "Date", "Template", "View Count"])
    # 将DataFrame保存为Excel文件
    all_data.to_excel(all_path, index=False)

# 读取总表格数据
all_data = pd.read_excel(all_path)

# 检查是否存在第六列，如果不存在则创建
if '是否被收录' not in all_data.columns:
    # 遍历each_path文件夹内的excel表格
    for filename in os.listdir(each_path):
        if filename.endswith(".xlsx"):
            # 读取单个excel表格数据
            data = pd.read_excel(os.path.join(each_path, filename))
            # 将单个表格数据合并到总表格中
            all_data = pd.concat([all_data, data], ignore_index=True)
    
    # 保存合并后的总表格数据到all_path表
    all_data['是否被收录'] = ""
    all_data.to_excel(all_path, index=False)

# 获取chromedriver路径和谷歌浏览器程序路径
# 检查保存路径的文件是否存在
path_file = "path.txt"
if os.path.exists(path_file):
    # 加载保存的路径
    with open(path_file, "r") as f:
        chrome_driver_path = f.readline().strip()
        chrome_browser_path = f.readline().strip()
    # 询问用户是否需要更改路径
    change_paths = input(Fore.GREEN + "是否需要更改之前设置的路径？(y/n): ").strip().lower()
    if change_paths == 'y':
        chrome_driver_path = input(Fore.GREEN + "请输入新的ChromeDriver路径：")
        chrome_browser_path = input(Fore.GREEN + "请输入新的谷歌浏览器程序路径：")
        # 更新保存的路径
        with open(path_file, "w") as f:
            f.write(chrome_driver_path + "\n")
            f.write(chrome_browser_path + "\n")
        print("-" * 50)
    else:
        print("-" * 50)
else:
    # 第一次运行程序，询问用户输入路径
    chrome_driver_path = input(Fore.GREEN + "请输入ChromeDriver路径：")
    chrome_browser_path = input(Fore.GREEN + "请输入谷歌浏览器程序路径：")
    # 将文件保存到路径中
    with open(path_file, "w") as f:
        f.write(chrome_driver_path + "\n")
        f.write(chrome_browser_path + "\n")
    print("-" * 50)

# 配置ChromeDriver
chrome_service = Service(chrome_driver_path)
chrome_service.start()
options = webdriver.ChromeOptions()
options.binary_location = chrome_browser_path
options.add_argument("--log-level=3") # 禁用输出错误信息
# options.add_argument("--headless") # 无头模式，不显示浏览器窗口
options.add_argument("--disable-blink-features=AutomationControlled")  # 禁用自动化测试标志
driver = webdriver.Chrome(service=chrome_service, options=options)

# 遍历表格第一列数据，进行谷歌检索
total_length = len(all_data)

for index, row in tqdm(all_data.iterrows(), total=total_length, desc="进度", colour="green"):
    # 检查第六列是否存在数据，如果存在则跳过该行
    if not pd.isnull(row['是否被收录']):
        continue

    url = row['url']
    # 构建谷歌搜索链接
    google_search_url = f"https://www.google.com/search?q=site%3A{url}"
    
    # 生成随机的User-Agents --- 打包为exe后有问题，故注释
    # ua = UserAgent()
    # user_agent = ua.random
    # options.add_argument(f"user-agent={user_agent}")

    driver.get(google_search_url)
    # 等待页面加载完成
    time.sleep(random.uniform(2, 5))
    html_content = driver.page_source
    
    # 检查该页面是否被 Google 收录
    current_url = driver.current_url
    if current_url.startswith("https://www.google.com/sorry"):
        all_data.loc[index, '是否被收录'] = ''
        print("-" * 50)
        print(Fore.CYAN + Style.BRIGHT + f"{url}已被检测反爬，请切换代理节点后重新运行程序。")
        input(Fore.GREEN + "按任意键结束当前程序")
        try:
            if sys.platform.startswith('win'):  # 检查操作系统是否为Windows
                import msvcrt
                msvcrt.getch()  # 等待用户按下任意键
            else:
                input()  # 在非Windows环境中等待用户输入任意内容
        except KeyboardInterrupt:  # 捕获键盘中断信号，如Ctrl+C
            pass
        continue

    # 检查指定元素判定是否被收录
    soup = BeautifulSoup(html_content, 'html.parser')
    links = soup.find_all('a', attrs={'jsname': 'UWckNb'})  # 查找所有包含指定属性的<a>标签
    # 根据搜索结果是否存在来填充是否被收录列
    # 使用loc来索引
    if len(links) > 0:
        all_data.loc[index, '是否被收录'] = "是"
    else:
        all_data.loc[index, '是否被收录'] = "否"

    # 保存更新后的表格数据
    all_data.to_excel(all_path, index=False)

# 关闭浏览器
driver.quit()

# 提示用户关闭程序
print("-" * 50)
print(Fore.YELLOW + "所有URL已site完毕")
for i in range(5, 0, -1):
    sys.stdout.write("\r程序将在{}秒后自动结束运行".format(i))
    sys.stdout.flush()
    time.sleep(1)
sys.exit()
