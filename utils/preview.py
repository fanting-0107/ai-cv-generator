"""
utils/preview.py
实时简历预览模块：接收简历信息，在控制台打印Markdown草稿预览
"""

def render_resume_preview(resume_data: dict):
    """
    根据简历字典，渲染当前简历草稿并打印到控制台
    :param resume_data: 简历信息字典，存放每一步录入的信息
    """
    print("\n" + "="*60)
    print("【实时简历草稿预览】")
    print("="*60)

    # 个人信息
    if resume_data.get("name"):
        print(f"# {resume_data['name']}")
        if resume_data.get("contact"):
            print(f"{resume_data['contact']}\n")

    # 教育经历
    if resume_data.get("education"):
        print("## 教育背景")
        print(f"{resume_data['education']}\n")

    # 项目经历
    if resume_data.get("projects"):
        print("## 项目经历")
        print(f"{resume_data['projects']}\n")

    # 专业技能
    if resume_data.get("skills"):
        print("## 专业技能")
        print(f"{resume_data['skills']}\n")

    # 获奖经历
    if resume_data.get("awards"):
        print("## 荣誉奖项")
        print(f"{resume_data['awards']}\n")

    print("="*60 + "\n")


def show_final_markdown_preview(md_content: str):
    """
    展示AI生成完成后的完整Markdown简历（最终预览）
    """
    print("\n" + "="*70)
    print("【AI生成完成｜完整简历预览】")
    print("="*70)
    print(md_content)
    print("="*70 + "\n")
