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
- [ ] 搭建项目文件结构
- [ ] 交互式分步采集简历信息，可选录入目标岗位JD
- [ ] 实时预览：每录入一段信息，控制台展示当前简历草稿
- [ ] Agent模块：结合【个人信息+岗位JD】润色简历，标准化Markdown排版
- [ ] 用户确认机制：生成完整简历后，等待用户确认，确认通过才写入文件
- [ ] 输出Markdown简历至 output_cv/ 文件夹
- [ ] 测试，调试优化

### 环境准备
本项目使用 Anaconda 管理Python虚拟环境
1. 创建虚拟环境
2. 激活环境
3. 在环境内安装依赖：
`pip install python-dotenv openai`
4. VS Code 选择解释器

### 导出环境（可选）
`conda env export > environment.yml`

### 环境准备
本项目使用 Anaconda 管理Python虚拟环境
1. 创建虚拟环境：
`conda create -n ai-cv-gen python=3.10`
2. 激活环境：
`conda activate ai-cv-gen`
3. 在环境内安装依赖：
`pip install python-dotenv openai`

4. VS Code 选择解释器：ai-cv-gen Python3.10

### 导出环境（可选）
`conda env export > environment.yml`

### 重建环境（可选）
`conda env create -f environment.yml`

