"""
agent/cv_agent.py
简历Agent核心模块
接收用户个人信息 + 岗位JD，调用大模型，生成排版规范的Markdown简历
"""
from openai import APIError, APIConnectionError, AuthenticationError
from openai import OpenAI
from dotenv import load_dotenv
import os

# 加载.env里的API密钥
load_dotenv()

def build_resume_prompt(resume_data: dict, jd_text: str):
    """
    构造给大模型的提示词
    :param resume_data: 用户填写的简历信息字典
    :param jd_text: 目标岗位JD文本，为空则走通用简历模式
    :return: 完整prompt字符串
    """
    # 把字典内容转为文本
    info_text = f"""
姓名：{resume_data.get('name','')}
联系方式：{resume_data.get('contact','')}
教育背景：{resume_data.get('education','')}
项目经历：{resume_data.get('projects','')}
专业技能：{resume_data.get('skills','')}
荣誉奖项：{resume_data.get('awards','')}
"""
    if jd_text.strip():
        jd_part = f"""
【目标岗位招聘JD】
{jd_text}
要求：仔细提取JD里关键词，在简历里对齐岗位要求，突出匹配能力，优先展示AI相关项目、模型指标、数据集等亮点。
"""
    else:
        jd_part = "没有指定目标岗位，请生成通用人工智能方向求职简历，突出AI项目、编程、模型相关能力。"

    prompt = f"""
你是专业简历优化Agent，任务：根据下面用户信息 + JD，输出一份美观规范的Markdown求职简历。
排版硬性规则（严格遵守）：
1. 使用Markdown标题层级：# 姓名（一级标题）；## 作为大模块标题（教育背景、项目经历、专业技能、荣誉奖项）；### 用于项目子标题
2. 使用无序列表- 罗列技能、项目要点；段落之间保留空行，保证阅读舒适
3. 优化语言，量化成果，适合AI岗位求职，不要空话，突出技术细节
4. 不要额外增加解释文字，**只输出Markdown简历正文**，不要多余说明

{info_text}
{jd_part}
"""
    return prompt


def generate_resume_markdown(resume_data: dict, jd_text: str) -> str:
    """
    调用DeepSeek大模型API，生成最终Markdown简历
    """
    client = OpenAI(
        api_key=os.getenv("DEEPSEEK_API_KEY"),
        base_url="https://api.deepseek.com"
    )
    prompt = build_resume_prompt(resume_data, jd_text)

    try:
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
    except (AuthenticationError, APIConnectionError, APIError) as err:
        # 捕获OpenAI系列SDK异常，向上抛出，main.py做捕获处理
        raise err
    md_result = response.choices[0].message.content.strip()
    return md_result
