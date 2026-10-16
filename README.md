# AutoResumeGenerator
AI Agent，根据用户输入信息自动生成个人简历。

## 项目简介
小型AI Agent，接收用户个人信息，调用大模型生成结构化简历内容，输出markdown简历。
面向AI专业求职，自动提炼项目、技能描述，优化简历话术。

## MVP最小可行版本
功能清单：
1. 用户输入表单：姓名、联系方式、教育经历、项目经历、技能
2. 调用大模型，润色简历内容，突出AI方向能力；规范排版
3. 输出简历markdown文件，保存到本地
4. 简单命令行交互界面
5. 实时预览与最终确认功能

## 开发计划
- [x] 初始化git仓库，增加.gitignore
- [x] 搭建项目文件结构
- [x] 交互式分步采集简历信息，可选录入目标岗位JD
- [x] 实时预览：每录入一段信息，控制台展示当前简历草稿
- [x] Agent模块：结合【个人信息+岗位JD】润色简历，标准化Markdown排版
- [x] 用户确认机制：生成完整简历后，等待用户确认，确认通过才写入文件
- [x] 输出Markdown简历至 output_cv/ 文件夹
- [x] MVP测试，调试优化

### 导出环境
`conda env export --from-history > environment.yml`

### 环境准备
本项目使用 Anaconda 管理Python虚拟环境
1. 创建虚拟环境：
`conda create -n 虚拟环境名 python=3.10`
2. 激活环境：
`conda activate 虚拟环境名`
3. 在环境内安装依赖：
`pip install python-dotenv openai`
4. VS Code 选择解释器：AutoResume_env Python3.10.22

## 环境搭建
### Conda（推荐）
```bash
# 创建conda虚拟环境
conda env create -f environment.yml
# 激活环境
conda activate AutoResume_env
